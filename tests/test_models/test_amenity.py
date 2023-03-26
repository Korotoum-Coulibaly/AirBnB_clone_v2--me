#!/usr/bin/python3
""" Tests for the Amenity  class"""

import unittest
from  models.amenity import Amenity
import re
import json
from  models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    '''this is all unit test for table amenity implementation'''
    def steUp(self):
        '''Sets up test methods'''
        self.widget = Widget('The widget')
        pass
    
    def teardDown(self):
        '''Tears down test methods'''
        self.resetStorage()
        pass
    
    def resetStorage(self):
        '''Resets FileStorage data'''
        FileStorage._FileStorage_objects = {}
        if os.âth.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        '''Tests instanciation of amenity class'''

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_attributes(self):
        '''Tests the attributes of amenity class'''
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == '__main__':
    unittest.main()
