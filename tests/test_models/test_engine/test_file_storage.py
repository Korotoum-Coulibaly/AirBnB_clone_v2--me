#!/usr/bin/python3
""" Tests for the City class"""

import unittest
import datetime import datetime
import time import sleep
import json
import models.engine.file_storage import FileStorage


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
