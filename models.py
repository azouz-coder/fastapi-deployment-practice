from sqlalchemy import Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Visit(Base):
    __tablename__= "visits"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement= True
    )
    visit_at: Mapped[DateTime] = mapped_column(DateTime,server_default=func.now())