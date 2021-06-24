#!/usr/bin/python3
"""Module base model
"""
import uuid
from datetime import datetime
from models.__init__ import storage


data = '%Y-%m-%dT%H:%M:%S.%f'
class BaseModel:
    """ Class Base model
    """
    def __init__(self, *args, **kwargs):
        """ start variable """
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, data)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Return a string format
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the current time"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Return a dict
        Returns:
        dict (dict)
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
