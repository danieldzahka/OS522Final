"""
io_bound_seq.py : io_bound program

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


if __name__ == "__main__":
	print("Duplicating Files...")
	start = time.time()
	duplicate_file("../text/operating_system-syscalls.txt", "../text/copy1.txt")
	duplicate_file("../text/operating_system-syscalls_copy.txt", "../text/copy2.txt")
	end = time.time()
	print("Done...")
	print(end - start)
