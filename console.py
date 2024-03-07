#!/usr/bin/ env python3
from models.base_model import BaseModel
import cmd

class HBNBCommand(cmd.Cmd):
    """the class for the airbnb console"""

    prompt =  '(HBNB)'

    class_list = ['BaseModel',"FileStorage"]

    cmd.Cmd.class_list = class_list
    
    def do_EOF(self, line):
        """exits the console """
        return True

    def do_quit(self, line):
        """exits the console"""
        return True

    def do_create(self, line):
        """function to create an instance of the BaseModel"""
        line_arr = line.split(' ')
        if not line:
            print("** class name missing **")
        else:
            if line_arr[0] not in cmd.Cmd.class_list:
                print(f"** class doesn't exist **")
            else:
                obj = eval(line_arr[0])()
                print(obj.id)
                obj.save()

    def do_show(self, line):
        line_arr = line.split(" ")
        if not line:
            print("** class name missing **")
        else:
            if line_arr[0] not in cmd.Cmd.class_list:
                print(" ** class doesn't exist ** ")
            else:
                if len(line_arr) < 3:
                    print("** instance id missing **")

    def default(self, line):
        """in case a command does not exist it displays the no command <command name>"""
        print(f"no command {line}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
