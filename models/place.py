#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    '''Table place models'''
    user_id = ""
    name = ""
    city_id = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
