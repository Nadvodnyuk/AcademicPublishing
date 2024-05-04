from io import BytesIO
from typing import List
from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import Spacer
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

from src.schemas.authors import AuthorOutSchema
from src.schemas.token import Status
from src.database.models import AuthorsWorks, Works
from src.schemas.works import WorkOutSchema
import src.crud.authors_works as crudAW
from tortoise.expressions import Q


async def get_works():
    return await WorkOutSchema.from_queryset(Works.all())


async def get_work(work_id) -> WorkOutSchema:
    return await WorkOutSchema.from_queryset_single(Works.get(id=work_id))


async def create_work(work) -> WorkOutSchema:
    try:
        work_obj = await Works.create(**work.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(
            status_code=401, detail=f"Sorry, that work name already exists.")

    return await WorkOutSchema.from_tortoise_orm(work_obj)


async def update_work(work_id, work) -> WorkOutSchema:
    try:
        await WorkOutSchema.from_queryset_single(Works.get(id=work_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Work {work_id} not found")

    await Works.filter(id=work_id).update(**work.dict(exclude_unset=True))
    return await WorkOutSchema.from_queryset_single(Works.get(id=work_id))


async def delete_work(work_id) -> Status:
    author_works = await AuthorsWorks.filter(work_id=work_id).first()

    if author_works:
        await crudAW.delete_authors_works_by_work_id(work_id)

    try:
        await WorkOutSchema.from_queryset_single(Works.get(id=work_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Work {work_id} not found")

    deleted_count = await Works.filter(id=work_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"Work {work_id} not found")
    return Status(message=f"Deleted work {work_id}")


async def search_filter_works(
    query: str,
    start_year: int = None,
    end_year: int = None,
    field_value: str = None
) -> List[WorkOutSchema]:
    try:
        year = None
        try:
            year = int(query)
        except ValueError:
            pass

        filter_params = (
            Q(field__icontains=query) |
            Q(title__icontains=query) |
            Q(event__icontains=query) |
            Q(status__icontains=query) |
            Q(abstract__icontains=query) |
            Q(key_words__icontains=query) |
            Q(intro__icontains=query) |
            Q(aim__icontains=query) |
            Q(materials_methods__icontains=query) |
            Q(results__icontains=query) |
            Q(conclusion__icontains=query) |
            Q(literature__icontains=query) |
            (Q(year=year) if year is not None else Q())
        )

        if start_year is not None:
            filter_params &= Q(year__gte=start_year)

        if end_year is not None:
            filter_params &= Q(year__lte=end_year)

        if field_value:
            filter_params &= Q(field=field_value)

        results = await Works.filter(filter_params).all()
        return [await WorkOutSchema.from_tortoise_orm(work) for work in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def create_pdf(work_id):
    work_data = await get_work(work_id)
    # authors = work_data.author
    # print('work_data', work_data.author.f5kprh)
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, leftMargin=2*cm,
                            rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    
    pdfmetrics.registerFont(TTFont('TNR', 'times.ttf', 'UTF-8'))
    
    style = getSampleStyleSheet()
    style['Normal'].fontName='TNR'
    # style = styles["Normal"]
    # style.fontName = "Times-Roman"
    style['Normal'].fontSize = 14
    style['Normal'].leading = 14 * 1.5
    style['Normal'].alignment = TA_JUSTIFY
    style['Normal'].firstLineIndent = 1.25 * cm

    title_style = getSampleStyleSheet()
    title_style['Normal'].fontName='TNR'

    title_style['Normal'].fontSize = 14
    title_style['Normal'].leading = 14 * 1.5
    title_style['Normal'].alignment = 1
    title_style['Normal'].fontWeight = "Bold"

    content = []

    field_names = ['ID', 'УДК', 'Название', 'Подготовлено для:', 'Статус', 'Год', 'Организация',
                   'Подразделение', 'Страна', 'Город', 'Индекс', 'Данные о научных руководителях',
                   'Данные о научных консультантах', 'Аннотация', 'Ключевые слова', 'Введение',
                   'Цель', 'Материалы и методы', 'Результаты и обсуждение', 'Заключение', 
                   'Список источников', 'Автор']
    
    print("Длина списка field_names:", len(field_names))
    print("Длина словаря work_data.__dict__:", len(work_data.__dict__))
    
    for idx, (key, value) in enumerate(work_data.__dict__.items()):
        if key != "id":  # не id
            # print('key', key)
            field_name = field_names[idx]
            # print('field_name', field_name)
            field_text = field_name

            if key == 'index' or key == 'year':
                value = str(value)

            value_text = value
            # print('value_text', value_text)

            if key == 'title':
                content.append(Paragraph(value_text, title_style["Normal"]))
            elif key == 'author':
                for valueAuthor in value:
                    content.append(Paragraph(field_text, style["Normal"]))
                    for ix, (k, v) in enumerate(valueAuthor.author_id.__dict__.items()):
                        if k != "id" and k != "created_at" and k != "modified_at":
                            if k == 'a_index':
                                v = str(v)
                            content.append(Paragraph(v, style["Normal"]))  
                    content.append(Spacer(1, 12))           
            else:
                content.append(Paragraph(field_text, style["Normal"]))
                content.append(Paragraph(value_text, style["Normal"]))
            content.append(Spacer(1, 12))
             
    doc.build(content)
    pdf_data = buffer.getvalue()
    buffer.close()

    return pdf_data