"""FastAPI file - Chapter 2"""
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import Session, engine

api_description = """
This API provides read-only access to info from the Sports World Central (SWC)
Fantasy Football API. 🏈.

The endpoints are grouped into the following categories:

## Player
You can get a list of an NFL players, or search for an individual player by
player_id.

## Scoring
You can get a list of NFL player performances, including the fantasy points
they scored using SWC league scoring.

## Membership
Get information about all the SWC fantasy football leagues and the teams in
them.
"""

app = FastAPI(
    description=api_description,
    title="Sports World Central (SWC) Fantasy Football API",
    version="0.1"
)


# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/",
         summary="Health check",
         description="Check API health",
         response_description="API status",
         operation_id="get_root",
         tags=["general"])
async def root():
    return {"message": "API health check successful"}

@app.get("/v0/players/",
         response_model=list[schemas.Player],
         summary="Get all players",
         description="Get all NFL players",
         response_description="All NFL players",
         operation_id="get_players",
         tags=["player"])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = crud.get_players(db, skip=skip, limit=limit)
    return players

@app.get("/v0/players/{player_id}",
         response_model=schemas.Player,
         summary="Get players by Player ID",
         description="Get an individual NFL player by the SWC Player ID",
         response_description="One NFL player",
         operation_id="get_players_by_player_id",
         tags=["player"])
def read_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.get_player(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@app.get("/v0/performances/",
         response_model=list[schemas.Performance],
         summary="Get performances",
         description="Get all performances",
         response_description="All performances",
         operation_id="get_performances",
         tags=["scoring"])
def read_performances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    performances = crud.get_performances(db, skip=skip, limit=limit)
    return performances

@app.get("/v0/leagues/",
         response_model=list[schemas.League],
         summary="Get leagues",
         description="Get all leagues",
         response_description="All leagues",
         operation_id="get_leagues",
         tags=["membership"])
def read_leagues(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leagues = crud.get_leagues(db, skip=skip, limit=limit)
    return leagues

@app.get("/v0/teams/",
         response_model=list[schemas.Team],
         summary="Get teams",
         description="Get all teams",
         response_description="All teams",
         operation_id="get_teams",
         tags=["membership"])
def read_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = crud.get_teams(db, skip=skip, limit=limit)
    return teams
