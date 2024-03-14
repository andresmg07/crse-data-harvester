import os
from datetime import date, timedelta
from data_acquisition import retrieve_current_session_data
import time
import schedule
from utils.job_util import schedule_job


def retrieve_session_job():
    start_date = date.today()
    end_date = date.today() + timedelta(1)
    retrieve_current_session_data(start_date, end_date)
    os.chdir("/".join(__file__.split("/")[0:-1]))


if __name__ == '__main__':
    schedule_job(retrieve_session_job, {}, "10:30", "America/Costa_Rica")
    while True:  # Keeps the program alive
        schedule.run_pending()  # Runs every job that was meant to be executed during a sleep
        time.sleep(600)  # Passive waiting
