from pydantic import BaseModel
from typing import List, Optional
class Etudiant(BaseModel):
    id: int
    nom: str
    age: Optional[int] = None
    notes: List[float] = []
class Classe(BaseModel):
    id: int
    nom: str
    etudiants: List[Etudiant] = []