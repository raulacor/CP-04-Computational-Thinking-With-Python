from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import FileResponse, RedirectResponse as rr
from fastapi.templating import Jinja2Templates

from database.db import add_to_db, get_all_movies, remove_from_db, get_movie, update_in_db

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


@router.get("/edit/{movie_id}")
async def edit_movie(request: Request, movie_id: int):
    movie = get_movie(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return templates.TemplateResponse(
        request,
        "edit/edit.html",
        {"movie": movie}
    )

@router.post("/update-movie")
async def update(
    movie_id: int = Form(...),
    title: str = Form(...),
    genre: str = Form(...)
):
    update_in_db(movie_id=movie_id, title=title, genre=genre)

    return rr(status_code=303, url='/movies')
