import math
import random
import uuid

WORLD_WIDTH = 1000
WORLD_HEIGHT = 1000

SECTORS = {
    "A": {"x_range": (0, 500), "y_range": (0, 500)},
    "B": {"x_range": (500, 1000), "y_range": (0, 500)},
    "C": {"x_range": (0, 500), "y_range": (500, 1000)},
    "D": {"x_range": (500, 1000), "y_range": (500, 1000)},
}


def create_random_point():
    return random.uniform(0, WORLD_WIDTH), random.uniform(0, WORLD_HEIGHT)


def determine_sector(x: float, y: float) -> str:
    for sector, ranges in SECTORS.items():
        if (
            ranges["x_range"][0] <= x < ranges["x_range"][1]
            and ranges["y_range"][0] <= y < ranges["y_range"][1]
        ):
            return sector
    return "Unknown"


def generate_payload() -> str:
    return "".join(random.choices("0123456789abcdef", k=200))


def generate_object_id() -> str:
    return uuid.uuid4().hex


def normalize_angle(angle: float) -> float:
    return angle % (2 * math.pi)
