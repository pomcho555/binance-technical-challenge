import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from threading import Thread

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import Gauge, generate_latest

from questions.question5 import print_spread_each_symbol

app = FastAPI()

INTERVAL = 10
MAX_WORKERS = 2


SPREADS_GAUGE = Gauge("spreads_10s", "Description of gauge", ["symbol", "filed"])


def scheduler():
    # create instances each symbols
    base_timing = datetime.now()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while True:
            future = executor.submit(print_spread_each_symbol)  # noqa
            current_timing = datetime.now()
            elapsed_sec = (current_timing - base_timing).total_seconds()
            sleep_sec = INTERVAL - (elapsed_sec % INTERVAL)
            result = future.result(timeout=5)
            for s in result:
                SPREADS_GAUGE.labels(s, "spread").set(result[s]["spread"])
                SPREADS_GAUGE.labels(s, "delta").set(result[s]["delta"])
            # logger.info(f"Collecting timestamp: {current_timing}")
            time.sleep(max(sleep_sec, 0))


def infinite_loop():
    scheduler()


# Separate event-loop from ASGI server
thread = Thread(target=infinite_loop, args=(), kwargs={})
thread.daemon = True
thread.start()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return generate_latest()
