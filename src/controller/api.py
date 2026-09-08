from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import FileResponse
import sqlite3 as sql
from database.db import add_to_db
router = APIRouter()

@router.get("/add")
async def add_movie():
    return FileResponse('../pages/add_movie.html')

@router.post("/submit-movie")
async def submit(
    title: str = Form(...),
    genre: str = Form(...)
):
    add_to_db(title=title, genre=genre)