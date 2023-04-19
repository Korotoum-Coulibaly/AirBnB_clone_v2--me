#!/usr/bin/python3
from datetime import datetime

current_time = datetime.now()
current_time =  current_time.isoformat()
print(current_time)
print(type(current_time))
'''converted date string in object'''
current_time = datetime.fromisoformat(current_time)
print(current_time)
print(type(current_time))
