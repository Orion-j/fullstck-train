import sys
from sqlalchemy import
Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import
declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy.orm import create_engine

class Restaurant(Base):
    __tablename__ = 'restaurants'


class Menu_Item(Base):
    __tablename__ = 'menu_item'

Base = declarative_base()
## Insert at the end of file ###

engine = create_engine( 
    'sqlite:///restaurantmenu.db'
)

Base.metadata.create_all(engine)