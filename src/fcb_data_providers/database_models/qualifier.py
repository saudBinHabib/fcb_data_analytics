from sqlalchemy import (BigInteger, Boolean, Column, DateTime, Enum, Float,
                        ForeignKey, Integer, String)
from sqlalchemy.orm import relationship

from fcb_data_providers.database_models import BaseModel


class Qualifier(BaseModel):
    __tablename__ = "qualifiers"
    id = Column(Integer, primary_key=True, autoincrement=True)  # qualifier id
    q_id = Column(BigInteger, nullable=True)  # qId
    qualifier_id = Column(Integer, nullable=False)  # qualifierId
    value = Column(String, nullable=True)
    event_id = Column(BigInteger)

    # Foreign Key
    # event_id = Column(BigInteger, ForeignKey("events.id"))
