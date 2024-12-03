from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from fcb_data_providers.database_models import BaseModel


# Match Entity
class Match(BaseModel):
    __tablename__ = "matches"

    id = Column(String, primary_key=True)  # Match ID
    match_date = Column(DateTime)
    match_status = Column(String)  # Played, Scheduled, etc.
    home_team_id = Column(String)
    away_team_id = Column(String)
    winner = Column(String)  # 'home', 'away', or None for draw
    match_length_min = Column(Integer)
    match_length_sec = Column(Integer)
