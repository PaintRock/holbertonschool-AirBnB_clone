#!/usr/bin/python3
"""Review from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review module"""
    place_id = ""
    user_id = ""
    text = ""
