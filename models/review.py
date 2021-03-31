#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
=======
>>>>>>> 53b61010553308a71dec1c79fde6531f6ad148b7


class Review(BaseModel, Base):
    """ Review classto store review information """
<<<<<<< HEAD
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
=======
    __tablename__ = 'review'
    place_id = ""
    user_id = ""
    text = ""
>>>>>>> 53b61010553308a71dec1c79fde6531f6ad148b7
