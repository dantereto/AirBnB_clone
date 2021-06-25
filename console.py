#!/usr/bin/python3
"""Module to storage a file
"""
import cmd, sys

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def do_quit(self, arg):
        'Quit command to exit the program'
        exit()
    def do_EOF(self, arg):
        'EOF command to exit the program'
        exit()
if __name__ == '__main__':
    HBNBCommand().cmdloop()