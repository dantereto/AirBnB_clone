#!/usr/bin/python3
"""Module base model
"""
import uuid
from datetime import datetime

class BaseModel:
    """ Class Base model
    """
    def __init__(self):
        """ start variables
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return a string format
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the current time"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return a dict
        Returns:
        dict (dict)
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
