from fastapi import APIRouter, HTTPException
from modeles import Etudiant
from base_donnees import etudiants_db
from utilitaires import (
    trouver_etudiant_par_id,
    trouver_classe_par_id,
    etudiant_dans_classe
)

router = APIRouter(prefix="/etudiants", tags=["Etudiants"])

@router.post("/")
def creer_etudiant(etudiant: Etudiant):
    if trouver_etudiant_par_id(etudiant.id):
        raise HTTPException(
            status_code=400,
            detail="etudiant existe deja"
        )
    etudiants_db.append(etudiant)
    return etudiant

@router.get("/{etudiant_id}")
def afficher_etudiant(etudiant_id: int):
    etudiant = trouver_etudiant_par_id(etudiant_id)
    if not etudiant:
        raise HTTPException(
            status_code=404,
            detail="etudiant non trouve"
        )
    return etudiant

@router.post("/ajouter/{classe_id}/{etudiant_id}")
def ajouter_etudiant_a_classe(classe_id: int, etudiant_id: int):
    classe = trouver_classe_par_id(classe_id)
    if not classe:
        raise HTTPException(
            status_code=404,
            detail="classe non trouvée"
        )
    etudiant = trouver_etudiant_par_id(etudiant_id)
    if not etudiant:
        raise HTTPException(
            status_code=404,
            detail="etudiant non trouve"
        )
    if etudiant_dans_classe(etudiant_id, classe):
        raise HTTPException(
            status_code=400,
            detail="etudiant deja dans class"
        )
    classe.etudiants.append(etudiant)
    return {"message": "etudiant ajouté a la classe"}

@router.delete("/retirer/{classe_id}/{etudiant_id}")
def retirer_etudiant_de_classe(classe_id: int, etudiant_id: int):
    classe = trouver_classe_par_id(classe_id)
    if not classe:
        raise HTTPException(
            status_code=404,
            detail="classe non trouvée"
        )
    if not etudiant_dans_classe(etudiant_id, classe):
        raise HTTPException(
            status_code=404,
            detail="etudiant nest pas dans la classe"
        )
    classe.etudiants= [
        etudiant for etudiant in classe.etudiants if etudiant.id != etudiant_id
    ]
    return {"message": "etudiant retiré de la classe"}

@router.post("/{etudiant_id}/notes")
def ajouter_note(etudiant_id: int, note: float):
    etudiant = trouver_etudiant_par_id(etudiant_id)
    if not etudiant:
        raise HTTPException(
            status_code=404,
            detail="etudiant non trouve"
        )
    etudiant.notes.append(note)
    return {"message": "note ajoutée", "notes": etudiant.notes}

@router.delete("/{etudiant_id}/notes/{note}")
def supprimer_note(etudiant_id: int, note: float):
    etudiant = trouver_etudiant_par_id(etudiant_id)
    if not etudiant:
        raise HTTPException(
            status_code=404,
            detail="etudiant non trouve"
        )
    if note not in etudiant.notes:
        raise HTTPException(
            status_code=404,
            detail="note non trouvée"
        )
    etudiant.notes.remove(note)
    return {"message": "note supprimée", "notes": etudiant.notes}
