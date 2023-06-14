#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """User imports from BaseModel"""
    first_name = ""
    last_name = ""
    password = ""
    email = ""
