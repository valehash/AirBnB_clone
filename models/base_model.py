#!/usr/bin/python3
"""The python base class for the Airbnb project """

from datetime import datetime
import uuid
import models as mp

class BaseModel:
	"""The base Model class"""

	def __init__(self, *args, **kwargs):
		"""Init method"""
		if (kwargs):
			for key,value in kwargs.items():
				if key != '__class__':
					if key in ["created_at", "updated_at"]:
						if isinstance(key, str):
							value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
					setattr(self, key, value)
		else:
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			self.id = str(uuid.uuid4())
			mp.storage.new(self)

	def save(self):
		"""method to update the value of update_at to current time"""
		self.updated_at = datetime.now()
		mp.storage.save()

	def to_dict(self):
		"""method to return a dictionary containing all keys/values of dict"""
		object_dict = self.__dict__.copy()
		object_dict['__class__'] = self.__class__.__name__
		if 'created_at' in object_dict and isinstance(object_dict['created_at'], datetime):
			object_dict['created_at'] = object_dict['created_at'].isoformat()
		if 'updated_at' in object_dict and isinstance(object_dict['updated_at'], datetime):
			object_dict['updated_at'] = object_dict['updated_at'].isoformat()
		return object_dict

	def __str__(self):
		"""The return satttement of the class"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
