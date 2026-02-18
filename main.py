from fastapi import FastAPI
from routes import classes, etudiants
app = FastAPI(title="projet python API Nicolas Julie Adel")
app.include_router(classes.router)
app.include_router(etudiants.router)