#!/usr/bin/env python3
from models.base_model import BaseModel

class Review(BaseModel):
    """The review class would handle reveis left by users"""
    place_id = ''
    user_id = ''
    text = ' '
