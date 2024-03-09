#!/usr/bin/env python3
from models.base_model import BaseModel

class Place(BaseModel):
    """The place class will hold the information about a particular place"""
    user_id =' '
    city_id = ''
    name = ' '
    description = ''
    number_rooms = 0
    number_basthrooms = 0
    max_guest = 0
    price_by_night = 0
    lastitude = 0
    longitude = 0
    amenity_ids = 0
