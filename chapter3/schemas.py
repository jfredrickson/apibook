"""Pydantic schemas definition - Chapter 2"""
from pydantic import BaseModel
from typing import List

class Performance(BaseModel):
    player_id: int
    performance_id: int
    week_number: str
    fantasy_points: float

    class Config:
        from_attributes = True

class PlayerBase(BaseModel):
    player_id: int
    nfl_player_id: str
    first_name: str
    last_name: str

    class Config:
        from_attributes = True

class Player(PlayerBase):
    performances: list[Performance] = []

    class Config:
        from_attributes = True

class TeamBase(BaseModel):
    team_id: int
    league_id: int
    team_name: str

    class Config:
        from_attributes = True

class Team(TeamBase):
    players: List[PlayerBase] = []

    class Config:
        from_attributes = True

class League(BaseModel):
    league_id: int
    league_name: str
    scoring_type: str
    teams: List[TeamBase] = []

    class Config:
        from_attributes = True
