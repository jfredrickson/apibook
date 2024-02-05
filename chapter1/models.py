"""SQLAlchemy models definition - Chapter 1"""
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

class Performance(Base):
    __tablename__ = "performance"

    performance_id = Column(Integer, primary_key=True, index=True)

    # This statement defines a foreign key 'player_id' that references the 'Player' table's 'player_id'.
    player_id = Column(Integer, ForeignKey("player.player_id"))

    week_number = Column(String)
    fantasy_points = Column(Float)

    # Create a many-to-one relationship with the 'Player' table.
    player = relationship("Player", back_populates="performances")
