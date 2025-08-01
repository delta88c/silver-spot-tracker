from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from datetime import datetime

from config import METALS_API_KEY, FROM_EMAIL, EMAIL_PW, TO_EMAIL, TIMEZONE
from fetch_price import get_silver_spot_price
from db import init_db, save_price
from email_utils import send_email
from report import generate_report

def daily_task():
    try:
        # Fetch and store price
        price, ts = get_silver_spot_price(METALS_API_KEY)
        date_str = ts.strftime("%Y-%m-%d")
        save_price(date_str, price)
        # Generate and send report
        body = generate_report()
        subject = "Daily Silver Spot Price Update"
        send_email(subject, body, TO_EMAIL, FROM_EMAIL, EMAIL_PW)
        print(f"Email sent: {subject} at {datetime.now()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    init_db()
    scheduler = BlockingScheduler(timezone=pytz.timezone(TIMEZONE))
    # Schedule for 07:00 CDT (America/Chicago)
    scheduler.add_job(daily_task, CronTrigger(hour=7, minute=0))
    print("Scheduler started, waiting for next run...")
    scheduler.start()
