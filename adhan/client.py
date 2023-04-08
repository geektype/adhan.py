from typing import Optional
from adhan.const import TIMINGS_URL
from adhan.utils import json_timings, json_hijri
from .models import *
import requests

class Client:
    """Client responsible for interfacing with the API"""
    def __init__(
            self,
            latitude: Optional[float] = None,
            longitude: Optional[float] = None,
            address: Optional[str] = None,
            city: Optional[str] = None,
            country: Optional[str] = None,
            state: Optional[str] = None
            ):

        self._latitude = latitude
        self._longitude = longitude
        self._address = address
        self._city = city
        self._country = country
        self._state = state

    def get_day(self, date: Optional[str] = None) -> Prayer:
        if date:
            url = f"{TIMINGS_URL}/{date}"
        else:
            url = TIMINGS_URL
        resp = requests.get(
            url,
            {
                'latitude': self._latitude,
                'longitude': self._longitude,
                'iso8601': 'true'
            }
        ).json()
        timings = json_timings(resp['data']['timings'])
        hijri = json_hijri(resp['data']['date']['hijri'])

        return Prayer(timings, hijri)
        
