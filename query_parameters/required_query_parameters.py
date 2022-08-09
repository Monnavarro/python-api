# -- coding: utf-8 --
"""

Created on: 9/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def red_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
