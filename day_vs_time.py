#!/usr/bin/env python
"""
Takes a JSON list of scrobbles from the input file arguments. The JSON format
is as found from the Last.FM api.
Plots a pretty graph of each file's scrobbles using matplotlib, overlaid on top
of each other.
"""
import sys
import json
import matplotlib.pyplot as plt
from datetime import datetime

if len(sys.argv) <= 1:
    print "Usage: python day_vs_time.py <scrobbles.json> ..."
    sys.exit(1)


fig = plt.figure()
subplot = fig.add_subplot(111)
subplot.set_ylim(24, 0)
subplot.set_yticks(range(0,24))
subplot.set_ylabel("Hours since midnight")
subplot.set_xlabel("Date of scrobble")
subplot.set_title("Last.FM scrobbles for " + sys.argv[1])

colors = ['b','g','r','c','m']

for filename in sys.argv[1:]:
    dates = []
    times = []

    f = open(filename)
    scrobbles = json.load(f)

    for scrobble in scrobbles:
        dt = datetime.fromtimestamp(float(scrobble['date']['uts']))
        dates.append(dt.date())
        times.append(dt.hour + dt.minute/60.0)

    color = colors.pop()
    print color
    subplot.scatter(dates, times, color=color)

plt.show()
