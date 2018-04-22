"""
spawn_2_fork.py : Forks a new process to side step the GIL

Daniel Zahka ~ daniel.zahka@wustl.edu
Anish Naik ~ anish.r.naik@wustl.edu
"""

import os
import time

def work_func():
        for i in xrange(1, 50000000):
                k = i * 3


if __name__ == "__main__":
	print("Forking...")
	newpid = os.fork()
	if newpid == 0:
		#child
		work_func()
	else:
		#parent
		work_func()
		pid, status = os.waitpid(newpid, 0)
		print("Child and Parent Finished...")
