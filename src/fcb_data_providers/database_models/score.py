from sqlalchemy import (JSON, Boolean, Column, DateTime, Enum, Float,
                        ForeignKey, Integer, String)
from sqlalchemy.orm import relationship

from fcb_data_providers.database_models import BaseModel


class Score(BaseModel):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Score ID
    match_id = Column(String, nullable=False)
    ht_home = Column(Integer, default=0)  # Halftime home score
    ht_away = Column(Integer, default=0)
    ft_home = Column(Integer, default=0)  # Full-time home score
    ft_away = Column(Integer, default=0)
    total_home = Column(Integer, default=0)  # Total score for home team
    total_away = Column(Integer, default=0)
