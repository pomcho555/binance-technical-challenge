import logging
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime

from questions.question2 import fetch_top5_trades_symbols_with_specific_quote_asset
from questions.question4 import get_spread_each_symbols

logging.basicConfig()
logger = logging.getLogger(__name__)

INTERVAL = 10
MAX_WORKERS = 2

previous_spreads = {}


@dataclass
class Spread:
    symbol: str
    spread: float
    previous_spread: float = 0.0
    delta: float = 0.0

    def calculate_delta(self):
        self.delta = abs(self.spread - self.previous_spread)
        self.previous_spread = self.spread


def print_spread_each_symbol(symbols: list) -> dict:
    """Print a spread and delta on each symbol.

    Args:
        symbols (list): target symbols you want to calculate spread.
            e.g. ['LUNAUSDT', 'BTCUSDT', ... ]

    Returns:
        dict: Return output
            e.g. {'BTCUSDT': {'spread': 0.010000000002037268, 'delta': 0.010000000002037268},..}
    """

    spreads = get_spread_each_symbols(symbols)
    output = {s: {"spread": spreads[s], "delta": 0} for s in spreads.keys()}
    for s in spreads:
        if s not in previous_spreads:
            previous_spreads[s] = 0.0
        output[s]["delta"] = abs(previous_spreads[s] - spreads[s])
        previous_spreads[s] = spreads[s]

    print(output)
    return output


def scheduler():
    target_symbols = fetch_top5_trades_symbols_with_specific_quote_asset()
    # create instances each symbols
    base_timing = datetime.now()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while True:
            future = executor.submit(print_spread_each_symbol, target_symbols)  # noqa
            current_timing = datetime.now()
            elapsed_sec = (current_timing - base_timing).total_seconds()
            sleep_sec = INTERVAL - (elapsed_sec % INTERVAL)
            logger.info(f"Collecting timestamp: {current_timing}")
            time.sleep(max(sleep_sec, 0))


def print_answer():
    print("====Q5 ANSWER====")
    print("Stop a metrics emitting every 10 seconds with Ctrl+CEmit.")
    scheduler()
