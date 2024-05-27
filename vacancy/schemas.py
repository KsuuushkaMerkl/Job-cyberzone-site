from uuid import UUID

from core.schemas import Schemas


class VacancySchema(Schemas):
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
    requirements: list[str]
    tasks: list[str]


class VacancyIdSchema(Schemas):
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
    requirements: list[str]
    tasks: list[str]


class CreateVacancyRequestSchema(Schemas):
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
    requirements: list[str]
    tasks: list[str]


class UpdateVacancyRequestSchema(Schemas):
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
    requirements: list[str] | None = None
    tasks: list[str] | None = None

