#!/usr/bin/pyhton3

from basemodel import BaseModel

class user(BaseModel):
    '''Table User Model'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""


