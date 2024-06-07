import json
import math
import random
import logging

from datetime import datetime, timedelta
from typing import Dict

from helpers import (
    create_random_point,
    determine_sector,
    generate_object_id,
    generate_payload,
)

logging.basicConfig(filename="simulation.log", level=logging.INFO, format="%(message)s")

START_TIME = datetime(2006, 12, 1, 1, 0, 0)
SIMULATION_DURATION = timedelta(hours=10)
END_TIME = START_TIME + SIMULATION_DURATION
NUM_OBJECTS = 500


class FlyingObject:
    def __init__(
        self,
        object_id: str,
        x: float,
        y: float,
        speed: float,
        expire_time: datetime,
        created_time: datetime,
        payload: str,
    ):
        self.object_id = object_id
        self.x = x
        self.y = y
        self.angle = None
        self.speed = speed
        self.expire_time = expire_time
        self.created_time = created_time
        self.payload = payload

    def update_position(self, current_time: datetime):
        elapsed_time = (current_time - self.created_time).total_seconds()
        if (
            elapsed_time > 0
            and elapsed_time <= (self.expire_time - self.created_time).total_seconds()
        ):
            self.x += self.speed * elapsed_time * math.cos(self.angle)
            self.y += self.speed * elapsed_time * math.sin(self.angle)
            self.angle = math.atan2(self.y, self.x)

    def to_dict(self) -> Dict:
        return {
            "object_id": self.object_id,
            "x": self.x,
            "y": self.y,
            "angle": self.angle,
            "speed": self.speed,
            "expire_time": self.expire_time.isoformat(),
            "created_time": self.created_time.isoformat(),
            "payload": self.payload,
            "sector": determine_sector(self.x, self.y),
        }


def create_object() -> FlyingObject:
    object_id = generate_object_id()
    x, y = create_random_point()
    destination_x, destination_y = create_random_point()
    speed = random.uniform(10, 80)
    created_time = START_TIME + timedelta(
        seconds=random.uniform(0, SIMULATION_DURATION.total_seconds())
    )
    expire_time = created_time + timedelta(seconds=abs(destination_x - x) / speed)
    payload = generate_payload()

    obj = FlyingObject(object_id, x, y, speed, expire_time, created_time, payload)
    obj.angle = math.atan2(destination_y - y, destination_x - x)
    return obj


objects = [create_object() for _ in range(NUM_OBJECTS)]


def log_object_state(obj: FlyingObject, current_time: datetime):
    obj.update_position(current_time)
    log_entry = {"timestamp": current_time.isoformat(), "object_data": obj.to_dict()}
    logging.info(json.dumps(log_entry))


current_time = START_TIME
while current_time <= END_TIME:
    for obj in objects:
        log_object_state(obj, current_time)
    current_time += timedelta(milliseconds=150)
