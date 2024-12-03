from sqlalchemy import (BigInteger, Boolean, Column, DateTime, Enum, Float,
                        ForeignKey, Integer, String)
from sqlalchemy.orm import relationship

from fcb_data_providers.database_models import BaseModel


class Event(BaseModel):
    __tablename__ = "events"
    id = Column(BigInteger, primary_key=True, autoincrement=True)  # unique event id
    e_id = Column(BigInteger)
    event_id = Column(Integer)  # eventId
    type_id = Column(Integer)  # typeId
    time_min = Column(Integer)
    time_sec = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    outcome = Column(Boolean)
    timestamp = Column(DateTime)
    last_modified = Column(DateTime)
    match_id = Column(String)
    team_id = Column(String)
    period_id = Column(Integer)
    player_id = Column(String)

    # Foreign Keys
    # match_id = Column(String, ForeignKey("matches.id"))
    # team_id = Column(String, ForeignKey("teams.id"))
    # period_id = Column(Integer, ForeignKey("periods.id"))
    # player_id = Column(String, ForeignKey("players.id"))
