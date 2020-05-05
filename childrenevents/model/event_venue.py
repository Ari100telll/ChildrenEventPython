from enum import Enum
import json


class EventVenue(int, Enum):
    INDOOR: int = 1
    OUTDOOR: int = 2
    MIXED: int = 3
