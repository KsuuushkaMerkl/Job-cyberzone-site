import uuid

from sqlalchemy import ForeignKey, String, UUID, ARRAY
from sqlalchemy.orm import mapped_column, Mapped
from core.base_model import Base


class Application(Base):
    __tablename__ = "applications"  # noqa

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vacancy_id: Mapped[int] = mapped_column(ForeignKey("vacancies.id", ondelete="CASCADE"))
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    telegram: Mapped[str] = mapped_column(String)
    discord: Mapped[str] = mapped_column(String)
    comment: Mapped[str] = mapped_column(String)
    experience: Mapped[str] = mapped_column(String)
    github: Mapped[str] = mapped_column(String)
    work_time: Mapped[str] = mapped_column(String)
    what_do_you_want: Mapped[str] = mapped_column(String)
