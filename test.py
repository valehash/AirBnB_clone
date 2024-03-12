#!/usr/bin/python3
from models.base_model import BaseModel

bm = BaseModel()
sbm = bm.to_dict()
print(sbm["id"])
s_bm = str(bm)

print(s_bm.split(" ")[0])
print(s_bm.split(" ")[1] == "({})".format(bm.id))
