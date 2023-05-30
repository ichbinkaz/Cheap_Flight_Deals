
import json

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, ):
        self.city_names = []

    def get_city_names(self):
        #sheety_data = requests.get(url=api_endpoint).json()["prices"]
        #self.city_names = [sheety_data[row]["city"] for row in range(len(sheety_data))]
        with open("files/flight_deals.json", "r") as data:
            flight_deals = json.load(data)
            self.city_names = [flight_deals[row]["city"] for row in range(len(flight_deals))]

        return self.city_names

    def get_prices(self):
        with open("files/flight_deals.json", "r") as data:
            flight_deals = json.load(data)
            self.city_prices = [flight_deals[row]["lowestPrice"] for row in range(len(flight_deals))]

        return self.city_prices

    def fill_codes(self, codes):
        with open("files/flight_deals.json", "r") as data:
            flight_deals = json.load(data)
            for row in range(len(flight_deals)):
                if flight_deals[row]["iataCode"] == '':
                    flight_deals[row]["iataCode"] = codes[row]
                    with open("files/flight_deals.json", "w") as data:
                        json.dump(flight_deals, data)
                else:
                    print("The rows are already filled in")
                    break
            return flight_deals




