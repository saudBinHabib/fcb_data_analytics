from sqlalchemy import (JSON, Boolean, Column, DateTime, Enum, Float,
                        ForeignKey, Integer, String)
from sqlalchemy.orm import relationship

from fcb_data_providers.database_models import BaseModel


class Goal(BaseModel):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True, autoincrement=True)  # Goal ID
    match_id = Column(String, nullable=False)
    contestant_id = Column(String)  # Team ID of the scorer
    period_id = Column(Integer)
    time_min = Column(Integer)
    time_min_sec = Column(String)  # e.g., "49:37"
    last_updated = Column(DateTime)
    timestamp = Column(DateTime)
    type = Column(String)  # 'G' for goal
    scorer_id = Column(String)  # Player ID of the scorer
    scorer_name = Column(String)
    assist_player_id = Column(String, nullable=True)
    assist_player_name = Column(String, nullable=True)
    opta_event_id = Column(String)
    home_score = Column(Integer)
    away_score = Column(Integer)
