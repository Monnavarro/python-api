# -- coding: utf-8 --
"""

Created on: 9/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str or None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id" : item_id}
