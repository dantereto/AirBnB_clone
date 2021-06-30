#!/usr/bin/python3
"""Module to storage a file
"""
import json
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review


objects = {'User': User, 'Place': Place, 'State': State,
           'City': City, 'Amenity': Amenity, 'Review': Review}


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

        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialization the objects
        """

        save_o = {}
        for key, value in self.__objects.items():
            save_o[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file_json:
            json.dump(save_o, file_json)

    def reload(self):
        """reload the objects"""

        from models.base_model import BaseModel
        objects['BaseModel'] = BaseModel
        try:
            with open(self.__file_path) as file_json:
                data = json.load(file_json)

            if not data:
                return
            for key in data.keys():
                if data[key]['__class__'] in objects.keys():
                    FileStorage.__objects[key] = objects[data[
                        key]['__class__']](**data[key])
        except Exception:
            pass
