from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "YOUR_POSTGRESQL_DB_URL"



engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()