from sqlalchemy import (JSON, Boolean, Column, DateTime, Enum, Float,
                        ForeignKey, Integer, String)
from sqlalchemy.orm import relationship

from fcb_data_providers.database_models import BaseModel


class Player(BaseModel):
    __tablename__ = "players"
    id = Column(String, primary_key=True)  # player id
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    short_first_name = Column(String)
    short_last_name = Column(String)
    match_name = Column(String, nullable=False)  # e.g., "M. Neuer"
    shirt_number = Column(Integer)
    position = Column(String)  # e.g., Goalkeeper, Defender
    position_side = Column(String)  # e.g., Centre, Left
    formation_place = Column(String)
    is_captain = Column(Boolean, default=False)
    team_id = Column(String)
