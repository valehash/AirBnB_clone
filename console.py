#!/usr/bin/ env python3
import cmd

class HBNBCommand(cmd.Cmd):
    """the class for the airbnb console"""

    prompt =  '(hbnb)'
    
    def do_EOF(self, line):
        """exits the console """
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
