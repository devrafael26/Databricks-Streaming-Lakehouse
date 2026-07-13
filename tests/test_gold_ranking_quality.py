import json
from pathlib import Path


def load_city_ranking():
    path = Path("tests/fixtures/gold_city_ranking.json")

    with open(path) as file:
        return json.load(file)


def load_state_ranking():
    path = Path("tests/fixtures/gold_state_ranking.json")

    with open(path) as file:
        return json.load(file)


def test_city_ranking_quality():

    data = load_city_ranking()

    assert len(data) > 0

    for row in data:

        assert row["state"] is not None
        assert row["city"] is not None

        assert row["total_orders"] >= 0
        assert row["total_units"] >= 0
        assert row["avg_units"] >= 0



def test_state_ranking_quality():

    data = load_state_ranking()

    assert len(data) > 0

    for row in data:

        assert row["state"] is not None

        assert row["total_orders"] >= 0
        assert row["total_units"] >= 0
        assert row["avg_units"] >= 0
