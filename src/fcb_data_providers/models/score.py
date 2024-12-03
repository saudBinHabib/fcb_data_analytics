from pydantic import BaseModel as PydanticBaseModel


class ScoreModel(PydanticBaseModel):
    match_id: str
    ht_home: int = 0
    ht_away: int = 0
    ft_home: int = 0
    ft_away: int = 0
    total_home: int = 0
    total_away: int = 0
