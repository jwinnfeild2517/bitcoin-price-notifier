import time
from datetime import datetime
from bitcoin_helper import BitcoinPrice, IFTTTNotifier


def main():
    bitcoin_history = []
    while True:
        price = BitcoinPrice() #create an instace of the Bitcoinprice() class
        price = price.get_bitcoin_price() #call the get_bitcoin_price method on the instance

        current_time = datetime.now().strftime('%a %I:%M %p') #pass the current time into a variable

        notfiy_me = IFTTTNotifier() #create and instance of the IFTTNotifier() class
        notfiy_me.send_price_notification('price_notification', price, current_time) #call the send_price_notifcation() method and pass in the name of the event, price, and current_time

        time.sleep(5 * 60) #sleep for 5 mins before send another notification


if __name__ == '__main__':
    main()

