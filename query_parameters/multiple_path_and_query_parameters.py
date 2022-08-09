# -- coding: utf-8 --
"""

Created on: 9/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/Users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q:str or None = None, short: bool = False

):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update( {"q": q})
    if not short:
        item.update(
            {"description": "This is an Amazing item that has a "
                            "long description"}
        )
    return item
