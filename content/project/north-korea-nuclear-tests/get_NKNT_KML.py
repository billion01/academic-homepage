#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
import simplekml

Event = namedtuple('Event', ['id', 'date', 'time', 'latitude', 'longitude', 'depth'])

events = []
with open("NKNT.dat", "r") as fin:
    for line in fin:
        if line.startswith('#'):
            continue
        events.append(Event(*line.split()))

kml = simplekml.Kml()
for event in events:
    point = kml.newpoint(name=None)
    point.coords = [(event.longitude, event.latitude)]
    point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle_highlight.png'
    point.name = event.date
    description = "<p><b>Origin</b>: {}T{}</p>".format(event.date, event.time)
    description += "<p><b>Burial Depth</b>: {} m</p>".format(event.depth)

    point.description = description

kml.save("NKNT.kml")
