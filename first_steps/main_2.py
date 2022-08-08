# -- coding: utf-8 --
"""

Created on: 8/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from fastapi import FastAPI

my_app = FastAPI()

@my_app.get("/")
def root():
    return{"message": "Mi primer API"}