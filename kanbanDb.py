from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import time
 
Base = declarative_base()
 
class KanbanDb(Base):
    __tablename__ = 'kanban'
    # Define columns for the kanban person
    # Each column is a normal Python instance attribute.
    id = Column(Integer, primary_key = True)
    task_name = Column(String(255), nullable = False)
    task_status = Column(String(50), nullable = False)
    start_time = Column(DateTime, nullable =True)
    task_duration = Column(String(50), nullable = True)
 
engine = create_engine('sqlite:///kanban.db') # Create an engine that stores data in the local directory's
Base.metadata.create_all(engine) # Create table in the engine