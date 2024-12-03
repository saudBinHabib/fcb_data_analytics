from typing import Optional

from pydantic import BaseModel as PydanticBaseModel


class QualifierModel(PydanticBaseModel):
    q_id: Optional[int]
    qualifier_id: Optional[int]
    value: str | None = None
    event_id: Optional[int]
