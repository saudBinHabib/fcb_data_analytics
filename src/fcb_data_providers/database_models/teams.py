from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from fcb_data_providers.database_models import BaseModel


class Team(BaseModel):
    __tablename__ = "teams"
    id = Column(String, primary_key=True)  # team id
    name = Column(String, nullable=False)
    short_name = Column(String)
    official_name = Column(String)
    code = Column(String)
