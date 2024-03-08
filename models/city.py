#!/usr/bin/python3
"""
Module: city.py
This module defines the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Defines City class which inherits from BaseModel
    """
    name = ""
    state_id = ""
