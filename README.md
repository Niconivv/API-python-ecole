# Projet Python API - Gestion d'École
API en FastAPI qui permet de gérer les classes et les étudiants d'une école.
Ce projet permet de :
-	Créer, afficher et supprimer des classes
-	Créer, afficher et supprimer des étudiants
-	Ajouter ou retirer des étudiants d'une classe
-	Ajouter ou retirer des notes a un étudiant
Le projet est fait en python et testé sur postman et utilisé uvicorn  a l’adresse local : http://127.0.0.1:8000
Les routes principales sont /étudiants et /classes
Pour les IDs c’est /classes/1 /classes/2 etc. Voire le guide en dessous.
Classes
Type	URL	                                         Description
POST    /classes	                                 Créer une classe
GET	    /classes	                                 Lister toutes les classes
GET	    /classes/{classe_id}	                     Afficher une classe
DELETE	/classes/{classe_id}	                     Supprimer une classe
Étudiants
Type	URL	                                          Description
POST	/etudiants	                                  Créer un étudiant
GET	    /etudiants/{etudiant_id}	                  Afficher un étudiant
POST	/etudiants/ajouter/{classe_id}/{etudiant_id}  Ajouter un étudiant à une classe
DELETE	/etudiants/retirer/{classe_id}/{etudiant_id}  Retirer un étudiant d’une classe
POST	/etudiants/{etudiant_id}/notes?note=(float)	  Rajouter une note
DELETE	/etudiants/{etudiant_id}/notes/{note}	      Effacer une note(doit inclure la décimale même si elle est = a 0)

Exemple dans le body JSON
Créer une classe
{
  "id": 1,
  "nom": "B1",
  "etudiants": []
}
Créer un étudiant
{
  "id": 1,
  "nom": "Dany",
  "age": 18,
  "notes": []
}
