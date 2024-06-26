from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sex = Column(String, index=True)
    age = Column(String, index=True)
    traits = Column(Text)
    behaviors = Column(Text)
    background = Column(Text)
    book_title = Column(String, index=True)
    author = Column(String, index=True)
    dialogue_examples = Column(Text)
    genre = Column(String, index=True)

    def update_from_dict(self, details_dict):
        for key, value in details_dict.items():
            setattr(self, key, value)

class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    description = Column(Text)
    objectives = Column(Text)

    def update_from_dict(self, details_dict):
        for key, value in details_dict.items():
            setattr(self, key, value)

class Setting(Base):
    __tablename__ = "setting"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, index=True, unique=True)
    value = Column(Text)

# Database URL for PostgreSQL
DATABASE_URL = "postgresql://user:password@db:5432/gamedb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
