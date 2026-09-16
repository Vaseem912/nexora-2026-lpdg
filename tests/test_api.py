import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_valid_week(client):
    response = client.get("/predictions?week=2026-02-02")

    assert response.status_code == 200
    assert len(response.json) == 15


def test_missing_week(client):
    response = client.get("/predictions")

    assert response.status_code == 400


def test_invalid_week(client):
    response = client.get("/predictions?week=2099-01-01")

    assert response.status_code == 404