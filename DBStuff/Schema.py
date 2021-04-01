from sqlalchemy.orm import declarative_base, relationship, registry
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey, DateTime

mapper_registry = registry()
Base = mapper_registry.generate_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    display_name = Column(String(30))

class Password(Base):
    __tablename__ = 'password'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'))
    password = Column(String(30))

class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

class Section(Base):
    __tablename__ = 'section'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    game = Column(Integer, ForeignKey('game.id'))

class Level(Base):
    __tablename__ = 'level'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    section = Column(Integer, ForeignKey('section.id'))

class TTTime(Base):
    __tablename__ = 'timetrials'
    id = Column(Integer, primary_key=True)
    level = Column(Integer, ForeignKey('level.id'))
    user = Column(Integer, ForeignKey('users.id'))
    time = Column(Float(20))
    lap1 = Column(Float(20))
    lap2 = Column(Float(20))
    lap3 = Column(Float(20))
    proof = Column(String(200))
    timestamp = Column(DateTime())
