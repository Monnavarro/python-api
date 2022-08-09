# -- coding: utf-8 --
"""

Created on: 8/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def red_item(item_id):
    return {"item_id": item_id}


