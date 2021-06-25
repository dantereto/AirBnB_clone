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
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialization
        """
        save_o = {}
        for key, value in self.__objects.items():
            save_o[key] = value.to_dict()
        with open(self.__file_path, 'w+', encoding='utf-8') as file_json:
            file_json.write(json.dumps(save_o))

    def reload(self):
        """Deserialization
        """
        try:
            if exists(self.__file_path):
                with open(self.__file_path, 'r', encoding='utf-8') as file_json:
                    self.__objects = json.load(file_json.read())
        except:
            pass