from logging import Logger

from sqlalchemy import text
from sqlalchemy.orm.session import Session


def create_match_detail_view(session: Session, logger: Logger) -> bool:
    """
    This method create a view for match_detail information.

    Args:
        session (Session):
        logger (Logger): _description_

    Returns:
        bool: _description_
    """

    CREATE_MATCH_DETAIL_VIEW_QUERY = text
    (
        """
            CREATE OR REPLACE VIEW match_details AS
            SELECT
                m.id,
                m.match_date,
                m.match_status,
                ht.official_name AS home_team_name,
                m.home_team_id,
                at.official_name AS away_team_name,
                m.away_team_id,
                m.winner,
                m.match_length_min,
                m.match_length_sec
            FROM
                matches m
            JOIN
                teams ht ON (m.home_team_id = ht.id)
            JOIN
                teams at ON (m.away_team_id = at.id);
        """
    )

    try:
        session.execute(CREATE_MATCH_DETAIL_VIEW_QUERY)
        session.commit()
        logger.info("Match details view created successfully")
        return True
    except Exception as exc:
        logger.error(f"Error while creating match details view: {exc}")
        return False
