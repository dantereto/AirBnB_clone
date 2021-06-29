#!/usr/bin/python3

"""create the class"""

from models.base_model import BaseModel


class User(BaseModel):

    """user"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
