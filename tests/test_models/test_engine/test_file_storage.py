#!/usr/bin/python3
""" Tests for the City class"""

import unittest
from datetime import datetime
from time import sleep
import json
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    '''this is all unit test FileStorage'''
    def test_instances(self):
        '''instantiation'''
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)
    
    def test_docs(self):
        '''Test documentation'''
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

if __name__ == '__main__':
    unittest.main()
