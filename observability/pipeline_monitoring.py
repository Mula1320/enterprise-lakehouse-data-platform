import datetime

def log_pipeline_status(layer, status):
    print(f"{datetime.datetime.now()} - {layer} layer status: {status}")
