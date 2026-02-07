# Analyse de consommation énergétique par data science

## Contexte
Projet réalisé dans le cadre du module *EI – Analyse de consommation avec data science* (ST4).  
L’objectif est d’exploiter des données issues de capteurs énergétiques afin d’analyser, nettoyer et modéliser des séries temporelles de consommation.

Projet réalisé en groupe.

## Problématique
Comment exploiter des données hétérogènes issues de capteurs pour analyser des profils de consommation énergétique et en extraire des informations exploitables, malgré les données manquantes et les différences de granularité temporelle ?

## Données
Les données utilisées proviennent de plusieurs fichiers de capteurs (stations), contenant :
- des mesures de consommation électrique,
- des timestamps à différentes fréquences,
- des valeurs manquantes ou aberrantes.

Un travail préalable de **fusion, alignement temporel et interpolation** est nécessaire avant toute analyse.

## Approche
Le projet est structuré autour des étapes suivantes :

1. **Importation et fusion des données**
   - Chargement de plusieurs sources de données
   - Alignement temporel des séries
   - Interpolation des valeurs manquantes

2. **Nettoyage et préparation**
   - Détection et traitement des incohérences
   - Normalisation des formats
   - Sélection des variables pertinentes

3. **Analyse exploratoire**
   - Visualisation des profils de consommation
   - Étude des variations temporelles
   - Comparaison entre stations

4. **Modélisation**
   - Mise en œuvre de méthodes statistiques et de data science
   - Analyse des tendances et comportements de consommation

## Résultats
L’analyse permet de :
- mettre en évidence des profils de consommation distincts,
- comprendre l’impact du traitement des données manquantes,
- illustrer l’importance de la préparation des données dans un pipeline data science.

Les visualisations et analyses sont regroupées dans le notebook principal.

## Limites
- Qualité et granularité des données dépendantes des capteurs
- Approche exploratoire sans déploiement opérationnel
- Modèles limités par la taille et la structure des données disponibles

## Perspectives
- Utilisation de modèles temporels plus avancés
- Automatisation du pipeline de traitement
- Extension à d’autres types de données énergétiques

## Organisation du repository
.
├── Livrable.ipynb        # Notebook principal du projet
├── README.md             # Description et contexte du projet
├── requirements.txt      # Dépendances Python
├── .gitignore            # Fichiers à ignorer par Git
└── data/
    ├── fichier1.csv      # Données utilisées dans l’analyse
    ├── fichier2.csv
    └── README.md         # Description des données

