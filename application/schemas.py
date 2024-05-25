from uuid import UUID

from core.schemas import Schemas


class ApplicationSchema(Schemas):
    """
    Application schema
    """
    id: UUID
    vacancy_id: UUID
    first_name: str
    last_name: str
    email: str
    phone: str
    telegram: str
    discord: str
    comment: str
    experience: str
    github: str
    work_time: str
    what_do_you_want: str


class CreateApplicationRequestSchema(Schemas):
    """
    Create application schema
    """
    vacancy_id: UUID
    first_name: str
    last_name: str
    email: str
    phone: str
    telegram: str
    discord: str
    comment: str
    experience: str
    github: str
    work_time: str
    what_do_you_want: str


class UpdateApplicationRequestSchema(Schemas):
    """
    Update application request schema
    """
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone: str | None = None
    telegram: str | None = None
    discord: str | None = None
    comment: str | None = None
    experience: str | None = None
    github: str | None = None
    work_time: str | None = None
    what_do_you_want: str | None = None


