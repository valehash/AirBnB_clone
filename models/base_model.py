#!/usr/bin/python3
"""The python base class for the Airbnb project """


from datetime import datetime
import uuid
import models as mp


class BaseModel:
    """The base Model class"""

    def __init__(self, *args, **kwargs):
        """Init method"""
        fmt_str = "%Y-%m-%dT%H:%M:%S.%f"
        if (kwargs):
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, fmt_str)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            mp.storage.new(self)

    def save(self):
        """method to update the value of update_at to current time"""
        self.updated_at = datetime.now()
        mp.storage.save()

    def to_dict(self):
        """method to return a dictionary containing all keys/values of dict"""
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = object_dict['created_at'].isoformat()
        object_dict['updated_at'] = object_dict['updated_at'].isoformat()
        return object_dict

    def __str__(self):
        """The return satttement of the class"""
        return f"[{self.__class__.__name__}], ({self.id}), {self.__dict__}"
