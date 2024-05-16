from uuid import UUID

from pydantic import BaseModel


class ApplicationSchema(BaseModel):
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
    what_do_you_want: str


class CreateApplicationRequestSchema(BaseModel):
    """
    Create application schema
    """
    first_name: str
    last_name: str
    email: str
    phone: str
    telegram: str
    discord: str
    comment: str
    what_do_you_want: str


class UpdateApplicationRequestSchema(BaseModel):
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
    what_do_you_want: str | None = None


