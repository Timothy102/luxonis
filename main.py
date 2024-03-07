from datetime import datetime
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Database connection URL
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db/postgres"

# SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Define database model
Base = declarative_base()

class Property(Base):
    """PSQL Property Base Element

    Args:
        Base (sqlalchemy.ext.declarative): PSQL Property Base Element
    """
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    image_url = Column(String)
    href = Column(String)

Base.metadata.create_all(bind=engine)

# Function to insert property into database
def insert_property(db: Session, title: str, image_url: str, href: str):
    """Insert Property into PSQL

    Args:
        db (Session): SessionLocal object
        title (str): Property Title
        image_url (str): Property Image URL
        href (str): _description_
    """
    db_property = Property(title=title, image_url=image_url, href=href)
    db.add(db_property)
    db.commit()
    
@app.get("/")
def root(request: Request, db: Session = Depends(get_db)):
    start_time = datetime.now()  # Record the start time
    
    with open("cz/cz/spiders/output.json", 'r', encoding='utf-8') as file:
        property_items = json.load(file)
        
    for property_item in property_items:
        # Insert data into database
        insert_property(db, property_item["title"], property_item["href"], property_item["image_url"])
    
    end_time = datetime.now()  # Record the end time
    time_taken = end_time - start_time  # Calculate the time taken
    
    message = f"Scraped {len(property_items)} properties in {time_taken.total_seconds()} seconds"
    
    return templates.TemplateResponse("properties.html", {"request": request, "properties": property_items, "message": message})
