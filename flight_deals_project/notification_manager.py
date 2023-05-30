from flight_data import FlightData
from users_management import UserBrain
from os import getenv
from dotenv import load_dotenv
import telegram
import asyncio

load_dotenv("files/data.env")
bot_token = getenv("BOT_TOKEN")
bot = telegram.Bot(token=bot_token)


class NotificationManager:
    def __init__(self, flight_data: FlightData, users_management: UserBrain):
        self.flight_data = flight_data
        self.user_management = users_management

    async def send_message(self, message):
        for user_index in range(len(self.user_management.get_users())):
            print(f"Sending message: {message}")
            await bot.send_message(chat_id=self.user_management.users[user_index]["chat_id"], text=message)
            print("Message sent!")

    def check_prices(self, prices):
        new_prices = self.flight_data.get_prices()
        flight_info = self.flight_data.flight_info

        for flight_index in range(len(flight_info)):
            for price in range(len(prices)):
                if new_prices[price] < prices[price]:
                    if flight_info[flight_index]["price"] == new_prices[price]:
                        message = f"Low price alert! Only {flight_info[flight_index]['price']}€," \
                                  f" to fly from {flight_info[flight_index]['cityFrom']}-{flight_info[flight_index]['flyFrom']}" \
                                  f" to {flight_info[flight_index]['cityTo']}-{flight_info[flight_index]['fly_to']}," \
                                  f" from {flight_info[flight_index]['out_local_departure_date']}" \
                                  f" to {flight_info[flight_index]['return_local_departure_date']}, Check out this offer at Kiwi.com"

                        asyncio.run(self.send_message(message))


















