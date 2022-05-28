# from app import create_app, db
#
# app = create_app()

from schedule import repeat, every, run_pending
import time


@repeat(every(5).seconds)
def job():
    print("I'm Working")


# schedule.every(3).seconds.do(job)

while True:
    run_pending()
    time.sleep(1)
