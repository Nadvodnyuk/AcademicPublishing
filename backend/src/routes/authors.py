from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

from src.schemas.token import Status
import src.crud.authors as crud
from src.schemas.authors import AuthorInSchema, AuthorOutSchema


router = APIRouter()


@router.get("/authors", response_model=List[AuthorOutSchema])
async def get_authors():
    return await crud.get_authors()


@router.get("/author/{author_id}", response_model=AuthorOutSchema)
async def get_author(author_id: int) -> AuthorOutSchema:
    try:
        return await crud.get_author(author_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Author does not exist",)


@router.post("/authors", response_model=AuthorOutSchema)
async def create_author(author: AuthorInSchema) -> AuthorOutSchema:
    return await crud.create_author(author)


@router.delete(
    "/author/{author_id}",
    response_model=Status, responses={404: {"model": HTTPNotFoundError}}
)
async def delete_author(author_id: int) -> Status:
    return await crud.delete_author(author_id)


@router.get("/authors/search", response_model=List[AuthorOutSchema])
async def search_authors(query: str):
    try:
        if(query==''):
            return await crud.get_authors()
        else:
            return await crud.search_authors(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.get("/authors/graphs/{author_id}", response_model=List[str])
async def get_author_graphs(author_id: int):
    # Вызываем функцию из crud для генерации графиков и получения путей к изображениям
    image_paths = await crud.generate_author_works_plots(author_id)
    if not image_paths:
        raise HTTPException(status_code=404, detail="Graphs not found")
    return image_paths