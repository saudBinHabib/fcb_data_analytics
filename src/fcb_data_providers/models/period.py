from datetime import datetime

from pydantic import BaseModel as PydanticBaseModel


class PeriodModel(PydanticBaseModel):
    match_id: str
    start_time: datetime
    end_time: datetime
    length_min: int
    length_sec: int
