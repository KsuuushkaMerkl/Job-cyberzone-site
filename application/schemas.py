from uuid import UUID
from pydantic import Field, AliasChoices
from core.schemas import Schemas


class ApplicationSchema(Schemas):
    """
    Application schema
    """
    id: UUID
    vacancy_id: UUID = Field(validation_alias=AliasChoices("vacancy_id", "vacancyId"))
    first_name: str = Field(validation_alias=AliasChoices("first_name", "firstName"))
    last_name: str = Field(validation_alias=AliasChoices("last_name", "lastName"))
    email: str
    phone: str
    telegram: str
    discord: str
    comment: str
    experience: str
    github: str
    work_time: str = Field(validation_alias=AliasChoices("work_time", "workTime"))
    what_do_you_want: str = Field(validation_alias=AliasChoices("what_do_you_want", "whatDoYouWant"))


class CreateApplicationRequestSchema(Schemas):
    """
    Create application schema
    """
    vacancy_id: UUID = Field(validation_alias=AliasChoices("vacancy_id", "vacancyId"))
    first_name: str = Field(validation_alias=AliasChoices("first_name", "firstName"))
    last_name: str = Field(validation_alias=AliasChoices("last_name", "lastName"))
    email: str
    phone: str
    telegram: str
    discord: str
    comment: str
    experience: str
    github: str
    work_time: str = Field(validation_alias=AliasChoices("work_time", "workTime"))
    what_do_you_want: str = Field(validation_alias=AliasChoices("what_do_you_want", "whatDoYouWant"))


class UpdateApplicationRequestSchema(Schemas):
    """
    Update application request schema
    """
    first_name: str | None = Field(None, validation_alias=AliasChoices("first_name", "firstName"))
    last_name: str | None = Field(None, validation_alias=AliasChoices("last_name", "lastName"))
    email: str | None = None
    phone: str | None = None
    telegram: str | None = None
    discord: str | None = None
    comment: str | None = None
    experience: str | None = None
    github: str | None = None
    work_time: str | None = Field(None, validation_alias=AliasChoices("work_time", "workTime"))
    what_do_you_want: str | None = Field(None, validation_alias=AliasChoices("what_do_you_want", "whatDoYouWant"))


