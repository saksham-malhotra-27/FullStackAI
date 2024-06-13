from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "postgresql://neondb_owner:fh8RHsnWbO3p@ep-calm-dust-a5glzizl.us-east-2.aws.neon.tech/proj?sslmode=require"



engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()