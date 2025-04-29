from sqlalchemy import Column,Integer,String
from app.database.db import Base

class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(String)    