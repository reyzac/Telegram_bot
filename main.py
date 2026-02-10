import logging
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

logger = logging.getLogger(__name__ )


class TelegramAI:
    def __init__(self):
        self.telegram_token = os.getenv("TG_TOKEN")

    def GetUpdates(self):
        url = f"https://api.telegram.org/bot{self.telegram_token}/getUpdates"
        response = requests.get(url)
        return response.json()










def main():
    telegram = TelegramAI()
    update = telegram.GetUpdates()

    #with open("update.json", "w") as f:
    #    json.dump(update, f)

    #print(update.keys())
    print(update.values())
    print("------------------------------")
    print(f"From: {update['result'][0]['message']['from']['username']} Message: {update['result'][0]['message']['text']}")
    print(f"From: {update['result'][1]['message']['from']['username']} Message: {update['result'][1]['message']['text']}")



if __name__ == "__main__":
    main()
