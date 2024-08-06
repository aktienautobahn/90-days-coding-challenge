from email.base64mime import body_encode
from flight_data import FlightData
from email.mime.text import MIMEText
import smtplib


MY_EMAIL = ""
MY_PASSWORD = ""
SEND_TO = ""


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def wished_price(self, min_price,wished_price):
        if min_price <= wished_price:
            return True

    def send_email(self, results:FlightData):

        href = MIMEText(f'<a href="{results.deep_link}">Book here</a>','html')
        body = f"Low price alert! Only €{results.fair_price} (+€{results.bag_price} for baggage) to fly from {results.origin_city}-{results.origin_airport} to {results.destination_city}-{results.destination_airport}, from {results.out_date} to {results.in_date}, for {results.nights_in_dest} days."
        if results.stop_overs_number > 0:
            if results.stop_overs_number > 1:
                body +=f"\nFlight have {results.stop_overs_number} stop overs, via {', '.join(map(str, results.stop_over_cities))}."
            else:
                body +=f"\nFlight has {results.stop_overs_number} stop over, via {', '.join(map(str, results.stop_over_cities))}."

        link = f"https://www.google.de/flights?hl=en#flt={results.origin_airport}.{results.destination_airport}.{results.out_date}*{results.destination_airport}.{results.origin_airport}.{results.in_date}"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                                from_addr=MY_EMAIL,
                                to_addrs=SEND_TO,
                                msg=f"Subject:New Low Price Flight!\n\n{body}\n\n{href}".encode('utf-8')
                                )

