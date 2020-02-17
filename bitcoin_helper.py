import requests
from passwords import TOKENS

key = TOKENS()

class BitcoinPrice:
    # place the public coin market api in a variable
    BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
    def get_bitcoin_price(self):
        price = requests.get(self.BITCOIN_API_URL).json() #create a request to the coin marketmarket API
        return round(float(price[0]['price_usd']), 2) #retrieve the price_usd key and round the value given


class IFTTTNotifier:
    #Here we use the maker.IFTT serveice to make a request which triggers a notfication action
    webhook_url = 'https://maker.ifttt.com/trigger/{}/with/key/{}'
    def send_price_notification(self, event_name, value, current_time):
        webhook_url = self.webhook_url.format(event_name, key.IFTTT_key) #pass the event name into request url
        data = {"value1": value, "value2": current_time} #IFTT allows you send to json place holder values with your request
        requests.post(webhook_url, data) #make request with url variable and json data