"""
Lock and RLock are two of the basic tools used in threaded programming to prevent race conditions.
There are a few other that work in different ways. Before you look at them,
let’s shift to a slightly different problem domain.
"""


import threading

l = threading.Lock()  # program stucks
# l = threading.RLock()  # multiple acquire

print("before first acquire")
l.acquire()
print("before second acquire")
l.acquire()
print("acquired lock twice")
l.release()
