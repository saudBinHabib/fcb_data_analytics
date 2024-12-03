from pydantic import BaseModel as PydanticBaseModel


class PlayerModel(PydanticBaseModel):
    id: str
    first_name: str
    last_name: str
    short_first_name: str | None = None
    short_last_name: str | None = None
    match_name: str
    shirt_number: int | None = None
    position: str | None = None
    position_side: str | None = None
    formation_place: str | None = None
    is_captain: str | None = None
    team_id: str
