#!/bin/python3

import math
import os
import random
import re
import sys
import dateutil.parser
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def time_delta():
    data = request.data.decode("utf-8")
    processedData = data.split("\n")
    n = int(processedData[0]);
    i = 1;
    result = []
    for t_itr in range(n):
        date1 = dateutil.parser.parse(processedData[i], fuzzy=True)
        date2 = dateutil.parser.parse(processedData[i+1], fuzzy=True)
        i = i+2
        diff = date2 - date1
        result.append(str(int(abs(diff.total_seconds()))))
    return json.dumps(result)

if __name__ == '__main__':
    app.run()
