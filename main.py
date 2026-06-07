import os
import config
import ia_client
import theme
from colorama import init, Fore, Style

PROMPT_PREFIX = (f"\n{Fore.GREEN}┌─[{Fore.RED}LezookGPT{Fore.GREEN}]──[{Fore.RED}~{Fore.GREEN}]─[{Fore.YELLOW}menu{Fore.GREEN}]:\n└─────► " + Fore.RESET).lower()

LANGUAGE_LABELS = {
    "fr": {
        "menu_title": "Menu",
        "conversation": "Conversation avec LezookGPT",
        "file_access": "Accéssion au fichier",
        "back": "Sortir",
        "language_title": "Option de la langue",
    },
    "en": {
        "menu_title": "Menu",
        "conversation": "Conversation with LezookGPT",
        "file_access": "File access\t",
        "back": "Back",
        "language_title": "Language option",
    },
    "mg": {
        "menu_title": "Menu",
        "conversation": "Resadresaka amin' LezookGPT",
        "file_access": "Fidirana rakitra",
        "back": "Sortir",
        "language_title": "Safidin'ny fiteny",
    },
}


def select_language():
    while True:
        theme.clear_console()
        print(theme.big_banner())
        print(f"\n\n\n\t   -----------------------------------------------------" )
        print(f"\t |                  {Fore.GREEN}Option de la langue{Fore.WHITE}                 |" )
        print(f"\t   -----------------------------------------------------" )
        print(f"\n\t  {Fore.WHITE}|\t{Fore.WHITE}- [{Fore.GREEN}1{Fore.WHITE}]{Fore.GREEN}{Fore.WHITE} : {Fore.GREEN}Français{Fore.WHITE}\t\t\t      |")
        print(f"\t  {Fore.WHITE}|\t{Fore.WHITE}- [{Fore.CYAN}2{Fore.WHITE}]{Fore.CYAN}{Fore.WHITE} :{Fore.CYAN} Anglais\t\t\t\t      {Fore.WHITE}|")
        print(f"\t  {Fore.WHITE}|\t{Fore.WHITE}- [{Fore.CYAN}3{Fore.WHITE}] : {Fore.CYAN}Malagasy\t\t\t      {Fore.WHITE}|")
        print(f"\t  {Fore.WHITE}|\t{Fore.WHITE}- [{Fore.RED}4{Fore.WHITE}] : {Fore.RED}Sortir (Exit) \t\t\t      {Fore.WHITE}|")
        print(f"\t   {Fore.WHITE}---------------------------------------------------" )

        choice = input('\n' + PROMPT_PREFIX).strip()
        if choice == '1':
            return 'fr'
        elif choice == '2':
            return 'en'
        elif choice == '3':
            return 'mg'
        elif choice == '4':
            print(theme.info("\n\n\t 🧸 Au revoir 🫶. Merci d'utiliser Lezook GPT☠️."))
            return None
        else:
            print(theme.warn("\t[☢️ Choix invalide !]"))


def lire_fichier(chemin):
    if not os.path.exists(chemin):
        return None, f"[!] Erreur : Le fichier '{chemin}' n'existe pas."
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return f.read(), None
    except Exception as e:
        return None, f"[!] Erreur lors de la lecture du fichier : {e}"


def demarrer_session():
    # 1. Demande du fichier à analyser
    chemin_fichier = input("\n" + theme.prompt_label("[?] Glissez/Déposez ou tapez le chemin du fichier à analyser : ")).strip()

    contenu_fichier, err = lire_fichier(chemin_fichier)
    if err:
        print(err)
        return
    print(theme.info("[+] Fichier chargé avec succès."))

    # 3. Demande de précision à l'utilisateur
    consigne = input(theme.prompt_label("[?] Que doit faire l'IA avec ce fichier ? (Ex: trouve les failles) : "))

    # Construire messages conversationnels : inclure système, le fichier (éventuellement chunké), puis la consigne
    messages = []
    max_chars = getattr(__import__('config'), 'MAX_PROMPT_CHARS', 12000)
    if isinstance(contenu_fichier, str) and len(contenu_fichier) > max_chars:
        # splitter en parties
        parts = [contenu_fichier[i:i+max_chars] for i in range(0, len(contenu_fichier), max_chars)]
        for idx, part in enumerate(parts, 1):
            messages.append({"role": "user", "content": f"[FICHIER PART {idx}/{len(parts)}]\n{part}"})
    else:
        messages.append({"role": "user", "content": f"[FICHIER]\n{contenu_fichier}"})

    messages.append({"role": "user", "content": f"Consigne : {consigne}"})

    print("\n" + theme.info("[...] Connexion à l'API en cours (Analyse de sécurité)..."))
    reponse_ia = ia_client.envoyer_requete_ia(messages=messages)

    print("\n" + theme.banner("LezookGPT"))
    print(theme.info(" RAPPORT D'ANALYSE LezookGPT "))
    print(reponse_ia)
    print(theme.banner("LezookGPT"))

    # Ajouter la réponse de l'IA à l'historique et entrer en mode chat continu
    messages.append({"role": "assistant", "content": reponse_ia})

    print("\n" + theme.info("Mode conversationnel activé. Écris 'exit' pour quitter."))
    while True:
        user_msg = input('\n' + theme.prompt_label('[To IA] : ')).strip()
        if not user_msg:
            continue
        if user_msg.lower() in ('exit', 'quit'):
            print(theme.info('Fin de la session.'))
            break
        messages.append({"role": "user", "content": user_msg})
        reponse = ia_client.envoyer_requete_ia(messages=messages)
        print('\n' + theme.warn('[IA] ') + reponse)
        messages.append({"role": "assistant", "content": reponse})


