import pytest
from api import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_trajectory(client):
    response = client.get(
        "/trajectory",
        query_string={
            "object_id": "some-object-id",
            "start_time": "2006-12-01T01:00:00",
            "end_time": "2006-12-01T11:00:00",
        },
    )
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_get_snapshot(client):
    response = client.get(
        "/snapshot",
        query_string={
            "sector_id": "A",
            "start_time": "2006-12-01T01:00:00",
            "end_time": "2006-12-01T11:00:00",
        },
    )
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
