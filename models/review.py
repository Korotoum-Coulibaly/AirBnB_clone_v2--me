#!/usr/bin/python3

from basemodel import BaseModel

class Review(BaseModel):
    ''' Table review model'''
    user_id = ""
    place_id = ""
    text = ""
