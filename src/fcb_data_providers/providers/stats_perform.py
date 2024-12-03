import os
from typing import List

import pandas as pd
from dotenv import load_dotenv

from fcb_data_providers.database import Database
from fcb_data_providers.database_models import (Card, Event, Goal, Match,
                                                Period, Player, Qualifier,
                                                Score, Team)
from fcb_data_providers.models import (CardModel, EventModel, GoalModel,
                                       MatchModel, PeriodModel, PlayerModel,
                                       QualifierModel, ScoreModel, TeamModel)
from fcb_data_providers.utils import get_logger


class StatsPerformProvider:

    def __init__(self, data_path: str, database_url: str):

        self.logger = get_logger(__name__)

        self.logger.info("Initializing StatsPerform data provider")

        self.data_path = data_path

        self.db = Database(database_url=database_url)
        self.db.create_tables()
        self.session = self.db.get_session()

        load_dotenv()

    def get_match_related_files(self, file_type: str) -> List[str]:
        """
        Get the match event data files from the StatsPerform data provider directory.
        :param file_type: str: The type of file to get.
        return: List[str]: List of file names.
        """
        self.logger.info(
            "Getting match event data files from StatsPerform data provider directory"
        )
        return [
            self.data_path + "/" + file
            for file in os.listdir(self.data_path)
            if file.startswith(file_type)
        ]

    def get_json_data(self, file_path: str) -> pd.DataFrame:
        """
        Get the JSON data from the file.

        file_path: str: The file path to the JSON file.

        return: pd.DataFrame: Dataframe.
        """
        return pd.read_json(file_path)

    def store_match_data(self, match_id: str, match_details: dict) -> None:
        """
        Store the match data.

        match_id: str: The match id.
        match_details: dict: The match details.

        return: None
        """
        match_model = MatchModel(
            id=match_id,
            match_date=match_details.get("local_date"),
            match_status=match_details.get("matchStatus"),
            home_team_id=match_details.get("home_team_id"),
            away_team_id=match_details.get("away_team_id"),
            winner=match_details.get("winner"),
            match_length_min=match_details["matchLengthMin"],
            match_length_sec=match_details["matchLengthSec"],
        )
        try:
            self.session.add(Match(**match_model.model_dump()))
            self.session.commit()
        except Exception as e:
            self.logger.error(
                f"Error storing match data for match id: {match_id}. Error: {e}"
            )
            self.session.rollback()

    def store_team_data(self, teams_data: List[dict]) -> None:
        """
        Store the team data.

        teams_data: List[dict]: The team data.

        return: None
        """
        for team_details in teams_data:
            team_model = TeamModel(
                id=team_details.get("id"),
                name=team_details.get("name"),
                short_name=team_details.get("shortName"),
                official_name=team_details.get("officialName"),
                code=team_details.get("code"),
            )
            try:
                self.session.add(Team(**team_model.model_dump()))
                self.session.commit()
            except Exception as e:
                self.logger.error(
                    f"Error storing Team data for team id: {team_details.get('id')}. Error: {e}"
                )
                self.session.rollback()

    def store_period_data(self, match_id: str, match_data: dict) -> None:
        """
        Store the period data.
        match_id: str: The match id.
        match_data: dict: The match data.

        return: None
        """
        periods = match_data.get("period")
        for period in periods:
            period_model = PeriodModel(
                match_id=match_id,
                start_time=period.get("start"),
                end_time=period.get("end"),
                length_min=period.get("lengthMin"),
                length_sec=period.get("lengthSec"),
            )
            try:
                self.session.add(Period(**period_model.model_dump()))
                self.session.commit()
            except Exception as e:
                self.logger.error(
                    f"Error storing Period data for Match id: {match_id}. Error: {e}"
                )
                self.session.rollback()

    def store_score_data(self, match_id: str, match_data: dict) -> None:
        """
        Store the score data.

        match_id: str: The match id.
        match_data: dict: The match data.

        return: None
        """
        scores = match_data.get("scores")
        score_model = ScoreModel(
            match_id=match_id,
            ht_home=scores.get("ht").get("home"),
            ht_away=scores.get("ht").get("away"),
            ft_home=scores.get("ft").get("home"),
            ft_away=scores.get("ft").get("away"),
            total_home=scores.get("total").get("home"),
            total_away=scores.get("total").get("away"),
        )
        try:
            self.session.add(Score(**score_model.model_dump()))
            self.session.commit()
        except Exception as e:
            self.logger.error(
                f"Error storing Score data for Match id: {match_id}. Error: {e}"
            )
            self.session.rollback()

    def store_event_quailifier_data(
        self, event_id: int, qualifiers_data: List[dict]
    ) -> None:
        """
        Store the event qualifier data.

        event_id: int: The event id.
        qualifiers_data: List[dict]: The event qualifier data.

        return: None
        """
        for qualifier in qualifiers_data:

            qualifier_model = QualifierModel(
                q_id=qualifier.get("id"),
                qualifier_id=qualifier.get("qualifierId"),
                value=qualifier.get("value"),
                event_id=event_id,
            )
            try:
                self.session.add(Qualifier(**qualifier_model.model_dump()))
                self.session.commit()
            except Exception as e:
                # import ipdb; ipdb.set_trace()
                self.logger.error(
                    f"Error storing Qualifier data for Event id: {event_id}. Error: {e}"
                )
                self.session.rollback()

    def store_event_data(self, match_id: str, events_data: List[dict]) -> None:
        """
        Store the event data.

        match_id: str: The match id.
        events_data: List[dict]: The event data.

        return: None
        """
        for event in events_data:
            event_id = event.get("id")
            event_model = EventModel(
                e_id=event.get("id"),
                event_id=event.get("eventId"),
                type_id=event.get("typeId"),
                period_id=event.get("periodId"),
                time_min=event.get("timeMin"),
                time_sec=event.get("timeSec"),
                x=event.get("x"),
                y=event.get("y"),
                outcome=event.get("outcome"),
                timestamp=event.get("timestamp"),
                last_modified=event.get("lastModified"),
                match_id=match_id,
                player_id=event.get("playerId"),
                team_id=event.get("contestantId"),
            )
            try:
                self.session.add(Event(**event_model.model_dump()))
                self.session.commit()
                qualifier_data = event.get("qualifier")

                self.store_event_quailifier_data(event_id, qualifier_data)
            except Exception as e:
                self.logger.error(
                    f"Error storing Event data for Match id: {match_id}. Error: {e}"
                )
                self.session.rollback()

    def store_player_data(self, lineups: List[dict]) -> None:
        """
        Store the player data.

        lineups: List[dict]: The lineup data.

        return: None
        """
        for lineup in lineups:
            team_id = lineup.get("contestantId")
            players = lineup.get("player")
            for player in players:
                player_model = PlayerModel(
                    id=player.get("playerId"),
                    first_name=player.get("firstName"),
                    last_name=player.get("lastName"),
                    short_first_name=player.get("shortFirstName"),
                    short_last_name=player.get("shortLastName"),
                    match_name=player.get("matchName"),
                    shirt_number=player.get("shirtNumber"),
                    position=player.get("position"),
                    position_side=player.get("positionSide"),
                    formation_place=player.get("formationPlace"),
                    is_captain=player.get("captain"),
                    team_id=team_id,
                )
                try:
                    self.session.add(Player(**player_model.model_dump()))
                    self.session.commit()

                except Exception as e:
                    self.logger.error(
                        f"Error storing Player data for Player id: {player.get('id')}. Error: {e}"
                    )
                    self.session.rollback()

    def store_goal_data(self, match_id: str, goals_data: List[dict]) -> None:
        """
        Store the goal data.

        match_id: str: The match id.
        goals_data: List[dict]: The goal data.

        return: None
        """
        for goal in goals_data:
            goal_model = GoalModel(
                match_id=match_id,
                contestant_id=goal.get("contestantId"),
                period_id=goal.get("periodId"),
                time_min=goal.get("timeMin"),
                time_min_sec=goal.get("timeMinSec"),
                last_updated=goal.get("lastUpdated"),
                timestamp=goal.get("timestamp"),
                type=goal.get("type"),
                scorer_id=goal.get("scorerId"),
                scorer_name=goal.get("scorerName"),
                assist_player_id=goal.get("assistPlayerId"),
                assist_player_name=goal.get("assistPlayerName"),
                opta_event_id=goal.get("optaEventId"),
                home_score=goal.get("homeScore"),
                away_score=goal.get("awayScore"),
            )
            try:
                self.session.add(Goal(**goal_model.model_dump()))
                self.session.commit()
                self.logger.info(f"Goal data stored for match id: {match_id}")
            except Exception as e:
                self.logger.error(
                    f"Error storing Goal data for Match id: {match_id}. Error: {e}"
                )
                self.session.rollback()

    def store_card_data(self, match_id: str, cards_data: List[dict]) -> None:
        """
        Store the card data.

        match_id: str: The match id.
        cards_data: List[dict]: The card data.

        return: None
        """
        for card in cards_data:
            card_model = CardModel(
                match_id=match_id,
                contestant_id=card.get("contestantId"),
                period_id=card.get("periodId"),
                time_min=card.get("timeMin"),
                time_min_sec=card.get("timeMinSec"),
                last_updated=card.get("lastUpdated"),
                timestamp=card.get("timestamp"),
                type=card.get("type"),
                player_id=card.get("playerId"),
                player_name=card.get("playerName"),
                opta_event_id=card.get("optaEventId"),
                card_reason=card.get("cardReason"),
            )
            try:
                self.session.add(Card(**card_model.model_dump()))
                self.session.commit()
                self.logger.info(f"Card data stored for match id: {match_id}")
            except Exception as e:
                self.logger.error(
                    f"Error storing Card data for Match id: {match_id}. Error: {e}"
                )
                self.session.rollback()

    def process_event_data(self, df_events: pd.DataFrame) -> None:
        """
        Process the event data.

        dataframe: pd.DataFrame: The event data.

        return: None
        """

        match_details = df_events.loc["matchDetails", "liveData"]
        events_data = df_events.loc["event", "liveData"]
        contestants = df_events.loc["contestant", "matchInfo"]

        # getting match id
        match_id = df_events.loc["id", "matchInfo"]

        # getting contestants id.
        home_contestant_id = next(
            contestant["id"]
            for contestant in contestants
            if contestant["position"] == "home"
        )
        away_contestant_id = next(
            contestant["id"]
            for contestant in contestants
            if contestant["position"] == "away"
        )

        # getting match date
        local_date = df_events.loc["localDate", "matchInfo"]

        # adding match info in match_details dictionary
        match_details["local_date"] = local_date
        match_details["home_team_id"] = home_contestant_id
        match_details["away_team_id"] = away_contestant_id

        self.logger.info(f"Storing match data for match id: {match_id}")
        self.store_match_data(match_id, match_details)
        self.logger.info(f"Stored match data for match id: {match_id}")

        self.logger.info(f"Storing team data for match id: {match_id}")
        self.store_team_data(contestants)
        self.logger.info(f"Stored team data for match id: {match_id}")

        self.logger.info(f"Storing period data for match id: {match_id}")
        self.store_period_data(match_id, match_details)
        self.logger.info(f"Stored period data for match id: {match_id}")

        self.logger.info(f"Storing score data for match id: {match_id}")
        self.store_score_data(match_id, match_details)
        self.logger.info(f"Stored score data for match id: {match_id}")

        self.logger.info(f"Storing event data for match id: {match_id}")
        self.store_event_data(match_id, events_data)
        self.logger.info(f"Stored event data for match id: {match_id}")

    def process_stats_data(self, df_stats: pd.DataFrame) -> None:
        """
        Process the stats data.

        dataframe: pd.DataFrame: The stats data.

        return: None
        """

        match_details = df_stats.loc["matchDetails", "liveData"]
        contestants = df_stats.loc["contestant", "matchInfo"]
        lineup = df_stats.loc["lineUp", "liveData"]
        goals = df_stats.loc["goal", "liveData"]
        cards = df_stats.loc["card", "liveData"]

        # getting match id
        match_id = df_stats.loc["id", "matchInfo"]

        # getting contestants id.
        home_contestant_id = next(
            contestant["id"]
            for contestant in contestants
            if contestant["position"] == "home"
        )
        away_contestant_id = next(
            contestant["id"]
            for contestant in contestants
            if contestant["position"] == "away"
        )

        # getting match date
        local_date = df_stats.loc["localDate", "matchInfo"]

        # adding match info in match_details dictionary
        match_details["local_date"] = local_date
        match_details["home_team_id"] = home_contestant_id
        match_details["away_team_id"] = away_contestant_id

        self.logger.info(f"Storing match data for match id: {match_id}")
        self.store_match_data(match_id, match_details)
        self.logger.info(f"Stored match data for match id: {match_id}")

        self.logger.info(f"Storing team data for match id: {match_id}")
        self.store_team_data(contestants)
        self.logger.info(f"Stored team data for match id: {match_id}")

        self.logger.info(f"Storing period data for match id: {match_id}")
        self.store_period_data(match_id, match_details)
        self.logger.info(f"Stored period data for match id: {match_id}")

        self.logger.info(f"Storing score data for match id: {match_id}")
        self.store_score_data(match_id, match_details)
        self.logger.info(f"Stored score data for match id: {match_id}")

        self.logger.info(f"Storing lineup data for match id: {match_id}")
        self.store_player_data(lineup)
        self.logger.info(f"Stored lineup data for match id: {match_id}")

        self.logger.info(f"Storing cards data for match id: {match_id}")
        self.store_card_data(match_id, cards)
        self.logger.info(f"Stored cards data for match id: {match_id}")

        self.logger.info(f"Storing goals data for match id: {match_id}")
        self.store_goal_data(match_id, goals)
        self.logger.info(f"Stored goals data for match id: {match_id}")

    def process_match_event_data(self, file_path_list: List) -> None:
        """
        Process the match event data.

        file_path_list: List: The file path to the match event data file.

        return: None
        """

        for file_path in file_path_list:
            data = self.get_json_data(file_path)
            try:
                self.logger.info(f"Processing match event data from file: {file_path}")
                self.process_event_data(data)
            except Exception as e:
                self.logger.error(
                    f"Error processing match event data from file: {file_path}. Error: {e}"
                )

    def process_match_stats_data(self, file_path_list: List) -> None:
        """
        Process the match stats data.

        file_path_list: list: The file path to the match stats data file.

        return: None
        """

        for file_path in file_path_list:
            data = self.get_json_data(file_path)
            try:
                self.logger.info(f"Processing match stats data from file: {file_path}")
                self.process_stats_data(data)
            except Exception as e:
                self.logger.error(
                    f"Error processing match stats data from file: {file_path}. Error: {e}"
                )

    def process_data(self) -> None:
        """
        Process the data from the StatsPerform data provider.

        return: None
        """

        match_event_files = self.get_match_related_files(file_type="match_event")
        match_stats_files = self.get_match_related_files(file_type="match_stats")
        if not match_event_files and not match_stats_files:
            self.logger.info("No match event or match stats data files found.")
            return
        if match_event_files:
            self.logger.info("Processing match event data.")
            self.process_match_event_data(match_event_files)
        if match_stats_files:
            self.logger.info(" Processing match stats data.")
            self.process_match_stats_data(match_stats_files)
