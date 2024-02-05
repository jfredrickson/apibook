"""SQLAlchemy models definition - Chapter 2"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#define the Player class, a subclass of Base
class Player(Base):
    __tablename__ = "player"

    player_id = Column(Integer, primary_key=True, index=True)

    nfl_player_id = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)

    # Create a one-to-many relationship with the 'Performance' table.
    performances = relationship("Performance", back_populates="player")

#define the Performance class, a subclass of Base
class Performance(Base):
    __tablename__ = "performance"

    performance_id = Column(Integer, primary_key=True, index=True)

    # This statement defines a foreign key 'player_id' that references the 'Player' table's 'player_id'.
    player_id = Column(Integer, ForeignKey("player.player_id"))

    week_number = Column(String)
    fantasy_points = Column(Float)

    # Create a many-to-one relationship with the 'Player' table.
    player = relationship("Player", back_populates="performances")

class League(Base):
    __tablename__ = "league"

    league_id = Column(Integer, primary_key=True, index=True)
    league_name = Column(String, nullable=False)
    scoring_type = Column(String, nullable=False)

    # Create a one-to-many relationship with the 'Team' table.
    teams = relationship("Team", back_populates="league")

class Team(Base):
    __tablename__ = "team"

    team_id = Column(Integer, primary_key=True, index=True)
    league_id = Column(Integer, ForeignKey("league.league_id"), nullable=False)
    team_name = Column(String, nullable=False)

    # Create a many-to-one relationship with the 'League' table.
    league = relationship("League", back_populates="teams")

    # Create a many-to-many relationship with the 'player' table through the 'team_player' table.
    players = relationship("Player", secondary="team_player", back_populates="teams")

class TeamPlayer(Base):
    __tablename__ = "team_player"

    team_id = Column(Integer, ForeignKey("team.team_id"), primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("player.player_id"), primary_key=True, index=True)

    # Create a many-to-many relationship with the 'team' table through the 'team_player' table.
    Player.teams = relationship("Team", secondary="team_player", back_populates="players")
