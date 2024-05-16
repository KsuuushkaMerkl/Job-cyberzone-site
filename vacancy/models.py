import uuid

from sqlalchemy import String, UUID, Boolean
from sqlalchemy.orm import mapped_column, Mapped
from core.base_model import Base


class Vacancy(Base):
    __tablename__ = "vacancies"  # noqa

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    departament: Mapped[str] = mapped_column(String)
    level: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    important: Mapped[bool] = mapped_column(Boolean)
    logo: Mapped[str] = mapped_column(String)
    header: Mapped[str] = mapped_column(String)
    info: Mapped[str] = mapped_column(String)
