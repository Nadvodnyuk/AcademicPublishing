from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

from src.schemas.token import Status
import src.crud.authors_works as crud
from src.schemas.authors_works import AWInSchema, AWOutSchema


router = APIRouter()

# работает
@router.get("/authors_works", response_model=List[AWOutSchema])
async def get_authors_works_all():
    return await crud.get_authors_works_all()

# работает
@router.get("/authors_works/author/{author_id}", response_model=List[AWOutSchema])
async def get_authors_works_by_author_id(author_id: int) -> AWOutSchema:
    try:
        return await crud.get_authors_works_by_author_id(author_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Instance does not exist",)

# работает
@router.get("/authors_works/work/{work_id}", response_model=List[AWOutSchema])
async def get_authors_works_by_work_id(work_id: int) -> AWOutSchema:
    try:
        return await crud.get_authors_works_by_work_id(work_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Instance does not exist",)

# работает
@router.get("/authors_works/id/{authors_works_id}", response_model=AWOutSchema)
async def get_authors_works(authors_works_id: int) -> AWOutSchema:
    try:
        return await crud.get_authors_works(authors_works_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Instance does not exist",)

# работает
@router.post("/authors_works", response_model=AWOutSchema)
async def create_authors_works(authors_works: AWInSchema) -> AWOutSchema:
    return await crud.create_authors_works(authors_works)


# Придумать функцию, которая получает список author_id, и один work_id
# потом записывает поочереди

# работает
@router.delete(
    "/authors_works/author/{author_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_authors_works_by_author_id(author_id: int) -> Status:
    return await crud.delete_authors_works_by_author_id(author_id)

# работает
@router.delete(
    "/authors_works/work/{work_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_authors_works_by_work_id(work_id: int) -> Status:
    return await crud.delete_authors_works_by_work_id(work_id)

# как-то нужно завтра потестить
@router.delete(
    "/authors_works/id/{authors_works_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_aw(authors_works_id: int) -> Status:
    return await crud.delete_aw(authors_works_id)

# как-то нужно завтра потестить
@router.delete(
    "/authors_works",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_authors_works(authors_works: AWInSchema) -> Status:
    return await crud.delete_authors_works(authors_works)
