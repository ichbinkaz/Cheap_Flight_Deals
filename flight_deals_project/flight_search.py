from os import getenv
import requests
""" Need to install pip install python-dotenv """
from dotenv import load_dotenv
from data_manager import DataManager

load_dotenv("files/data.env")

api_key = getenv("API_KEY")
api_endpoint = getenv("API_ENDPOINT_QUERY")

headers = {
            "apikey": api_key
        }


class FlightSearch:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager
        self.iata_codes = []

    def get_iata_codes(self):
        for city in self.data_manager.get_city_names():
            response = requests.get(url=api_endpoint, params={"term": city},
                                    headers=headers).json()["locations"][0]["code"]
            self.iata_codes.append(response)
        return self.iata_codes





