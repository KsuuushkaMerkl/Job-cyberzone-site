from uuid import UUID

from pydantic import BaseModel


class VacancySchema(BaseModel):
    """
    Vacancy schema
    """
    id: UUID
    name: str
    departament: str
    level: str
    location: str
    important: bool
    logo: str


class VacancyIdSchema(BaseModel):
    """
    Vacancy schema
    """
    id: UUID
    name: str
    departament: str
    level: str
    location: str
    logo: str
    header: str
    info: str


class CreateVacancyRequestSchema(BaseModel):
    """
    Create vacancy request schema
    """ 
    name: str
    departament: str
    level: str
    location: str
    important: bool
    logo: str
    header: str
    info: str


class UpdateVacancyRequestSchema(BaseModel):
    """
    Update vacancy request schema
    """
    name: str | None = None
    departament: str | None = None
    level: str | None = None
    location: str | None = None
    important: bool | None = None
    logo: str | None = None
    header: str | None = None
    info: str | None = None

