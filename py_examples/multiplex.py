"""
multiplex.py : Uses threading module to emulate "poll" like
behavior

Daniel Zahka ~ daniel.zahka@wustl.edu
Anish Naik ~ anish.r.naik@wustl.edu
"""

import os, sys
import threading
import time

path = "tempfifo"

def read_fifo():
	with open(path, 'r') as fifo:
		print("Waiting for input...")
		line = fifo.read()
		print(line)
	return

def cpu_bound():
	t = threading.currentThread()
	while getattr(t, "do_run", True):
		#do nothing
		i = 1
	return

	
if __name__ == "__main__":
	try:
		os.mkfifo(path , 0644)
	except:
		print("failed to make fifo")

	t1 = threading.Thread(target=read_fifo, name="read_fifo")
	t2 = threading.Thread(target=cpu_bound, name="cpu_bound")
	print("Spawning Threads...")
	t1.start()
	t2.start()
	t1.join()
	t2.do_run = False
	t2.join()
	print("Joined Threads...")
	os.remove(path)
