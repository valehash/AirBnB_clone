#!/usr/bin env python3
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Filestorage class, basically handles serialization and deserailization"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Function to return all the objects in the dictionary"""
        return self.__objects
    def new(self, obj):
        """sets in objects with keys"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """save function to save the dictionary to a json"""
        new_dict = {}
        for objects, val in self.__objects.items():
            new_dict[objects] = val.to_dict()
        with open(self.__file_path, 'w') as f: 
                json.dump(new_dict, f)

    def reload(self):
        """reads the file json and converts it into objects"""
        try:
            with open(self.__file_path, 'r') as f:
                obs = json.load(f)
                for key, value in obs.items():
                    vals = eval(f"{value['__class__']}(**value)")
                    self.__objects[key] = vals
        except:
            pass
