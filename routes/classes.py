from fastapi import APIRouter, HTTPException
from modeles import Classe
from base_donnees import classe_db
from utilitaires import trouver_classe_par_id
router = APIRouter(prefix="/classes", tags=["Classes"])

@router.post("/")
def creer_classe(classe: Classe):
    if trouver_classe_par_id(classe.id):
        raise HTTPException(
            status_code=400,
            detail="La classe existe deja"
        )
    classe_db.append(classe)
    return classe

@router.get("/")
def afficher_classes():
    return classe_db

@router.get("/{classe_id}")
def afficher_classe(classe_id: int):
    classe = trouver_classe_par_id(classe_id)
    if not classe:
        raise HTTPException(
            status_code=404,
            detail="classe non trouvée"
        )
    return classe

@router.delete("/{classe_id}")
def supprimer_classe(classe_id: int):
    classe = trouver_classe_par_id(classe_id)
    if not classe:
        raise HTTPException(
            status_code=404,
            detail="classe non trouvée"
        )
    classe_db.remove(classe)
    return{"message": "classe suppimé"}