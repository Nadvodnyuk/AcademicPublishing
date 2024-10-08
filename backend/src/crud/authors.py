from collections import Counter
import os
from typing import List
from fastapi import HTTPException
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.schemas.token import Status
from src.database.models import Authors, AuthorsWorks, Works
from src.schemas.authors import AuthorOutSchema
import src.crud.authors_works as crudAW
from tortoise.expressions import Q


async def get_authors():
    return await AuthorOutSchema.from_queryset(Authors.all())


async def get_author(author_id) -> AuthorOutSchema:
    return await AuthorOutSchema.from_queryset_single(Authors.get(id=author_id))


async def get_ex_author(author) -> AuthorOutSchema:
    return await AuthorOutSchema.from_queryset_single(Authors.get(code=author.code))


async def create_author(author) -> AuthorOutSchema:
    existing_author = await Authors.filter(full_name=author.full_name, code=author.code).first()
    if existing_author:
        await Authors.filter(full_name=author.full_name, code=author.code).update(**author.dict(exclude_unset=True))
        ex_author = await Authors.filter(full_name=author.full_name, code=author.code).first()
        return await AuthorOutSchema.from_tortoise_orm(ex_author)
    try:
        author_obj = await Authors.create(**author.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(
            status_code=401, detail=f"Sorry, that username already exists.")

    return await AuthorOutSchema.from_tortoise_orm(author_obj)


async def delete_author(author_id) -> Status:
    author_works = await AuthorsWorks.filter(author_id=author_id).first()

    if author_works:
        await crudAW.delete_authors_works_by_author_id(author_id)

    try:
        await AuthorOutSchema.from_queryset_single(Authors.get(id=author_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Author {author_id} not found")

    deleted_count = await Authors.filter(id=author_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"Author {author_id} not found")
    return Status(message=f"Deleted author {author_id}")


async def search_authors(query: str) -> List[AuthorOutSchema]:
    try:
        index = None
        try:
            index = int(query)
        except ValueError:
            pass
        results = await Authors.filter(
            Q(full_name__icontains=query) |
            Q(short_name__icontains=query) |
            Q(code__icontains=query) |
            Q(a_status__icontains=query) |
            Q(a_country__icontains=query) |
            Q(a_city__icontains=query) |
            (Q(a_index=index) if index is not None else Q()) |
            Q(a_adress__icontains=query) |
            Q(a_org__icontains=query) |
            Q(a_sub_org__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        ).all()
        print(results)
        return [await AuthorOutSchema.from_tortoise_orm(author) for author in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def generate_author_works_plots(author_id):
    author_works = await AuthorsWorks.filter(author_id=author_id).all()
    author = await Authors.get(id=author_id)
    code = author.code

    years = []
    fields = []
    statuses = []
    print('все что есть', author_works)
    for aw in author_works:
        print('тольок одна', aw.work_id_id)
        work = await Works.get(id=aw.work_id_id)
        years.append(work.year)
        fields.append(work.field)
        statuses.append(work.status)

    data = pd.DataFrame({'year': years, 'field': fields, 'status': statuses})

    new_folder_path = 'C:\\Users\\Yana\\Desktop\\New'
    os.makedirs(new_folder_path, exist_ok=True)
    folder_path = os.path.join(new_folder_path, code)
    os.makedirs(folder_path, exist_ok=True)

    image_paths = []

    for year, group in data.groupby('year'):
        fig, ax = plt.subplots(figsize=(15, 6))
        group = group.groupby(['field', 'status']).size().unstack(fill_value=0)
        colors = plt.cm.get_cmap('Pastel1')(
            np.linspace(0, 1, len(group.columns)))
        bottom = None
        for i, (status, color) in enumerate(zip(group.columns, colors)):
            if bottom is None:
                ax.barh(group.index, group[status], label=status, color=color, alpha=0.7, height = 0.3)
                bottom = group[status]
            else:
                ax.barh(group.index, group[status], left=bottom, label=status, color=color, alpha=0.7, height = 0.3)
                bottom += group[status]
        # ax.set_ylabel('Разделы')
        ax.text(-0.4, -0.07, 'Разделы', fontsize=10, rotation=0, ha='center', va='center', transform=ax.transAxes)
        ax.set_xlabel('Количество статей')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        # ax.set_title(f'Статьи за {year} от {author.short_name}')
        ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1), frameon=False)
        ax.tick_params(axis='y', length=0, labelsize=12)
        ax.spines['left'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(axis='y', length=0)
        plt.tight_layout()
        filename = os.path.join(folder_path, f'{code}_{year}.png')
        filenameNew = os.path.join(code, f'{code}_{year}.png')
        plt.savefig(filename)
        
        image_paths.append(filenameNew)
        plt.close()

    return image_paths

async def generate_author_pie(author_id):
    author_works = await AuthorsWorks.filter(author_id=author_id).all()
    author = await Authors.get(id=author_id)
    code = 'test'

    field = []
    for aw in author_works:
        work = await Works.get(id=aw.work_id_id)
        field.append(work.field)


    new_folder_path = 'C:\\Users\\Yana\\Desktop\\New'
    os.makedirs(new_folder_path, exist_ok=True)
    folder_path = os.path.join(new_folder_path, code)
    os.makedirs(folder_path, exist_ok=True)

    files_and_folders = os.listdir(folder_path)

    image_path = []

    for item in files_and_folders:
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)

    os.makedirs(folder_path, exist_ok=True)

    field_counts = Counter(field)

    plt.figure(figsize=(10, 4))
    ax = plt.gca()

    labels = ['{} ({:.1f}%)'.format(field, (count/sum(field_counts.values()))*100)
              for field, count in field_counts.items()]
    colors = plt.get_cmap('tab10')(range(len(field_counts)))
    wedges, texts, autotexts = ax.pie(field_counts.values(), labels=labels, startangle=90, wedgeprops=dict(width=0.4),
                                      autopct='', textprops=dict(color="black"), colors=plt.cm.Pastel1.colors)

    centre_circle = plt.Circle((0, 0), 0.5, fc='white')

    ax.add_artist(centre_circle)
    plt.title(f'УДК использованные автором {author.short_name}')

    filename = os.path.join(folder_path, f'{code}.png')
    filenameNew = os.path.join(code, f'{code}.png')
    plt.savefig(filename)
        
    image_path.append(filenameNew)
    plt.close()

    return image_path
