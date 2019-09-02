#!/bin/python3
"""

Get pipeline stats from logstas

"""

import urllib.request 
import json 

with urllib.request.urlopen("http://localhost:9600/_node/stats/pipelines") as url:
   data = json.loads(url.read().decode())

res = []

for (pipeline, pstats) in data["pipelines"].items():

   if "." in pipeline:
      continue
   if pstats["queue"]["type"] == "persisted":
      res.append({"{#QUEUE}": pipeline})

print("- ls_queues", json.dumps({"data" : res}))
