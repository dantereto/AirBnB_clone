#!/usr/bin/python3
"""Module to storage a file
"""
import json
from os.path import exists

class FileStorage:
    """ File Storage class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return objects
        """
        return self.__objects

    def new(self, obj):
        """Set objects
        """
        self.__objects[obj.__class__.__name__] = obj

    def save(self):
        """Serialization
        """
        with open(self.__file_path, 'w+', encoding='utf-8') as file_json:
            file_json.write(json.dumps(self.__objects))

    def reload(self):
        """Deserialization
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file_json:
                self.__objects = json.load(file_json.read())
