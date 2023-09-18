# run_celery.py
import subprocess
from celery import Celery 
from celery.schedules import crontab
import multiprocessing
from celery.utils import uuid
from celery.exceptions import Reject
import redis 
import os
import sys
from _celery import app
# All these commands must be executed in the dir above celery-scheduler

# Starts celery beat
# celery -A celery-scheduler beat

# Starts a single threaded worker, only one that has worked on windows
# celery -A celery-scheduler worker --pool=solo -l info 

# Clears celery beat task queue
# celery -A celery-scheduler purge -f

def verify_redis_running():
    # Connect to Redis instance
    redis_client = redis.StrictRedis(host='localhost', port=6379)
    # Ping
    response = redis_client.ping()
    return response

def check_redis_queue():
    """
    Checks Redis Queue and returns queue length
    """
    # Connect to Redis instance 
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    # Get the current queue length 
    queue_length = redis_client.llen('celery')
    # Get the list of tasks in the Celery queue
    queue_tasks = redis_client.lrange('celery', 0, -1)
    # Decode the task information
    decoded_tasks = [task.decode('utf-8') for task in queue_tasks]
    print(f'Queue Length: {queue_length}')

def check_celery_queue():
    """
    Checks Celery Queue and returns active, scheduled, and reserved queues
    """
    inspector = app.control.inspect()
    active = inspector.active()
    scheduled = inspector.scheduled()
    reserved = inspector.reserved()
    
    # print(active, scheduled, reserved)
    return active, scheduled, reserved

def purge_celery_queue():
    """
    Clears Celery Queue
    """
    app.control.purge()

def start_celery_beat():
    '''
    Begins celery beat
    '''
    app.Beat(loglevel='debug').run()

def start_worker():
    '''
    Begins celery worker
    '''
    argv = [
        'worker', 
        '--pool=solo',
        # '-l', 
        # 'info'
        '-f', 
        'celery.log'
    ]
    app.worker_main(argv)

def start_celery_flower():
    ''''
    Runs a monitoring dashboard for celery workers
    '''
    subprocess.call(['celery', '-A', 'celery_scheduler', 'flower'], shell=True)

if __name__ == '__main__':

    # Create processes 
    celery_beat_proc = multiprocessing.Process(target=start_celery_beat)
    celery_worker_proc1 = multiprocessing.Process(target=start_worker)
    # celery_worker_proc2 = multiprocessing.Process(target=start_worker)   
    celery_flower_proc = multiprocessing.Process(target=start_celery_flower)


    # Start the processes
    celery_beat_proc.start()
    celery_worker_proc1.start()
    # celery_worker_proc2.start()
    celery_flower_proc.start()


    # Wait for the processes to finish
    celery_beat_proc.join()
    celery_worker_proc1.join()
    # celery_worker_proc2.join()
    celery_flower_proc.join()

