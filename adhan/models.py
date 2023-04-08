from dataclasses import dataclass
from datetime import datetime

@dataclass
class Timings:
    Fajr: datetime
    Sunrise: datetime
    Dhuhr: datetime
    Asr: datetime
    Sunset: datetime
    Maghrib: datetime
    Isha: datetime
    Imsak: datetime
    Midnight: datetime
    Firstthird: datetime
    Lastthird: datetime

@dataclass
class Hijri:
    Date: str
    Month: str
    Year: int

@dataclass
class Prayer:
    timings: Timings
    hijri: Hijri
