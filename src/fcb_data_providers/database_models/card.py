from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from fcb_data_providers.database_models import BaseModel


class Card(BaseModel):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Card ID
    match_id = Column(String, nullable=False)
    contestant_id = Column(String)  # Team ID of the player receiving the card
    period_id = Column(Integer)
    time_min = Column(Integer)
    time_min_sec = Column(String)  # e.g., "19:53"
    last_updated = Column(DateTime)
    timestamp = Column(DateTime)
    type = Column(String)  # 'YC' (Yellow Card), 'RC' (Red Card)
    player_id = Column(String)  # Player ID receiving the card
    player_name = Column(String)
    opta_event_id = Column(String)
    card_reason = Column(String, nullable=True)  # Reason for the card
