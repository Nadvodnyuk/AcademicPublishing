from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

from src.schemas.token import Status
import src.crud.authors_works as crud
from src.schemas.authors_works import AWInSchema, AWOutSchema


router = APIRouter()


@router.get("/authors_works", response_model=List[AWOutSchema])
async def get_authors_works_all():
    return await crud.get_authors_works_all()


@router.get("/authors_works/author/{author_id}", response_model=List[AWOutSchema])
async def get_authors_works_by_author_id(author_id: int) -> AWOutSchema:
    try:
        return await crud.get_authors_works_by_author_id(author_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Instance does not exist",)


@router.get("/authors_works/work/{work_id}", response_model=List[AWOutSchema])
async def get_authors_works_by_work_id(work_id: int) -> AWOutSchema:
    try:
        return await crud.get_authors_works_by_work_id(work_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Instance does not exist",)


@router.get("/authors_works/id/{authors_works_id}", response_model=AWOutSchema)
async def get_authors_works(authors_works_id: int) -> AWOutSchema:
    try:
        return await crud.get_authors_works(authors_works_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Instance does not exist",)


@router.post("/authors_works", response_model=AWOutSchema)
async def create_authors_works(authors_works: AWInSchema) -> AWOutSchema:
    return await crud.create_authors_works(authors_works)



@router.delete(
    "/authors_works/author/{author_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_authors_works_by_author_id(author_id: int) -> Status:
    return await crud.delete_authors_works_by_author_id(author_id)


@router.delete(
    "/authors_works/work/{work_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_authors_works_by_work_id(work_id: int) -> Status:
    return await crud.delete_authors_works_by_work_id(work_id)


@router.delete(
    "/authors_works/id/{authors_works_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_aw(authors_works_id: int) -> Status:
    return await crud.delete_aw(authors_works_id)


@router.delete(
    "/authors_works",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_authors_works(authors_works: AWInSchema) -> Status:
    return await crud.delete_authors_works(authors_works)
