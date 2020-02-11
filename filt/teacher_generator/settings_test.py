import os

from teacher_generator.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


CELERY_ALWAYS_EAGER = True
CELERY_TASK_ALWAYS_EAGER = True
