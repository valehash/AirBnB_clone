#!/usr/bin/ env python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd

class HBNBCommand(cmd.Cmd):
    """the class for the airbnb console"""

    prompt =  '(hbnb)'

    class_list = ['BaseModel', "FileStorage", "User", "State", "City", "Amenity", "Place", "Review"]

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
        """Shows all the attrributes of a class Useage: show <class_name> <id>"""
        line_arr = line.split(" ")
        if not line:
            print("** class name missing **")
        else:
            if line_arr[0] not in cmd.Cmd.class_list:
                print(" ** class doesn't exist ** ")
            else:
                if len(line_arr) < 2:
                    print("** instance id missing **")
                else:
                    load_id = line_arr[1]
                    all_obj = storage.all()
                    try:
                        obj = all_obj[f"{line_arr[0]}.{load_id}"]
                        print(obj)
                    except KeyError:
                        print("no instance found")

    def do_destroy(self, line):
        """destroys an instance of a class using the id Usage:destroy <class_name> <id>"""
        line_arr = line.split(" ")
        if not line:
            print("** class name missing **")
        else:
            if line_arr[0] not in cmd.Cmd.class_list:
                print(" ** class doesn't exist ** ")
            else:
                if len(line_arr) < 2:
                    print("** instance id missing **")
                else:
                    load_id = line_arr[1]
                    all_obj = storage.all()
                    try:
                        del all_obj[f"{line_arr[0]}.{load_id}"]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")

    def do_all(self, line):
        """Displays all attributes usagw :all  or all <class name>"""
        line_arr = line.split(" ")
        if line:
            if line_arr[0] not in cmd.Cmd.class_list:
                print(" ** class doesn't exist ** ")
            else:
                all_obj = storage.all()
                obj = [str(v) for k, v in all_obj.items() if line_arr[0] == k.split('.')[0]]
                print(obj)
        else:
            all_obj = storage.all()
            obj = [str(v) for v in all_obj.values()]
            print(obj)

    def default(self, line):
        """in case a command does not exist it displays the no command <command name>"""
        print(f"no command {line}")


    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". """
        line_arr = line.split(' ')
        if not line:
            print("** class name missing **")
            return

        class_name = line_arr[0]

        if class_name not in cmd.Cmd.class_list:
            print(" ** class doesn't exist ** ")
            return
        if len(line_arr) < 2:
            print("** instance id missing **")
            return

        instance_id = line_arr[1]
        try:
            obj = storage.all()[f"{class_name}.{instance_id}"]
        except KeyError:
            print(" ** instance not found ** ")
            return

        if len(line_arr) < 4:
            print("** attribute name or value missing **")
            return

        setattr(obj, line_arr[2], line_arr[3])

        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
