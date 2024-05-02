from io import BytesIO
from typing import List
from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import Spacer

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


def create_pdf(work_id):
    work_data = Works.get(id=work_id)
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, leftMargin=2*cm,
                            rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)

    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.fontName = "Times-Roman"
    style.fontSize = 14
    style.leading = 14 * 1.5
    # style.alignment = TA_JUSTIFY
    style.firstLineIndent = 1.25 * cm
    
    title_style = ParagraphStyle(
        name='TitleStyle',
        fontSize=14,
        fontWeight="Bold",
        alignment=1
    )

    content = []
    # допиши
    field_names = []
    
    for key, value in work_data.items():
        if key != "id":  # не id
            field_name = field_names[key]
            field_text = '<font name="Times-Roman">{0}</font>'.format(field_name)
            value_text = '<font name="Times-Roman">{0}</font>'.format(value)
            if key == 'title':
                title_paragraph = Paragraph(value_text, title_style)
                content.append(title_paragraph)
            else:
                content.append(Paragraph(field_text, style))
                content.append(Paragraph(value_text, style))
            content.append(Spacer(1, 12))  # Пустое пространство

    doc.build(content)
    pdf_data = buffer.getvalue()
    buffer.close()

    return pdf_data
