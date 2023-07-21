from celery import Celery
from csv_controller import process_csv

# Create a Celery application instance
app = Celery(
    "csv_procesor", broker="redis://redis:6379/0", backend="redis://redis:6379/0"
)


@app.task
def process_csv_task(input_file, output_file):
    return process_csv(input_file, output_file)
