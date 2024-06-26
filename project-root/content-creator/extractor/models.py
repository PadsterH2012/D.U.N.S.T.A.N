from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sex = Column(String, index=True)
    age = Column(String, index=True)
    traits = Column(String, index=True)
    behaviors = Column(String, index=True)
    background = Column(String, index=True)
    book_title = Column(String, index=True)
    author = Column(String, index=True)
    dialogue_examples = Column(String, index=True)
    genre = Column(String, index=True)

class Setting(Base):
    __tablename__ = "setting"  # Ensure the table name matches the database

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, index=True, unique=True)
    value = Column(String)

# Database URL for PostgreSQL
DATABASE_URL = "postgresql://user:password@db:5432/gamedb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
