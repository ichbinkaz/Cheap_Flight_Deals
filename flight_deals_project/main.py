from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from users_management import UserBrain

data_manager = DataManager()
flight_search = FlightSearch(data_manager)
iata_codes = flight_search.get_iata_codes()
data_manager.fill_codes(iata_codes)

flight_data = FlightData(flight_search)
users_management = UserBrain()
notification_manager = NotificationManager(flight_data, users_management)
notification_manager.check_prices(data_manager.get_prices())



