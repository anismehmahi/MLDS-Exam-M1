# Projet de Classification du Diabète

Ce projet vise à créer un modèle de classification du diabète en utilisant des techniques d'apprentissage automatique(SVM, XGBoost , Random Forest). 


## Contenu


- **Dossier data** : contient deux fichiers CSV, l'un pour les données d'entraînement et l'autre pour les données de test.
- **Dossier experiments** : contient les notebooks sur lesquels nous avons étudié et analysé les données, puis entraîné nos modèles.
- **Dossier models* : contient les modèles entraînés (sous format Pickle).
- **main.py** : un script Python qui génère les résultats de l'application des trois modèles sur les données de test.
- **requirements.txt**  : Fichier spécifiant les packages nécessaires à l'exécution.
 
## Instructions

### Pour executer le projet en local :
1. Clonez ce repo avec la commande :  `git clone https://github.com/anismehmahi/MLDS-Exam-M1.git`
2. Assurez-vous de télécharger les packages spécifiés dans **requirements.txt** avec les versions indiquées.
3. Assurez-vous que vous êtes sur le bon chemin du fichier **main.py**

4. Executer **main.py** avec la commande : `python main.py`

### pour executer le projet avec l'image Docker

1. Faire un pull de l'image docker du projet (depuis docker hub) :  `docker pull anismahmahi/diabetes-amsd`

#### Pour ne pas  partager le volume : 

- executer le container avec la commande : `docker run --name diabetes-container diabetes-amsd`
#### Pour utiliser le volume partagé 
- Clonez ce repo avec la commande :  `git clone https://github.com/anismehmahi/MLDS-Exam-M1.git`
- Excuter le container avec la commande : `docker run --name (nom du container) -v (chemin absolue dans votre machine vers le repertoire models du repo):/app/models/ -p 5000:5000 diabetes-amsd`
- Pour tester un nouveau modèle (dans le cas de la mise à jour des modèles), veuillez remplacer l'un des trois modèles dans le dossier local (models) par votre nouveau modèle (assurez-vous d'utiliser le même nom de fichier Pickle).
![Fonctionnement du Volume Docker](https://github.com/anismehmahi/MLDS-Exam-M1/blob/main/volume-svg.drawio.png)


## Conclusion et remarques
Dans notre experimentation on a constaté que:
   - les principales variables caractéristiques du diabète sont : Hypertension artérielle, hypercholestérolémie, BMI, AVC, santé générale, santé mentale, santé physique, âge, niveau d'instruction et revenu.
   - Les variables caractéristiques qui augmentent le risque de diabète sont : Tabagisme et forte consommation d'alcool, accident vasculaire cérébral et maladie ou attaque cardiaque, pression artérielle élevée et taux de cholestérol élevé.
   - En raison du déséquilibre des données, le score de précision de base était trompeur, j'ai donc utilisé les bonnes mesures d'évaluation telles que la précision/spécificité, le rappel/sensibilité, le score F1 et l'AUC.
   - Classement des modéle selons les resultats obtenues:
     
| Modèle         | Précision (Accuracy) | F1-Macro | F1-Micro |
| -------------- | -------------------- | -------- | -------- |
| Xgboost        | 0.97                 | 0.95     | 0.97     |
| Random Forest  | 0.92                 | 0.75     | 0.92     |
| SVM            | 0.61                 | 0.42     | 0.61     |




