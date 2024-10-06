from datetime import datetime
from uuid import UUID
from pydantic import Field, AliasChoices

from application.models import ApplicationStatus
from core.schemas import Schemas


class ApplicationSchema(Schemas):
    """
    Application schema
    """
    id: UUID
    vacancy_id: UUID = Field(validation_alias=AliasChoices("vacancy_id", "vacancyId"))
    full_name: str = Field(validation_alias=AliasChoices("full_name", "fullName"))
    email: str
    phone: str
    telegram: str
    comment: str
    experience: str
    portfolio: str
    work_time: str = Field(validation_alias=AliasChoices("work_time", "workTime"))
    what_do_you_want: str = Field(validation_alias=AliasChoices("what_do_you_want", "whatDoYouWant"))
    created_at: datetime = Field(validation_alias=AliasChoices("created_at", "createdAt"))
    answered_at: datetime = Field(validation_alias=AliasChoices("answered_at", "answeredAt"))
    status: ApplicationStatus


class CreateApplicationRequestSchema(Schemas):
    """
    Create application schema
    """
    vacancy_id: UUID = Field(validation_alias=AliasChoices("vacancy_id", "vacancyId"))
    full_name: str = Field(validation_alias=AliasChoices("full_name", "fullName"))
    email: str
    phone: str
    telegram: str
    comment: str
    experience: str
    portfolio: str
    work_time: str = Field(validation_alias=AliasChoices("work_time", "workTime"))
    what_do_you_want: str = Field(validation_alias=AliasChoices("what_do_you_want", "whatDoYouWant"))
    answered_at: datetime = Field(validation_alias=AliasChoices("answered_at", "answeredAt"))
    status: ApplicationStatus = Field(default=ApplicationStatus.PENDING)


class UpdateApplicationRequestSchema(Schemas):
    """
    Update application request schema
    """
    full_name: str = Field(validation_alias=AliasChoices("full_name", "fullName"))
    email: str | None = None
    phone: str | None = None
    telegram: str | None = None
    comment: str | None = None
    experience: str | None = None
    portfolio: str | None = None
    work_time: str | None = Field(None, validation_alias=AliasChoices("work_time", "workTime"))
    what_do_you_want: str | None = Field(None, validation_alias=AliasChoices("what_do_you_want", "whatDoYouWant"))
    status: ApplicationStatus | None = None

class UpdateApplicationStatusSchema(Schemas):
    """
    Update status application schema
    """
    status: bool