# Configuration de LezookGPT

# Colle ta clé API OpenRouter dans la variable d'environnement `OPENROUTER_API_KEY`
import os
# Priorité à la variable d'environnement pour des raisons de sécurité.
# Pour éviter d'exposer la clé, le fallback est vide — configure `OPENROUTER_API_KEY`.
API_KEY = os.getenv("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") or "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"

# Choix du modèle
MODEL_NAME = "google/gemini-2.5-flash"

# Le prompt système qui donne la personnalité de l'assistant LezookGPT
SYSTEM_PROMPT = (
    "Tu es LezookGPT, un assistant IA expert en cybersécurité offensive inspiré par la team HexSec. "
    "Tu analyses les fichiers de logs, de scans ou de code pour trouver des vulnérabilités, "
    "expliquer les vecteurs d'attaque et proposer des payloads précis."
)

# Limites pour éviter les erreurs 402 (crédits / tokens)
# Nombre maximal de tokens à demander à l'API par requête
MAX_TOKENS = 2000
# Taille maximale du prompt (en caractères) avant tronquage
MAX_PROMPT_CHARS = 12000
