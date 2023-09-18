# _celery.py
from celery import Celery 
from celery.schedules import crontab

'''
For redis server install docker and run "docker run -d -p 6379:6379 redis" 
or use included docker file.
''' 

# Config Celery
app = Celery('celery_scheduler', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0', include=['tasks',])

# Change timezone from UTC 
app.conf.timezone = 'America/New_York'
# Enable task acknowledgment and track started tasks
app.conf.task_acks_late = True 
app.conf.task_track_started = True

app.conf.beat_schedule = {
    'run_diskSpaceManagement': {
        'task': 'run_diskSpaceManagement',
        'schedule': crontab(minute=0, hour='*/3'),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },

    'run_ScriptTracker': {
        'task': 'run_ScriptTracker',
        'schedule': crontab(minute=1, hour=7),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }
    },

    'run_DailyPubLog': {
        'task': 'run_DailyPubLog',
        'schedule': crontab(minute=0, hour=7),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }
    },

    'run_JapanETL': {
        'task': 'run_JapanETL',
        'schedule': crontab(minute=45, hour=6),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },
     
    'run_ThailandETL': {
        'task': 'run_ThailandETL',
        'schedule': crontab(minute=6, hour=6),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },

    'run_MauritiusETL': {
        'task': 'run_MauritiusETL',
        'schedule': crontab(minute=6, hour=6),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },

    'run_MacaoETL': {
        'task': 'run_MacaoETL',
        'schedule': crontab(minute=6, hour=6),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },

    'run_IsraelETL': {
        'task': 'run_IsraelETL',
        'schedule': crontab(minute=6, hour=6),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },

    'run_IndonesiaETL': {
        'task': 'run_IndonesiaETL',
        'schedule': crontab(minute=6, hour=6),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },

    'run_CzechRepublicETL': {
        'task': 'run_CzechRepublicETL',
        'schedule': crontab(minute=5, hour=6),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },

    'run_ArgentinaETL': {
        'task': 'run_ArgentinaETL',
        'schedule': crontab(minute=4, hour=6),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },

    'run_ItalyIstatETL': {
        'task': 'run_ItalyIstatETL',
        'schedule': crontab(minute=3, hour=6),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },

    'run_FranceCustomsETL': {
        'task': 'run_FranceCustomsETL',
        'schedule': crontab(minute=2, hour=6),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },

    'run_FinlandScrape': {
        'task': 'run_FinlandScrape',
        'schedule': crontab(minute=1, hour=6),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },

    'run_ITC_Availability': {
        'task': 'run_ITC_Availability',
        'schedule': crontab(minute=0, hour=4),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }        
    },

    'run_JetroAvailability': {
        'task': 'run_JetroAvailability',
        'schedule': crontab(minute=0, hour=4),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }        
    },

    'run_UN_Comtrade_ETL': {
        'task': 'run_UN_Comtrade_ETL',
        'schedule': crontab(minute=0, hour=4),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }        
    },

    'run_DashesInDB3': {
        'task': 'run_DashesInDB3',
        'schedule': crontab(minute=0, hour=3),
        # 'schedule': 30.0,
        'args': (),
        'options': {
            'max_instances': 1
        }

    },
    
}


