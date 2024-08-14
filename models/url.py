from sqlalchemy.orm import mapped_column
from sqlalchemy import String, DateTime
from datetime import datetime
from database.db import Base

class Url(Base):
    __tablename__ = "urls"

    id = mapped_column(String, primary_key=True)
    alias = mapped_column(String, unique=True)
    url = mapped_column(String)
    create_at = mapped_column(DateTime, default=datetime.now)