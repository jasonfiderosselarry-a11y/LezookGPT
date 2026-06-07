# LezookGPT
Un outils IA offensif inspiré de Hexsec GPT créér par Jason (LeszooksHackers)
# 🎭 LezookGPT

[![Python Version](https://shields.io)](https://python.org)
[![API Provider](https://shields.io)](https://openrouter.ai)
[![Purpose](https://shields.io)]()

LezookGPT est un framework d'intelligence artificielle offensive inspiré de **Hexsec GPT**. Il a été amélioré pour intégrer un système de gestion et d'accès direct aux fichiers locaux, supporte 3 langues, et fonctionne nativement avec OpenRouter.

L'avantage majeur de cette version est l'intégration d'une configuration simplifiée pour que l'utilisateur n'ait pas à se soucier de la configuration fastidieuse d'une clé API payante.

> ⚠️ **Avertissement Légal :** Cet outil est développé uniquement à des fins éducatives, de recherche en sécurité et de Red Teaming. L'exploitation de cet outil sur des systèmes sans accord écrit préalable est strictement illégale.

---

## ✨ Améliorations par rapport à Hexsec GPT

- **Accès aux Fichiers :** Capacité de lire, analyser et interagir avec les fichiers locaux pour auditer du code ou des rapports.
- **Multilingue :** Prise en charge native de 3 langues pour une flexibilité accrue lors des audits.
- **Clé API Intégrée :** Pré-configuré pour utiliser OpenRouter sans friction financière immédiate pour l'utilisateur.

---

## 📁 Structure du Projet

Le projet est ultra-léger et se compose de seulement 4 fichiers principaux :

- `main.py` : Point d'entrée de l'application et interface utilisateur.
- `config.py` : Gestion des configurations globales et de la clé API OpenRouter.
- `ia_client.py` : Gestion des requêtes et de la communication avec l'API OpenRouter.
- `theme.py` : Gestion de l'affichage visuel, des couleurs et du style de la console.

---

## 🛠️ Installation et Prérequis

### 1. Cloner le projet

```bash
git clone https://github.com/jasonfiderosselarry-a11y/LezookGPT.git
cd LezookGPT
```

### 2. Installer les dépendances

Le script utilise des bibliothèques standards et légères. Installez-les directement via `pip` :

```bash
pip install -r requirements.txt
```

---

## 💻 Utilisation

Avant de lancer le script, vous devez exporter la clé API OpenRouter dans votre terminal.

### Étape 1 : Activer la clé API
Il faut d'abord changer la ligne 7 dans config.py:
```bash
nano config.py
line 7 : API_KEY = os.getenv("votre_api_key_sur_openrouter") or "votre_api_key_sur_openrouter"
ctrl + s
ctrl + x
```

Exécutez la commande suivante dans votre terminal :

```bash
export OPENROUTER_API_KEY="api_key openrouter"
```

*(Note : La clé est également gérée en interne dans `config.py` pour assurer la gratuité et la simplicité d'accès).*

### Étape 2 : Lancer LezookGPT

```bash
python main.py
```

Une fois lancé, choisissez votre langue, chargez vos fichiers si nécessaire, et commencez votre audit offensif assisté par l'IA.

---

## 📄 Licence

Ce projet est destiné à la recherche en cybersécurité. Veuillez vous référer aux lois en vigueur dans votre pays avant toute utilisation.
