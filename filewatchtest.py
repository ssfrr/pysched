#! /usr/bin/python

from pysched import Scheduler
from filewatcher import FileWatcher

print """

This script creates two FileWatcher processes, each watching for one file. 
The files watched for are called "file1" and "file2".

The scheduler will execute the appropriate process if one of the 2 files
are created. After both processes have excuted the scheduler will exit.

"""

sched = Scheduler()
proc1 = FileWatcher("proc1", "file1")
proc2 = FileWatcher("proc2", "file2")

sched.add_process(proc1)
sched.add_process(proc2)

while not sched.finished():
	sched.check_events()
	sched.run_next()
