import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('film.id'))
    film = relationship(Film)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)

class People(Base):
    __tablename__ = 'People'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20) != null)
    height = Column(Integer, not null)
    mass = Column(Integer, not null)
    hair_color = Column(String(10) != null)
    skin_color = Column(String(10) != null)
    eye_color = Column(String(10) != null)
    birth_year = Coloumn(String(8), not null)
    gender = Column(String(8))
    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    homeworld = relationship(Planet)

    
    
class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20) != null)
    population = Column(Integer, not null)
    gravity = Column(String(20) != null)
    climate =Column(String(20) != null)
    terrain = Column(String(20) != null)
    surface_water = Column(Integer, not null)
    diameter = Column(Integer, not null)
    rotation_period = Column(Integer, not null)
    orbital_period = Column(Integer, not null)


class Starship(Base):
    __tablename__ = 'Starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(50) != null)
    model = Column(String(50) != null)
    starship_class = Column(String(50) != null)
    manufacturer = Column(String(50) != null)
    cost_in_credits = Column(Integer, not null)
    length = Column(Integer, not null)
    crew = Column(Integer, not null)
    passengers = Column(Integer, not null)
    hyperdrive_rating = Column(Integer, not null)
    consumables = Column(Integer, not null)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
