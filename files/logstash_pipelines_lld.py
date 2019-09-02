#!/bin/python3
"""

Get pipeline stats from logstash

"""

import urllib.request 
import json 

with urllib.request.urlopen("http://localhost:9600/_node/stats/pipelines") as url:
   data = json.loads(url.read().decode())

res = []

for (pipeline, pstats) in data["pipelines"].items():

   if "." in pipeline:
      continue
   res.append({"{#PIPELINE}": pipeline})

print("- ls_pipelines", json.dumps({"data" : res}))
