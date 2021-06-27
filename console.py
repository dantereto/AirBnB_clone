#!/usr/bin/python3
"""Module to storage a file
"""
import cmd, sys
from shlex import split
from models.base_model import BaseModel
from models import storage
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
        if arg[0] == None:
            print ('** class name missing **')
        elif arg[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            my_model = BaseModel() 
            storage.new(my_model)
            my_model.save()
            print(my_model.id)
    def do_show(self, arg):
        arg = split(arg)
        if arg[0] == None:
            print ('** class name missing **')
        elif arg[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print('** instance id missing **')
        else:
            for key, value in storage.all().items():
                 if value.id == arg[1]:
                    print(str(value))
                    return
            print('** no instance found **')
    def do_destroy(self, arg):
        arg = split(arg)
        if arg[0] == None:
            print ('** class name missing **')
        elif arg[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print('** instance id missing **')
        else:
            for key, value in storage.all().items():
                if value.id == arg[1]:
                    storage.all().pop(key)
                    return
            print('** no instance found **')
    def do_all(self, arg):
        arg = split(arg)
        if arg[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(arg) == 0:
            for  key, value in storage.all().items():
                print(value)
        else:
            lista = []
            for  key, value in storage.all().items():
                if arg[0] == value.__class__.__name__:
                    lista.append(value)
            print(lista)
if __name__ == '__main__':
    HBNBCommand().cmdloop()