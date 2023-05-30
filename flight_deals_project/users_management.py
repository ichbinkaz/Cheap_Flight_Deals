import json


class UserBrain:
    def __init__(self):
        self.users = []

    def get_users(self):
        with open("files/data.json", "r") as data_file:
            data = json.load(data_file)
            self.users = data
        return self.users

    def add_user(self):
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        chat_id = input("Enter your chat_id: ")
        new_data = {"name": name,
                    "surname": surname,
                    "chat_id": chat_id}
        try:
            with open("files/data.json", "r") as data_file:
                data = json.load(data_file)
                self.users = data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("files/data.json", "w") as data_file:
                print("yes")
                json.dump([new_data], data_file, indent=4)
        else:
            data.append(new_data)
            with open("files/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)





