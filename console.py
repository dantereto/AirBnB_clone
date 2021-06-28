#!/usr/bin/python3
"""Module to storage a file
"""

from models.user import User
import cmd, sys
from shlex import split
from models.base_model import BaseModel
from models import storage


objects = {'BaseModel': BaseModel, 'User': User}

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def do_quit(self, arg):
        'Quit command to exit the program'
        exit()
    def do_EOF(self, arg):
        'EOF command to exit the program'
        exit()
    def emptyline(self):
         pass
    def do_create(self, arg):
        'create a json file'
        arg = split(arg)
        if arg == []:
            print ('** class name missing **')
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        else:
            storage.reload()
            if arg[0] == 'BaseModel':
                my_model = BaseModel()
            else:
                my_model = User()
            storage.new(my_model)
            my_model.save()
            print(my_model.id)
    def do_show(self, arg):
        arg = split(arg)
        if arg == []:
            print ('** class name missing **')
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
        arg = split(arg)
        if arg == []:
            print ('** class name missing **')
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
        arg = split(arg)
        if arg == []:
            lista = []
            for  key, value in storage.all().items():
                lista.append(value.__str__())
            print(lista)
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        else:
            lista = []
            for  key, value in storage.all().items():
                if arg[0] == value.__class__.__name__:
                    lista.append(value.__str__())
            print(lista)

    def do_update(self, arg):
        arg = split(arg)
        if arg == []:
            print ('** class name missing **')
        elif arg[0] not in objects.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print ('** instance id missing **')
        elif len(arg) == 2:
            print ('** attribute name missing **')
        elif len(arg) == 3:
            print ('** value missing **')
        else:
            for  key, value in storage.all().items():
                setattr(value, arg[2], arg[3])
if __name__ == '__main__':
    HBNBCommand().cmdloop()
