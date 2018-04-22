"""
spawn_2_multiprocessing.py : Spawns two multiprocessing cpu bound threads,
uses Queue to demonstrate IPC going on underneath the hood...

Daniel Zahka ~ daniel.zahka@wustl.edu
Anish Naik ~ anish.r.naik@wustl.edu
"""

import multiprocessing

def process_func1(q):
	q.put(["Sending", 1, "Message"])
	for i in xrange(1, 50000000):
		k = i * 3


def process_func2(q):
	for i in xrange(1, 50000000):
		k = i * 3
	q.put(["process func 2 is done"])		

if __name__ == "__main__":
	q = multiprocessing.Queue()
	p1 = multiprocessing.Process(target=process_func1, args=(q,))
	p2 = multiprocessing.Process(target=process_func2, args=(q,)) 
	print("Spawning Processes...")
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	print("Joined Processes...")
	print(q.get())
	print(q.get())
