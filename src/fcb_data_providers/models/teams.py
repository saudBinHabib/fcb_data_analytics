from pydantic import BaseModel as PydanticBaseModel


class TeamModel(PydanticBaseModel):
    id: str
    name: str
    short_name: str = None
    official_name: str = None
    code: str = None
