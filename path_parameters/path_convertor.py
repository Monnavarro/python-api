# -- coding: utf-8 --
"""

Created on: 9/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path: path}")
async def read_file(file_path: str):
    return {"file_path": file_path}