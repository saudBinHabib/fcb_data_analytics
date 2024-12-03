from unittest.mock import MagicMock, patch

import pytest

from fcb_data_providers.providers import StatsPerformProvider


@pytest.fixture
def stats_perform_provider():
    return StatsPerformProvider(
        data_path="test_data_path", database_url="sqlite:///:memory:"
    )


def test_get_match_related_files(stats_perform_provider):
    with patch(
        "os.listdir",
        return_value=["match_event_1.json", "match_stats_1.json", "other_file.txt"],
    ):
        result = stats_perform_provider.get_match_related_files("match_event")
        assert result == ["test_data_path/match_event_1.json"]


def test_get_json_data(stats_perform_provider):
    with patch("pandas.read_json", return_value="mock_dataframe") as mock_read_json:
        result = stats_perform_provider.get_json_data("test_file_path.json")
        mock_read_json.assert_called_once_with("test_file_path.json")
        assert result == "mock_dataframe"


def test_store_match_data(stats_perform_provider):
    stats_perform_provider.session = MagicMock()
    match_details = {
        "local_date": "2023-10-01",
        "matchStatus": "completed",
        "home_team_id": "team_1",
        "away_team_id": "team_2",
        "winner": "team_1",
        "matchLengthMin": 90,
        "matchLengthSec": 0,
    }
    stats_perform_provider.store_match_data("match_1", match_details)
    stats_perform_provider.session.add.assert_called_once()
    stats_perform_provider.session.commit.assert_called_once()


def test_store_team_data(stats_perform_provider):
    stats_perform_provider.session = MagicMock()
    teams_data = [
        {
            "id": "team_1",
            "name": "Team 1",
            "shortName": "T1",
            "officialName": "Team One",
            "code": "T1",
        },
        {
            "id": "team_2",
            "name": "Team 2",
            "shortName": "T2",
            "officialName": "Team Two",
            "code": "T2",
        },
    ]
    stats_perform_provider.store_team_data(teams_data)
    assert stats_perform_provider.session.add.call_count == 2
    assert stats_perform_provider.session.commit.call_count == 2


def test_store_score_data(stats_perform_provider):
    stats_perform_provider.session = MagicMock()
    match_data = {
        "scores": {
            "ht": {"home": 1, "away": 0},
            "ft": {"home": 2, "away": 1},
            "total": {"home": 2, "away": 1},
        }
    }
    stats_perform_provider.store_score_data("match_1", match_data)
    stats_perform_provider.session.add.assert_called_once()
    stats_perform_provider.session.commit.assert_called_once()
