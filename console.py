#!/usr/bin/python3
"""Module to storage a file
"""


import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


objects = {'User': User, 'BaseModel': BaseModel, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class HBNBCommand(cmd.Cmd):
    """funcion principal prueba"""
    prompt = '(hbnb) '

    def emptyline(self):
        """pass when found a empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """create a json file"""
        arg = shlex.split(arg)
        if arg == []:
            print('** class name missing **')
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        else:
            storage.reload()
            my_model = objects[arg[0]]()
            storage.new(my_model)
            my_model.save()
            print(my_model.id)

    def do_show(self, arg):
        """show the file"""
        arg = shlex.split(arg)
        if arg == []:
            print('** class name missing **')
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print('** instance id missing **')
        else:
            for key, value in storage.all().items():
                if value.id == arg[1] and value.__class__.__name__ == arg[0]:
                    print(str(value))
                    return
            print('** no instance found **')

    def do_destroy(self, arg):
        """destroy the file"""
        arg = shlex.split(arg)
        if arg == []:
            print('** class name missing **')
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print('** instance id missing **')
        else:
            for key, value in storage.all().items():
                if value.id == arg[1] and value.__class__.__name__ == arg[0]:
                    storage.all().pop(key)
                    return
            print('** no instance found **')

    def do_all(self, arg):
        """show all the files"""
        arg = shlex.split(arg)
        if arg == []:
            lista = []
            for key, value in storage.all().items():
                lista.append(value.__str__())
            print(lista)
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        else:
            lista = []
            for key, value in storage.all().items():
                if arg[0] == value.__class__.__name__:
                    lista.append(value.__str__())
            print(lista)

    def do_update(self, arg):
        """update a new element to the file"""
        arg = shlex.split(arg)
        if arg == []:
            print('** class name missing **')
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print('** instance id missing **')
        elif len(arg) == 2:
            print('** attribute name missing **')
        elif len(arg) == 3:
            print('** value missing **')
        else:
            for key, value in storage.all().items():
                setattr(value, arg[2], arg[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
