from datetime import timedelta
from simulation import (
    FlyingObject,
    create_object,
    START_TIME,
    SIMULATION_DURATION,
    determine_sector,
)
from helpers import create_random_point, generate_object_id, generate_payload

def test_create_random_point():
    x, y = create_random_point()
    assert 0 <= x <= 1000
    assert 0 <= y <= 1000

def test_generate_object_id():
    object_id = generate_object_id()
    assert len(object_id) == 32

def test_generate_payload():
    payload = generate_payload()
    assert len(payload) == 200

def test_determine_sector():
    assert determine_sector(100, 100) == "A"
    assert determine_sector(600, 100) == "B"
    assert determine_sector(100, 600) == "C"
    assert determine_sector(600, 600) == "D"
    assert determine_sector(1100, 1100) == "Unknown"

def test_create_object():
    obj = create_object()
    assert isinstance(obj, FlyingObject)
    assert obj.created_time >= START_TIME
    assert obj.created_time <= START_TIME + SIMULATION_DURATION

def test_update_position():
    obj = create_object()
    initial_x, initial_y = obj.x, obj.y
    obj.update_position(obj.created_time + timedelta(seconds=1))
    assert (obj.x, obj.y) != (initial_x, initial_y)

def test_to_dict():
    obj = create_object()
    obj_dict = obj.to_dict()
    assert obj_dict["object_id"] == obj.object_id
    assert obj_dict["sector"] == determine_sector(obj.x, obj.y)
    assert "payload" in obj_dict
