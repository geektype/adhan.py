from typing import Any, Dict

from adhan.models import Hijri, Timings
from datetime import datetime


def json_timings(timings: Dict[Any, Any]) -> Timings:
    t = timings
    for k, v in t.items():
        timings[k] = datetime.fromisoformat(v)

    return Timings(**t)

def json_hijri(hijri: Dict[Any, Any]) -> Hijri:
    return Hijri(
        Date = hijri['date'],
        Month = hijri['month']['en'],
        Year = int(hijri['year']),
    ) 

