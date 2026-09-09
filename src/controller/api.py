from fastapi import APIRouter, Request, Form
from fastapi.responses import FileResponse, RedirectResponse as rr
from fastapi.templating import Jinja2Templates

from database.db import add_to_db, get_all_movies, remove_from_db

router = APIRouter()
templates = Jinja2Templates(directory="../pages")


@router.get("/movies")
async def list_movies(request: Request):
    movies = get_all_movies()
    return templates.TemplateResponse(
        request,
        "list/list.html",
        {"movies": movies}
    )

@router.get("/add")
async def add_movie():
    return FileResponse("../pages/add/add.html")

@router.post("/submit-movie")
async def submit(
    title: str = Form(...),
    genre: str = Form(...)
):
    add_to_db(title=title, genre=genre)

    return rr(status_code=303, url='/movies')
    

@router.post("/delete-movies")
async def submit(ids: list[int] = Form(...)):
    for i in ids:
        remove_from_db(i)

    return rr(status_code=303, url='/movies')