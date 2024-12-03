from datetime import datetime
from typing import Optional

from pydantic import BaseModel as PydanticBaseModel


class CardModel(PydanticBaseModel):
    match_id: str
    contestant_id: Optional[str]
    period_id: Optional[int]
    time_min: Optional[int]
    time_min_sec: Optional[str]
    last_updated: Optional[datetime]
    timestamp: Optional[datetime]
    type: Optional[str]
    player_id: Optional[str]
    player_name: Optional[str]
    opta_event_id: Optional[str]
    card_reason: Optional[str]
