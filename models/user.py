#!/usr/bin/python3
"""
Module: user.py
This module defines the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Defines User class which inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
