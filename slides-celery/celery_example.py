from celery import Celery

app = Celery(
    'tasks',
    broker='redis://localhost:6379/1',
    backend='redis://'
)


# Decorator creates a Celery task from a regular function
@app.task
def add(x, y):
    return x + y
