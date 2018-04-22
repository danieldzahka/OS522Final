"""
spawn_2.py : Spawns two native cpu bound threads

Daniel Zahka ~ daniel.zahka@wustl.edu
Anish Naik ~ anish.r.naik@wustl.edu
"""

import threading
import time

def thread_func():
        for i in xrange(1, 50000000):
                k = i * 3


if __name__ == "__main__":
    t1 = threading.Thread(target=thread_func, name="spawn_2_t1")
    t2 = threading.Thread(target=thread_func, name="spawn_2_t1")
    print("Spawning Threads...")
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print("Joined Threads...")
    print(end - start)

