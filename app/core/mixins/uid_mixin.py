import uuid

from sqlalchemy import UUID, text
from sqlalchemy.orm import Mapped, declarative_mixin, mapped_column


@declarative_mixin
class UIDMixin:
    """Mixin that adds UUID column to a SQLAlchemy model."""

    uid: Mapped[uuid.UUID] = mapped_column(
        UUID,
        unique=True,
        default=uuid.uuid4,
        server_default=text("uuid_generate_v4()"),
        sort_order=1000,
    )
