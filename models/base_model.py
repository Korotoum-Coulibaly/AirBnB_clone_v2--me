#!/usr/bin/python3

class BaseModel():
    '''Contain all methods basics'''
    '''variable self is call to save information in FileStorage'''
    
    def save(self):
        id = ""
        update_at = ""
        created_at = ""

        '''FileStorage instanciation'''
        storage = FileStorage()
        '''save data to filestorage'''
        storage.save()

