from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from fcb_data_providers.database_models import BaseModel
from fcb_data_providers.utils import get_logger


class Database:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        BaseModel.metadata.bind = self.engine
        self.logger = get_logger(__name__)

    def get_session(self):
        self.logger.info("Getting session")
        return self.Session()

    def create_tables(self):
        self.logger.info("Creating tables")
        BaseModel.metadata.create_all(self.engine)

    def drop_tables(self):
        self.logger.info("Dropping tables")
        BaseModel.metadata.drop_all(self.engine)

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.Session()
        try:
            yield session
            session.commit()  # Commit if no exceptions
        except Exception as e:
            session.rollback()  # Rollback on exception
            raise e  # Re-raise the exception to handle it outside if needed
        finally:
            session.close()  #


# Example usage:
# db = Database('sqlite:///example.db')
# session = db.get_session()
# db.create_tables()
# Example usage with PostgreSQL:
# db = Database('postgresql://username:password@localhost:5432/mydatabase')
# session = db.get_session()
# db.create_tables()
