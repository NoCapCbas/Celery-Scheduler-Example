
# Celery Scheduler for Batch File Automation

This project utilizes Celery, a distributed task queue, to automate recurring batch file executions. It relies on a Redis instance running on localhost to manage the task queue.

## Prerequisites

- Python 3.x
- Docker (if you want to run Redis via Docker)

## Setting Up Redis

If you don't have a Redis instance running, you can use Docker to quickly set one up:

```bash
docker run -d -p 6379:6379 redis
```

## Installing Dependencies

To install the required Python Packages, create a virtual environment and run:

```bash 
pip install -r requirements.txt
```

## Running celery_scheduler.py 

Navigate to directory with celery_scheduler.py and run the following command to begin celery scheduler:

```bash
celery_scheduler.py
```

### Adding Tasks

To add a task it must be added in both tasks.py and _celery.py 

### Running a task manually

Assuming celery_scheduler.py is already running a task can be ran manually within the directory with the following command:

```bash
celery -A celery_scheduler call example_task
```

If celery_scheduler.py is not running, a celery worker must be started to run the task. 

### Celery Flower Dashboard

Assuming celery_scheduler.py is running, Celery Flower Dashboard can be accessed at http://localhost:5555
