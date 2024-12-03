from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )


# # Example usage
# if __name__ == "__main__":
#     engine = create_engine('sqlite:///example.db')
#     Base.metadata.create_all(engine)
#     Session = scoped_session(sessionmaker(bind=engine))
#     session = Session()

#     # Example model inheriting from Base
#     class ExampleModel(Base):
#         __tablename__ = 'example_model'
#         name = Column(String, nullable=False)

#     # Create a new instance
#     new_instance = ExampleModel(name="example")
#     session.add(new_instance)
#     session.commit()

#     # Update the instance
#     new_instance.name = "updated_example"
#     session.commit()
