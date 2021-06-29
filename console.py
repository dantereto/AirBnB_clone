#!/usr/bin/python3
"""Module to storage a file"""

from models.user import User
import cmd
import sys
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review


objects = {'User': User, 'BaseModel': BaseModel, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class HBNBCommand(cmd.Cmd):
    """ console """

    prompt = '(hbnb) '

    def default(self, arg):
        """Function default"""
        count = 0
        partition = arg.split('.')
        if len(partition) == 2:
            if partition[1] == 'count()':
                for key, value in storage.all().items():
                    if value.__class__.__name__ == partition[0]:
                        count += 1
                print(count)
        else:
            print('*** Unknown syntax: {}'.format(arg))


    def do_quit(self, arg):
        """quit the program"""

        return True

    def do_EOF(self, arg):
        """Quit the program"""

        print('')
        return True

    def emptyline(self):
        """pass when found a empty line"""

        pass

    def do_create(self, arg):
        """create a file"""

        arg = split(arg)
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

        arg = split(arg)
        if arg == []:
            print('** class name missing **')
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print('** instance id missing **')
        else:
            storage.reload()
            for key, value in storage.all().items():
                if value.id == arg[1] and value.__class__.__name__ == arg[0]:
                    print(str(value))
                    return
            print('** no instance found **')

    def do_destroy(self, arg):
        """destroy the file"""

        arg = split(arg)
        if arg == []:
            print('** class name missing **')
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print('** instance id missing **')
        else:
            storage.reload()
            for key, value in storage.all().items():
                if value.id == arg[1] and value.__class__.__name__ == arg[0]:
                    storage.all().pop(key)
                    return
            print('** no instance found **')

    def do_all(self, arg):
        """show all the files"""

        arg = split(arg)
        if arg == []:
            storage.reload()
            lista = []
            for key, value in storage.all().items():
                lista.append(value.__str__())
            print(lista)
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        else:
            storage.reload()
            lista = []
            for key, value in storage.all().items():
                if arg[0] == value.__class__.__name__:
                    lista.append(value.__str__())
            print(lista)

    def do_update(self, arg):
        """update a new element to the file"""

        arg = split(arg)
        if arg == []:
            print('** class name missing **')
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print('** instance id missing **')
        else:
            storage.reload()
            for key, value in storage.all().items():
                if value.id == arg[1] and value.__class__.__name__ == arg[0]:
                    if len(arg) == 2:
                        print('** attribute name missing **')
                        return
                    elif len(arg) == 3:
                        print('** value missing **')
                        return
                    else:
                        setattr(storage.all()[key], arg[2], arg[3])
                        storage.save()
                        return
            print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
