from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from fcb_data_providers.database_models import BaseModel


class Period(BaseModel):
    __tablename__ = "periods"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Period ID
    match_id = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    length_min = Column(Integer)
    length_sec = Column(Integer)
