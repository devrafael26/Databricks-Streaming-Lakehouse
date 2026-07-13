import json
from pathlib import Path


def load_gold_metrics():
    path = Path("tests/fixtures/gold_order_metrics.json")

    with open(path) as file:
        return json.load(file)


def test_gold_has_records():
    data = load_gold_metrics()

    assert len(data) > 0


def test_gold_metrics_are_valid():
    data = load_gold_metrics()

    for row in data:

        assert row["total_orders"] >= 0
        assert row["total_units"] >= 0
        assert row["avg_units_per_order"] >= 0

        assert row["min_units"] <= row["max_units"]


def test_gold_average_consistency():
    data = load_gold_metrics()

    for row in data:

        if row["total_orders"] > 0:

            calculated_avg = (
                row["total_units"] / row["total_orders"]
            )

            assert row["avg_units_per_order"] == calculated_avg
