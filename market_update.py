import time
from datetime import datetime
from bitcoin_helper import BitcoinPrice, IFTTTNotifier, Timer


BITCOIN_PRICE_EMERGENCY = 100000


def main():

    while True:
        price = BitcoinPrice()   #create an instace of the Bitcoinprice() class

        price = price.get_bitcoin_price()   #call the get_bitcoin_price method on the instance

        current_time = datetime.now().strftime('%a %I:%M %p')   #pass the current time into a variable

        if price > BITCOIN_PRICE_EMERGENCY:
            sent_notification = 'emergency_notfication'
        else:
            sent_notification = 'price_notification'

        Notfiy_Me = IFTTTNotifier()   #create an instance of the IFTTNotifier() class

        #call the send_price_notifcation() method and pass in the name of the event, price, and current_time
        Notfiy_Me.send_price_notification(sent_notification, price, current_time)

        send_review = Timer(20)
        if send_review.time_elapsed() == True:
            Notfiy_Me.send_price_notification(sent_notification, price, current_time) 


if __name__ == '__main__':
    main()
