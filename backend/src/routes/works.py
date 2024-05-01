import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

from src.schemas.token import Status
import src.crud.works as crud
from src.schemas.works import WorkInSchema, WorkOutSchema, UpdateWork


router = APIRouter()


@router.get("/works", response_model=List[WorkOutSchema])
async def get_works():
    return await crud.get_works()


@router.get("/work/{work_id}", response_model=WorkOutSchema)
async def get_work(work_id: int) -> WorkOutSchema:
    try:
        return await crud.get_work(work_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Work does not exist",)


@router.post("/works", response_model=WorkOutSchema)
async def create_work(work: WorkInSchema) -> WorkOutSchema:
    return await crud.create_work(work)


@router.patch(
    "/work/{work_id}",
    response_model=WorkOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_work(work_id: int, work: UpdateWork,) -> WorkOutSchema:
    return await crud.update_work(work_id, work)


@router.delete(
    "/work/{work_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_work(work_id: int) -> Status:
    return await crud.delete_work(work_id)


@router.get("/works/search", response_model=List[WorkOutSchema])
async def search_filter_works(
        query: str,
        start_year: int,
        end_year: int,
        field_value: str):
    try:
        if (query == '' and start_year == 0 and end_year == datetime.datetime.now().year and field_value == ''):
            return await crud.get_works()
        else:
            return await crud.search_filter_works(query, start_year, end_year, field_value)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
