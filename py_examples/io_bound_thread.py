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
	t1args = ("../text/operating_system-syscalls.txt", "../text/copy1.txt")
	t2args = ("../text/operating_system-syscalls_copy.txt", "../text/copy2.txt")
	t1 = threading.Thread(target=duplicate_file, name="duplicate_t1", args = t1args)
	t2 = threading.Thread(target=duplicate_file, name="duplicate_t2", args = t2args)
	print("Duplicating Files...")
	start = time.time()
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	end = time.time()
	print("Done...")
	print(end - start)
