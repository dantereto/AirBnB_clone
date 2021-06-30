#!/usr/bin/python3

"""Module base model
"""


import models
import uuid
from datetime import datetime


class BaseModel:
    """ Class Base model
    """

    def __init__(self, *args, **kwargs):
        """ start variable """

        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
                else:
                    pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return a string format
        """

        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the current time"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dict """

        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