def conversation_mode():
    print(theme.info("Mode conversationnel. Écris 'exit' pour revenir au menu."))
    history = [{"role": "system", "content": config.SYSTEM_PROMPT}]
    while True:
        user_msg = input(PROMPT_PREFIX).strip()
        if not user_msg:
            continue
        if user_msg.lower() in ('exit', 'quit'):
            print(theme.info('Retour au menu.'))
            break
        history.append({"role": "user", "content": user_msg})
        resp = ia_client.envoyer_requete_ia(messages=history)
        print(theme.warn('[IA] ') + resp)
        history.append({"role": "assistant", "content": resp})


def file_upload_mode():
    # reuse existing flow for file upload + analysis
    chemin_fichier = input(PROMPT_PREFIX + "Chemin du fichier à analyser: ").strip()
    contenu_fichier, err = lire_fichier(chemin_fichier)
    if err:
        print(theme.error(err))
        return
    print(theme.info('[+] Fichier chargé avec succès.'))
    consigne = input(PROMPT_PREFIX + "Que doit faire l'IA avec ce fichier ? : ")
    messages = []
    max_chars = getattr(__import__('config'), 'MAX_PROMPT_CHARS', 12000)
    if isinstance(contenu_fichier, str) and len(contenu_fichier) > max_chars:
        parts = [contenu_fichier[i:i+max_chars] for i in range(0, len(contenu_fichier), max_chars)]
        for idx, part in enumerate(parts, 1):
            messages.append({"role": "user", "content": f"[FICHIER PART {idx}/{len(parts)}]\n{part}"})
    else:
        messages.append({"role": "user", "content": f"[FICHIER]\n{contenu_fichier}"})
    messages.append({"role": "user", "content": f"Consigne : {consigne}"})
    print(theme.info("[...] Connexion à l'API en cours (Analyse de sécurité)..."))
    reponse_ia = ia_client.envoyer_requete_ia(messages=messages)
    print(theme.banner("LezookGPT"))
    print(theme.info(" RAPPORT D'ANALYSE LezookGPT "))
    print(reponse_ia)
    print(theme.banner("LezookGPT"))


def show_menu(language="fr"):
    labels = LANGUAGE_LABELS.get(language, LANGUAGE_LABELS['fr'])
    while True:
        theme.clear_console()
        print(theme.big_banner())
        print(f"\n\n\n\t  -----------------------------------------------------" )
        print(f"\t |                        {Fore.GREEN}{labels['menu_title']}{Fore.WHITE}                         |" )
        print(f"\t  -----------------------------------------------------" )
        print(f"\n\t  {Fore.WHITE}|\t{Fore.WHITE}- [{Fore.GREEN}1{Fore.WHITE}]{Fore.GREEN}{Fore.WHITE} : {Fore.GREEN}{labels['conversation']}{Fore.WHITE}           |")
        print(f"\t  {Fore.WHITE}|\t{Fore.WHITE}- [{Fore.CYAN}2{Fore.WHITE}]{Fore.CYAN}{Fore.WHITE} :{Fore.CYAN} {labels['file_access']} \t\t      {Fore.WHITE}|")
        print(f"\t  {Fore.WHITE}|\t{Fore.WHITE}- [{Fore.RED}3{Fore.WHITE}] : {Fore.RED}{labels['back']} \t\t\t\t      {Fore.WHITE}|")
        print(f"\t   {Fore.WHITE}---------------------------------------------------" )

        choice = input('\n' + PROMPT_PREFIX).strip()
        if choice == '1':
            theme.clear_console()
            conversation_mode()
        elif choice == '2':
            theme.clear_console()
            file_upload_mode()
        elif choice == '3':
            return
        else:
            print(theme.warn("\t[☢️ Choix invalide !]"))


if __name__ == '__main__':
    while True:
        selected_language = select_language()
        if not selected_language:
            break
        show_menu(selected_language)
