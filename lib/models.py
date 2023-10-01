from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    platform = Column(String)

    # Define a one-to-many relationship with Review
    reviews = relationship("Review", backref="game")

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    
    # Define a foreign key relationship to Game
    game_id = Column(Integer, ForeignKey('games.id'))
