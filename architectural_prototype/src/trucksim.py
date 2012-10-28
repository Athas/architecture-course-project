#!/usr/bin/env python

import time
import random
import threading
import httplib
import json
import urllib

global biglock
biglock = threading.RLock()
global sts_host
sts_host = "localhost:5000"

class Truck:
    def __init__(self, ident):
        self.messages = {}
        self.reading_interval = 2.0
        self.ident = ident
        self.location = (0,0)
        self.ancient = {} # The oldest acceptable timestamps from other trucks.
        self.gpsReading()

    def addTruckPosition(self, truck, time, pos):
        if truck in self.messages:
            self.messages[truck][time] = pos
        else:
            self.messages[truck] = {time: pos}

    def gpsReading(self):
        with biglock:
            x,y = self.location
            self.location = (x + random.random(), y + random.random())
            self.addTruckPosition(self.ident, time.time(), self.location)
            threading.Timer(self.reading_interval, self.gpsReading).start()

    def meet(self, other):
        added = {}
        for frm in other.messages:
            for time in other.messages[frm]:
                if frm in self.ancient and self.ancient[frm] > time:
                    # That message is too old, discard it.
                    continue
                if frm in added:
                    added[frm] = max(added[frm], time)
                else:
                    added[frm] = time
                    self.addTruckPosition(frm, time, other.messages[frm][time])
        for frm in added:
            # Don't keep any messages older than the youngest message we just received.
            self.ancient[frm] = added[frm]

    def offload(self):
        print "sending", self.messages
        conn = httplib.HTTPConnection(sts_host)
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        conn.request("POST", "/data", json.dumps(self.messages), headers)
        resp = conn.getresponse()
        if resp.status == httplib.OK:
            reply = resp.read()
            print reply
        else:
            print "Got ", resp.status, resp.reason, "instead of OK"
        conn.close()
        self.messages = {}

class RoadNetwork:
    def __init__(self):
        self.trucks = []
        self.meeting_interval = 1.0
        self.offload_interval = 1.0
        self.arrangeMeeting()
        self.arrangeOffload()

    def arrangeMeeting(self):
        # Randomly arrange meeting between two trucks.  They don't
        # have to be near each other in this simulation.
        with biglock:
            if len(self.trucks) > 1:
                x = random.choice(self.trucks)
                y = random.choice(self.trucks)
                if x != y:
                    x.meet(y)
                    y.meet(x)
            threading.Timer(self.meeting_interval, self.arrangeMeeting).start()

    def arrangeOffload(self):
        with biglock:
            if len(self.trucks) > 0:
                random.choice(self.trucks).offload()
            threading.Timer(self.offload_interval, self.arrangeOffload).start()

    def addTruck(self, truck):
        self.trucks += [truck]

if __name__ == '__main__':
    roads = RoadNetwork()
    trucks = 100
    with biglock:
        for i in range(trucks):
            roads.addTruck(Truck(i))
    time.sleep(100)
