import uuid

from sqlalchemy import String, UUID, Boolean, ARRAY
from sqlalchemy.orm import mapped_column, Mapped
from core.base_model import Base


class Vacancy(Base):
    __tablename__ = "vacancies"  # noqa

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    department: Mapped[str] = mapped_column(String)
    photo_url: Mapped[str] = mapped_column(String)
    logo_url: Mapped[str] = mapped_column(String)
    level: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    important: Mapped[bool] = mapped_column(Boolean)
    info: Mapped[str] = mapped_column(String)
    requirements: Mapped[list[str]] = mapped_column(type_=ARRAY(String), nullable=True)
    tasks: Mapped[list[str]] = mapped_column(type_=ARRAY(String), nullable=True)
    task: Mapped[str] = mapped_column(String)