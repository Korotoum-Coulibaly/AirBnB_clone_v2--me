#!/usr/bin/pyhton3

from models.base_model import BaseModel

class User(BaseModel):
    '''Table User Model'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""


