#!/bin/python3
"""

Get pipeline stats from logstas

"""

import urllib.request 
import json 

with urllib.request.urlopen("http://localhost:9600/_node/stats/pipelines") as url:
   data = json.loads(url.read().decode())

for (pipeline, pstats) in data["pipelines"].items():

   if "." in pipeline:
      continue
   print("-", "ls.pipe.in[" + pipeline + "]", pstats["events"]["in"])
   out = 0
   for output in pstats["plugins"]["outputs"]:
      if output["name"] == "elasticsearch":
         out += output["events"]["out"]
   print("-", "ls.pipe.out[" + pipeline + "]", out)
   if pstats["queue"]["type"] == "persisted":
      print("-", "ls.pipe.queue[" + pipeline + "]", pstats["queue"]["events"])
