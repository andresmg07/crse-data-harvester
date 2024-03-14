import schedule


def schedule_job(job, job_params, time, timezone):
    """
    Procedure that schedules a given job every workday monday-friday at a given time in a given timezone
    :param job: Procedure that executes at the scheduled times
    :param job_params: parameters dict passed to the given job
    :param time: hour of execution on a 24 hrs basis
    :param timezone: timezone identifier used to schedule the given job, identifiers can be found at https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
    :return: None
    """
    schedule.every().monday.at(time, timezone).do(job, **job_params)
    schedule.every().tuesday.at(time, timezone).do(job, **job_params)
    schedule.every().wednesday.at(time, timezone).do(job, **job_params)
    schedule.every().thursday.at(time, timezone).do(job, **job_params)
    schedule.every().friday.at(time, timezone).do(job, **job_params)
