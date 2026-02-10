import logging
import requests
from dotenv import load_dotenv
from tiktok_dload import download_tiktok_video
import os
import json
import asyncio

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
    updateID = []

    if os.path.exists("updateID.txt"):
        with open("updateID.txt", "r") as f:
            updateID = f.read().splitlines()
    else:
        updateID = []

    print(f"updateIDs {updateID}")
    #with open("update.json", "w") as f:
    #    json.dump(update, f)

    #print(update.keys())
    
    #print(update.values())
    print("------------------------------")
    
    if str(update['result'][-1]['update_id']) not in str(updateID):
        print("There are new updates")
        print(f"UpdateID: {update['result'][-1]['update_id']}")
        for result in update['result']:
            if result['update_id'] not in updateID:
                print(f"UpdateID: {result['update_id']} | From: {result['message']['from']['username']} Message: {result['message']['text']}")
                updateID.append(result['update_id'])

                tiktok_url = str(result['message']['text'])
                if tiktok_url.startswith("https://vt.tiktok"):
                    print(f"Downloading Tiktok Video...")
                    asyncio.run(download_tiktok_video(tiktok_url))
                else:
                    print(f"Not a TikTok URL: {tiktok_url}")


    else:
        print("No new updates")
    #print(f"UpdateID: {update['result'][0]['update_id']} | From: {update['result'][0]['message']['from']['username']} Message: {update['result'][0]['message']['text']}")
    #print(f"UpdateID: {update['result'][1]['update_id']} |From: {update['result'][1]['message']['from']['username']} Message: {update['result'][1]['message']['text']}")
    #print("------------------------------")



    with open("updateID.txt", "w") as f:
        for id in updateID:
            f.write(f"{id}\n")


if __name__ == "__main__":
    main()
