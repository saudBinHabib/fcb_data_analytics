from datetime import date
from typing import Optional

from pydantic import BaseModel as PydanticBaseModel


class MatchModel(PydanticBaseModel):
    id: str
    match_date: Optional[date]
    match_status: Optional[str]
    home_team_id: Optional[str]
    away_team_id: Optional[str]
    winner: Optional[str]
    match_length_min: Optional[int]
    match_length_sec: Optional[int]
