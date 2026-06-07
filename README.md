# 🎭 LezookGPT

Un outil IA offensif inspiré de Hexsec GPT créé par Jason (LeszooksHackers).

![Python Version](https://shields.io)
![API Provider](https://shields.io)
![Purpose](https://shields.io)

<img width="1366" height="768" alt="Screenshot_LezookGPT" src="https://github.com/user-attachments/assets/809a6cad-0444-4194-9563-56ea5ea31678" />

LezookGPT est un framework d'intelligence artificielle offensive inspiré de **Hexsec GPT**. Il a été amélioré pour intégrer un système de gestion et d'accès direct aux fichiers locaux, supporte 3 langues, et fonctionne nativement avec OpenRouter.

L'avantage majeur de cette version est l'intégration d'une configuration simplifiée pour que l'utilisateur n'ait pas à se soucier de la configuration fastidieuse d'une clé API payante.

> ⚠️ **Avertissement Légal :** Cet outil est développé uniquement à des fins éducatives, de recherche en sécurité et de Red Teaming. L'exploitation de cet outil sur des systèmes sans accord écrit préalable est strictement illégale.

---

## ✨ Améliorations par rapport à Hexsec GPT

- **Accès aux Fichiers :** Capacité de lire, analyser et interagir avec les fichiers locaux pour auditer du code ou des rapports.
- **Multilingue :** Prise en charge native de 3 langues (Français, Anglais, Malagasy 🇲🇬) pour une flexibilité accrue lors des audits.
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

Pour utiliser l'outil, vous devez lui fournir votre clé API OpenRouter. Deux options s'offrent à vous :

### Option 1 : Via une variable d'environnement (Recommandé)
Exécutez simplement cette commande dans votre terminal avant de lancer le script :
```bash
export OPENROUTER_API_KEY="votre_cle_openrouter"
python main.py
```

### Option 2 : Modification permanente dans `config.py`
Si vous préférez inscrire la clé en dur, ouvrez le fichier `config.py` à la ligne 7 :
```bash
nano config.py
```
Modifiez la variable pour y insérer votre clé :
```python
API_KEY = os.getenv("OPENROUTER_API_KEY") or "votre_cle_openrouter_ici"
```
Sauvegardez (`Ctrl+O` puis `Entrée`) et quittez (`Ctrl+X`), puis lancez l’outil :
```bash
python main.py
```

---

## 📄 Licence

Ce projet est destiné à la recherche en cybersécurité. Veuillez vous référer aux lois en vigueur dans votre pays avant toute utilisation.
