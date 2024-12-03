from datetime import datetime
from typing import Optional

from pydantic import BaseModel as PydanticBaseModel


class EventModel(PydanticBaseModel):
    e_id: Optional[int]
    event_id: int
    type_id: int
    period_id: Optional[int]
    time_min: int
    time_sec: int
    x: float
    y: float
    outcome: Optional[bool]
    timestamp: Optional[datetime]
    last_modified: Optional[datetime]
    match_id: str
    player_id: Optional[str]
    team_id: Optional[str]
