import requests
import json
import config


def _ensure_system_prompt(messages):
    """Assure que le prompt système est présent en première position."""
    if not messages:
        return [{"role": "system", "content": config.SYSTEM_PROMPT}]
    if messages[0].get('role') != 'system':
        return [{"role": "system", "content": config.SYSTEM_PROMPT}] + messages
    return messages


def _chunk_text(text, size):
    return [text[i:i+size] for i in range(0, len(text), size)]


def envoyer_requete_ia(prompt_utilisateur=None, messages=None):
    """Envoie une requête conversationnelle à OpenRouter.

    - `prompt_utilisateur` : une chaîne unique (compatibilité ascendante)
    - `messages` : liste de dicts {'role': 'user'|'assistant'|'system', 'content': '...'}
    """
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {config.API_KEY}",
        "Content-Type": "application/json"
    }

    max_chars = getattr(config, 'MAX_PROMPT_CHARS', 12000)

    # Construire la liste de messages si on a reçu un prompt simple
    if messages is None:
        if isinstance(prompt_utilisateur, str) and len(prompt_utilisateur) > max_chars:
            chunks = _chunk_text(prompt_utilisateur, max_chars)
            msgs = [{"role": "system", "content": config.SYSTEM_PROMPT}]
            for idx, chunk in enumerate(chunks, 1):
                msgs.append({
                    "role": "user",
                    "content": f"[FICHIER PART {idx}/{len(chunks)}]\n{chunk}"
                })
            messages = msgs
        else:
            messages = [
                {"role": "system", "content": config.SYSTEM_PROMPT},
                {"role": "user", "content": prompt_utilisateur or ""}
            ]
    else:
        # s'assurer que le system prompt est présent
        messages = _ensure_system_prompt(messages)

    donnees = {
        "model": config.MODEL_NAME,
        "messages": messages,
        "max_tokens": getattr(config, 'MAX_TOKENS', 2000)
    }

    try:
        reponse = requests.post(url, headers=headers, data=json.dumps(donnees), timeout=30)

        if reponse.status_code == 200:
            resultat = reponse.json()
            return resultat['choices'][0]['message']['content']
        elif reponse.status_code == 402:
            try:
                data = reponse.json()
                err_msg = data.get('error', {}).get('message') or reponse.text
            except Exception:
                err_msg = reponse.text
            return (f"[ERREUR 402 - Crédits insuffisants] {err_msg}\n"
                    f"Solution rapide: réduisez `MAX_TOKENS` (actuellement {getattr(config, 'MAX_TOKENS', 2000)})\n"
                    "Ou augmentez vos crédits sur https://openrouter.ai/settings/credits")
        else:
            return f"[ERREUR Serveur] Code {reponse.status_code} : {reponse.text}"

    except requests.exceptions.ConnectionError:
        return "[ERREUR] Impossible de se connecter. Vérifie que ta connexion/forfait est activé."
    except Exception as e:
        return f"[ERREUR Imprévue] {e}"
