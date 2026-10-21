from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#DATABASE_URL ="mysql+pymysql://root:root@localhost:3306/students"
DATABASE_URL = "postgresql+psycopg2://database_new_z4g9_user:z8qXSSVtXqnNHrrPV7r0SbOwtFGJZIFg@dpg-dbc7fk4s728c73e8trrg-a.oregon-postgres.render.com/database_new_z4g9"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()