from datetime import datetime
from typing import Optional

from pydantic import BaseModel as PydanticBaseModel


class GoalModel(PydanticBaseModel):
    match_id: str
    contestant_id: Optional[str]
    period_id: Optional[int]
    time_min: Optional[int]
    time_min_sec: Optional[str]
    last_updated: Optional[datetime]
    timestamp: Optional[datetime]
    type: Optional[str]
    scorer_id: Optional[str]
    scorer_name: Optional[str]
    assist_player_id: Optional[str]
    assist_player_name: Optional[str]
    opta_event_id: Optional[str]
    home_score: Optional[int]
    away_score: Optional[int]
