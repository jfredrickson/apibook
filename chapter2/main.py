"""FastAPI file - Chapter 2"""
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import Session, engine

app = FastAPI()


# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "API health check successful"}

@app.get("/v0/players/", response_model=list[schemas.Player])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = crud.get_players(db, skip=skip, limit=limit)
    return players

@app.get("/v0/players/{player_id}", response_model=schemas.Player)
def read_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.get_player(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@app.get("/v0/performances/", response_model=list[schemas.Performance])
def read_performances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    performances = crud.get_performances(db, skip=skip, limit=limit)
    return performances

@app.get("/v0/leagues/", response_model=list[schemas.League])
def read_leagues(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leagues = crud.get_leagues(db, skip=skip, limit=limit)
    return leagues

@app.get("/v0/teams/", response_model=list[schemas.Team])
def read_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = crud.get_teams(db, skip=skip, limit=limit)
    return teams
