#!/usr/bin/python3
"""
Module: review.py
This module defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Defines Review class which inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
