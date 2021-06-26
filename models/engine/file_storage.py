#!/usr/bin/python3
"""Module to storage a file
"""
import json


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

        with open(self.__file_path, 'w', encoding='utf-8') as file_json:
            json.dump(save_o, file_json)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path) as file_json:
                data = json.load(file_json)

            if not data:
                return
            for key in data.keys():
                if data[key]['__class__'] == 'BaseModel':
                    FileStorage.__objects[key] = BaseModel(**data[key])
        except:
            pass
