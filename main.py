import time
import schedule
from web_scraper import Alert

print("Enter the email address where you want to receive the notification.")
email = str(input("Email: "))

print("Enter the link where you want to monitor.")
link = str(input("Link: "))

schedule.every(10).seconds.do(Alert,email,link)

while True:
    schedule.run_pending()
    time.sleep(1)