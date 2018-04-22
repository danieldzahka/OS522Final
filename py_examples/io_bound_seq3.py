"""
io_bound_seq3.py : io_bound program

Daniel Zahka ~ daniel.zahka@wustl.edu
Anish Naik ~ anish.r.naik@wustl.edu
"""

import threading
import time

def duplicate_file(filename, outfile):
	with open(filename, 'r') as f:
		with open(outfile, 'w') as out:
			for line in f:
				out.write(line)

def busy_work():
        for i in xrange(1, 20000000):
                k = i * 3

if __name__ == "__main__":
	print("Duplicating Files...")
	start = time.time()
	duplicate_file("../text/operating_system-syscalls.txt", "../text/copy1.txt")
	busy_work()
	end = time.time()
	print("Done...")
	print(end - start)
