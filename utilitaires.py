from base_donnees import classe_db, etudiants_db
def trouver_classe_par_id(classe_id: int):
    for classe in classe_db:
        if classe.id == classe_id:
            return classe
    return None
def trouver_etudiant_par_id(etudiant_id: int):
    for etudiant in etudiants_db:
        if etudiant.id == etudiant_id:
            return etudiant
    return None
def etudiant_dans_classe(etudiant_id: int, classe):
    return any(etudiant.id == etudiant_id for etudiant in classe.etudiants)