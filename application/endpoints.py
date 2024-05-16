import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import scoped_session
from fastapi.encoders import jsonable_encoder

from core.database import get_session
from application.models import Application
from application.schemas import CreateApplicationRequestSchema, ApplicationSchema, UpdateApplicationRequestSchema

router = APIRouter()


@router.post("/", response_model=ApplicationSchema)
async def create_application(
        data: CreateApplicationRequestSchema,
        db: scoped_session = Depends(get_session)
):
    """
    Create new application
    """
    application = Application(**data.model_dump())
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


@router.patch("/{id}", response_model=ApplicationSchema)
async def update_application(
        application_id: uuid.UUID,
        data: UpdateApplicationRequestSchema,
        db: scoped_session = Depends(get_session)
):
    """
    Update application
    """
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        return HTTPException(
            status_code=404,
            detail="Application not found"
        )
    obj_data = jsonable_encoder(application)  # noqa
    update_data = data.model_dump(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(application, field, update_data[field])
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


@router.get("/", response_model=list[ApplicationSchema])
async def get_all_applications(
        db: scoped_session = Depends(get_session)
):
    """
    Get all applications
    """
    return db.query(Application).all()


@router.get("/{id}", response_model=ApplicationSchema)
async def get_application_by_id(
        application_id: uuid.UUID,
        db: scoped_session = Depends(get_session)
):
    """
    Get application by id
    """
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        return HTTPException(
            status_code=404,
            detail="Application not found"
        )
    return application


@router.delete("/")
async def delete_application(
        application_id: uuid.UUID,
        db: scoped_session = Depends(get_session)
):
    """
    Delete application
    """
    application = db.query(Application).filter(Application.id == application_id).delete()
    if application == 0:
        return HTTPException(
            status_code=404,
            detail="Application not found"
        )
    return {"id": application_id}

