# api_calls.py
from urllib.request import urlopen
import json


class API:
    def __init__(self, base_url):
        self.base_url = base_url
        self.methods = [
            'sessions?',
            'car_data?',
            'drivers?',
            'intervals?',
            'laps?',
            'location?',
            'meetings?',
            'pit?',
            'position?',
            'race control?',
            'stints?',
            'team radio?',
            'weather?'
        ]
        self.variables = [
            'year=',
            'driver_number=',
            'session_key=',
            'country_name='
        ]

    def fetch_data(self, method, params):
        url = self.base_url + method + params
        response = urlopen(url)
        return json.loads(response.read().decode('utf-8'))

    def get_sessions(self, year, session_key=None):
        params = f"{self.variables[0]}{year}"
        if session_key:
            params += f"&{self.variables[2]}{session_key}"
        return self.fetch_data(self.methods[0], params)

    def get_drivers(self, session_key):
        params = f"{self.variables[2]}{session_key}"
        return self.fetch_data(self.methods[2], params)

    def get_positions(self, session_key):
        params = f"{self.variables[2]}{session_key}"
        return self.fetch_data(self.methods[8], params)

    def process_session_data(self, session_data):
        session_keys = [item["session_key"] for item in session_data]
        country_codes = [item["country_code"] for item in session_data]
        session_types = [item["session_type"] for item in session_data]
        circuit_names = [item["circuit_short_name"] for item in session_data]
        circuit_keys = [item["circuit_key"] for item in session_data]
        return list(zip(session_keys, country_codes, session_types, circuit_names, circuit_keys))

    def process_driver_data(self, driver_data, session_key):
        broadcast_names = [item["broadcast_name"] for item in driver_data]
        driver_numbers = [item["driver_number"] for item in driver_data]
        team_names = [item["team_name"] for item in driver_data]
        first_names = [item["first_name"] for item in driver_data]
        last_names = [item["last_name"] for item in driver_data]
        name_acronyms = [item["name_acronym"] for item in driver_data]
        return list(zip(broadcast_names, driver_numbers, [session_key] * len(driver_numbers), team_names, first_names,
                        last_names, name_acronyms))

    def process_position_data(self, position_data, session_key):
        driver_numbers = [item["driver_number"] for item in position_data]
        positions = [item["position"] for item in position_data]
        dates = [item["date"] for item in position_data]
        return list(zip(driver_numbers, [session_key] * len(driver_numbers), positions, dates))
