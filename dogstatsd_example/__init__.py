__version__ = '0.1.0'
from datadog import initialize, statsd
import time 
import random

options = {
    "statsd_host": "127.0.0.1",
    "statsd_port": 8125,
}

initialize(**options)

def cli():
    i = 0
    while(1):
      i += 1
      statsd.set('example_metric.set', i, tags=["environment:dev"])
      print(f"sending metric {i} ")
      time.sleep(random.randint(0, 10))
    
