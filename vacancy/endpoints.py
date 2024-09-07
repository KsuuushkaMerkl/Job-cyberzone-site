import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import scoped_session
from fastapi.encoders import jsonable_encoder

from core.database import get_session
from vacancy.models import Vacancy
from vacancy.schemas import VacancyIdSchema, CreateVacancyRequestSchema, UpdateVacancyRequestSchema, \
    logo_url, photo_url, AllVacancySchema, VacancyAdminSchema, UpdateVacancyResponseSchema

router = APIRouter()


@router.post("/")
async def create_vacancy(
        data: CreateVacancyRequestSchema,
        db: scoped_session = Depends(get_session)
):
    """
    Create new vacancy
    """
    vacancy = Vacancy(**data.model_dump())
    vacancy.photo_url = photo_url.get(data.department, '')
    vacancy.logo_url = logo_url.get(data.department, '')
    db.add(vacancy)
    db.commit()
    db.refresh(vacancy)
    return vacancy


@router.patch("/{vacancy_id}", response_model=UpdateVacancyResponseSchema)
async def update_vacancy(
        vacancy_id: uuid.UUID,
        data: UpdateVacancyRequestSchema,
        db: scoped_session = Depends(get_session)
):
    """
    Update vacancy
    """
    vacancy = db.query(Vacancy).filter(Vacancy.id == vacancy_id).first()
    if not vacancy:
        return HTTPException(
            status_code=404,
            detail="Vacancy not found"
        )
    obj_data = jsonable_encoder(vacancy)  # noqa
    update_data = data.model_dump(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(vacancy, field, update_data[field])
    vacancy.photo_url = photo_url.get(vacancy.department, '')
    vacancy.logo_url = logo_url.get(vacancy.department, '')
    db.add(vacancy)
    db.commit()
    db.refresh(vacancy)
    return vacancy


@router.get("/", response_model=list[AllVacancySchema])
async def get_all_vacancies(
        db: scoped_session = Depends(get_session)
):
    """
    Get all vacancy
    """
    return db.query(Vacancy).all()


@router.get("/vacancy/admin", response_model=list[VacancyAdminSchema])
async def get_admin_vacancies(
        db: scoped_session = Depends(get_session)
):
    """
    Get admin all vacancy
    """
    return db.query(Vacancy).all()


@router.get("/{vacancy_id}", response_model=VacancyIdSchema)
async def get_vacancy_by_id(
        vacancy_id: uuid.UUID,
        db: scoped_session = Depends(get_session)
):
    """
    Get vacancy by id
    """
    vacancy = db.query(Vacancy).filter(Vacancy.id == vacancy_id).first()
    if not vacancy:
        return HTTPException(
            status_code=404,
            detail="Vacancy not found"
        )
    return vacancy


@router.delete("/{vacancy_id}")
async def delete_vacancy(
        vacancy_id: uuid.UUID,
        db: scoped_session = Depends(get_session)
):
    """
    Delete vacancy
    """
    vacancy = db.query(Vacancy).filter(Vacancy.id == vacancy_id).delete()
    if vacancy == 0:
        return HTTPException(
            status_code=404,
            detail="Vacancy not found"
        )
    return {"id": vacancy_id}
