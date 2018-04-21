"""
spawn_2.py : Runs two CPU bound functions sequentially

Daniel Zahka ~ daniel.zahka@wustl.edu
Anish Naik ~ anish.r.naik@wustl.edu
"""

import time

def thread_func():
        for i in xrange(1, 500000000):
                k = i * 3


if __name__ == "__main__":
    print("Spawning Threads...")
    start = time.time()
    thread_func()
    thread_func()
    end = time.time()
    print("Joined Threads...")
    print(end - start)
