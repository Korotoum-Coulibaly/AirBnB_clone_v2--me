#!/usr/bin/python3
""" Tests for the City class"""

import unittest
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    '''this is all unit test for table city implementation'''
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
        '''Tests instanciation of city class'''

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_attributes(self):
        '''Tests the attributes of City class'''
        attributes = storage.attributes()["City"]
        o = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == '__main__':
    unittest.main()
