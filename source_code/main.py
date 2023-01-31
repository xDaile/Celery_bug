from celery import Celery


celery = Celery("example", broker="redis://localhost:6379/0")

#@celery.task
def example(
    param: str,
):
    """
    some docs
    """
    print(param)