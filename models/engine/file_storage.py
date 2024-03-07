#!/usr/bin env python3
import json
import models
from models.base_model import BaseModel
class FileStorage:
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
        new_dict = {}
        for objects, val in self.__objects.items():
            new_dict[objects] = val.to_dict()
        with open(self.__file_path, 'w') as f: 
                json.dump(new_dict, f)

    def reload(self):
        with open(self.__file_path, 'r') as f:
            obs = json.load(f)
            for key, value in obs.items():
                vals = eval(f"{value['__class__']}(**value)")
                self.__objects[key] = vals
