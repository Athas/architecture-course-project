#!/usr/bin/env python

import time
import random
import threading

global biglock
biglock = threading.RLock()

class Truck:
    def __init__(self, ident):
        self.messages = {}
        self.reading_interval = 2.0
        self.ident = ident
        self.location = (0,0)
        self.ancient = {} # The oldest acceptable timestamps from other trucks.
        self.gpsReading()

    def gpsReading(self):
        with biglock:
            x,y = self.location
            self.location = (x + random.random(), y + random.random())
            self.messages[(self.ident, time.time())] = self.location
            threading.Timer(self.reading_interval, self.gpsReading).start()

    def meet(self, other):
        added = {}
        for frm, time in other.messages:
            if frm in self.ancient and self.ancient[frm] > time:
                # That message is too old, discard it.
                continue
            if frm in added:
                added[frm] = max(added[frm], time)
            else:
                added[frm] = time
            self.messages[(frm,time)] = other.messages[(frm,time)]
        for frm in added:
            # Don't keep any messages older than the youngest message we just received.
            self.ancient[frm] = added[frm]

    def offload(self):
        # Where does it go?  We need to transmit to the STS here.
        self.messages = {}

class RoadNetwork:
    def __init__(self):
        self.trucks = []
        self.meeting_interval = 1.0
        self.offload_interval = 10.0
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