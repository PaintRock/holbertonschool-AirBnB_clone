#!/usr/bin/python3
"""Module for city"""
from models.base_model import BaseModel


class City(BaseModel):
    """City and state id"""
    state_id = ""
    name = ""
