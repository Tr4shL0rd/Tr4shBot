from urllib.parse import urlencode, urlparse, urlunparse
import time
import os
import requests
from dotenv import load_dotenv
load_dotenv()

class Giphy:
    def __init__(self, search="search") -> None:
        self.search = search
        self.API_KEY = os.getenv("giphy_API_KEY")
        self.random_id = requests.get(f"http://api.giphy.com/v1/randomid?api_key={self.API_KEY}", timeout=1).json()["data"]["random_id"]
        self.gif_search_url = f"http://api.giphy.com/v1/gifs/search?api_key={self.API_KEY}&q={self.search}&random_id={self.random_id}"
        self.sticker_search_url = f"http://api.giphy.com/v1/stickers/search?api_key={self.API_KEY}&q={self.search}&random_id={self.random_id}"
        self.unix_timestamp = int(time.time()) * 1000


    def handle_analytics(self,analytics, analytics_payload, random_id, unix_timestamp):
        onsent  = [analytics["onsent"]["url"],"SENT"]
        
        params = {
            "ts": unix_timestamp,
            "action_type": onsent[1],
            "analytics_response_payload": analytics_payload,
            "random_id": random_id
        }
        query_string = urlencode(params)
        parsed_url = urlparse(onsent[0])
        new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, query_string, parsed_url.fragment))
        requests.get(new_url, timeout=1)

    def get_gif(self):
        gif_resp = requests.get(self.gif_search_url, timeout=1).json()
        data = gif_resp["data"]
        gif_url = data[0]["url"]
        
        analytics = data[0]["analytics"]
        analytics_payload = data[0]["analytics_response_payload"]
        self.handle_analytics(analytics, analytics_payload, self.random_id, self.unix_timestamp)

        return gif_url

    def get_sticker(self):
        sticker_resp = requests.get(self.sticker_search_url, timeout=1).json()
        analytics = sticker_resp["data"][0]["analytics"]
        analytics_payload = sticker_resp["data"][0]["analytics_response_payload"]
        self.handle_analytics(analytics, analytics_payload, self.random_id, self.unix_timestamp)

        
        data = sticker_resp["data"]
        sticker_url = data[0]["url"]
        return sticker_url