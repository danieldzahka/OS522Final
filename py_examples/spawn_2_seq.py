"""
spawn_2.py : Runs two CPU bound functions sequentially

Daniel Zahka ~ daniel.zahka@wustl.edu
Anish Naik ~ anish.r.naik@wustl.edu
"""

def thread_func():
        for i in xrange(1, 50000000):
                k = i * 3


if __name__ == "__main__":
    print("Starting work...")
    thread_func()
    thread_func()
    print("Done...")
