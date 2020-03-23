import requests
from passwords import TOKENS
import time


key = TOKENS()

class BitcoinPrice:
    # set bit_api_url as a protected attribute
    __bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'

    def get_bitcoin_price(self):
        price = requests.get(self.__bitcoin_api_url).json()  #create a request to the coin marketmarket API
        return round(float(price[0]['price_usd']), 2)  #retrieve the price_usd key and round the value given


class IFTTTNotifier:
    #Here we use the maker.IFTT service to make a request which triggers a notfication action
    __web_request_url = 'https://maker.ifttt.com/trigger/{}/with/key/{}'

    def send_price_notification(self, event_name, value, current_time):
        __web_request_url = self.__web_request_url.format(event_name, key.IFTTT_key)  #pass the event name into request url
        data = {"value1": value, "value2": current_time}  #IFTT allows you send a json place holder values with your request
        requests.post(__web_request_url, data)  #make request with url variable and json data


class Timer:
    def __init__(self, elapsed_time):
        self.start = round(time.perf_counter())
        self.elapsed_time = 60 * elapsed_time
    
    def time_elapsed(self):
        if self.elapsed_time > self.start:
            return True 

