# Projet Trustpilot
Topic modeling et classification de commentaires issus du site [TrustPilot](https://www.trustpilot.com/)

## Objectif du projet
Ce projet a pour objectif d'ajouter une nouvelle fonctionnalité au site Trustpilot : la possibilité de trier les commentaires d'une entreprise par thème.

Pour cela, le projet s'effectue en plusieurs étapes :
- Regrouper les commentaires en thèmes grâce au topic modeling.
- Nommer les groupes obtenus à l'aide de techniques statistiques et linguistiques.
- (Optionnel) A l'aide des données labellisées obtenues, créer un modèle de classification supervisée capable de prédire la catégorie d'un nouvel avis.

## Structure du dépôt

- `data` - données brutes, après traitement, et embeddings obtenus
- `models` - modèles d'embeddings et modèle de détection de langues
- `notebooks` - Notebooks Jupyter du projet
- `src` - scripts python
- `outputs` - résultats obtenus

## Installation et environnement

### Cloner le dépôt

HTTPS : `git clone https://github.com/laurinecharbonnier/trustpilot.git`

SSH : `git clone git@github.com:laurinecharbonnier/trustpilot.git`

### Environnement virtuel

Création : `python3 -m venv venv`

Activation : `source venv/bin/activate`

Installer les dépendances nécessaires : `pip install -r requirements.txt`

Désactivation de l'environnement virtuel : `deactivate`

Création du kernel pour Jupyter (en étant dans le venv) : `python -m ipykernel install --user --name=trustpilot_venv --display-name "TrustPilot Venv"`

Il faut ensuite le sélectionner dans Jupyter

### Téléchargement des modèles

Lancer le script python : `python3 src/download_models.py`

Modèles qui seront téléchargés :
- `frWac_no_postag_no_phrase_500_skip_cut100.bin` : [Word2Vec](https://fauconnier.github.io/#data)
- `frWac_postag_no_phrase_700_skip_cut50.bin` : [Word2Vec](https://fauconnier.github.io/#data)
- `frWac_postag_no_phrase_1000_skip_cut100.bin` : [Word2Vec](https://fauconnier.github.io/#data)
- `cc.fr.300` : [Fasttext français binaire](https://fasttext.cc/docs/en/crawl-vectors.html)
- `fasttext_fr.kv` et `fasttext_fr.kv.vectors.npy` : [Fasttext français avec uniquement les vecteurs de mots](https://fasttext.cc/docs/en/crawl-vectors.html)
- `lid.176.ftz` : [Modèle Fasttext de détection de langues](https://fasttext.cc/docs/en/language-identification.html)

## Utilisation

Ouvrir les Notebooks dans Jupyter-Lab

Lancer dans l’ordre :
- `01_exploration_de_donnees.ipynb`
- `02_preprocessing.ipynb`
- `03_modelisation.ipynb`

Les résultats serons enregistrés dans le dossier `outputs`

## Equipe du projet

- Julie BOUTELET
- Laurine CHARBONNIER
- Quentin GEORGE
- Kinjal KAPADIA