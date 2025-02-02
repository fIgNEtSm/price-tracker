from smtplib import SMTP
import os

SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

def send_msg(to_email, msg):
    message = msg
    with SMTP(host=SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject:AMAZON PRICE TRACKER\n\n{message}".encode())
