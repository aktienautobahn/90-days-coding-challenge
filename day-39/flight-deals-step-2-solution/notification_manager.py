class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def wished_price(self, min_price, wished_price):
        if min_price < wished_price:
            return True