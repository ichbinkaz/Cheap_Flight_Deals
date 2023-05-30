import os

from flight_search import FlightSearch
import datetime
import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv("files/data.env")

api_key = getenv("API_KEY")
api_endpoint = getenv("API_ENDPOINT_SEARCH")

headers = {
    "apikey": api_key
}


class FlightData:
    def __init__(self, flight_search: FlightSearch):
        self.flight_search = flight_search
        self.now = datetime.datetime.now()
        self.date_tomorrow = datetime.datetime(self.now.year, self.now.month, self.now.day + 1).strftime("%d/%m/%Y")
        self.prices = []
        self.flight_info = []
        self.departure_airport_code = "BUD"

    def get_prices(self):
        print(self.now)
        print(self.calcualte_time())
        print(self.flight_search.iata_codes)
        for code in self.flight_search.iata_codes:

            response = requests.get(url=api_endpoint, params={"fly_from": self.departure_airport_code,
                                                                  "fly_to": code,
                                                                  "date_from": self.date_tomorrow,
                                                                  "date_to": self.calcualte_time(),
                                                                  "curr": "EUR",
                                                                  "nights_in_dst_from": 7,
                                                                  "nights_in_dst_to": 28,
                                                                  "flight_type": "round",

                                                                  },
                                        headers=headers).json()["data"][0]

            self.prices.append(response["price"])
            print(code)
            print(self.prices)
            flight_details = {"cityFrom": response['route'][0]['cityFrom'],
                              "flyFrom": response["route"][0]["flyFrom"],
                              "cityTo": response["route"][0]["cityTo"],
                              "fly_to": response["route"][0]["flyTo"],
                              "price": response["price"],
                              "out_local_departure_date": response["route"][0]["local_departure"].split("T")[0],
                              "return_local_departure_date": response["route"][1]["local_departure"].split("T")[0]}

            self.flight_info.append(flight_details)
        print(self.flight_info)
        return self.prices

    def calcualte_time(self):
        for i in range(self.now.month, self.now.month+6):
            date_in_six_months = datetime.datetime(self.now.year, i, self.now.day).strftime("%d/%m/%Y")
        return date_in_six_months




