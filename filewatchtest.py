#! /usr/bin/python

from pysched import Scheduler
from filewatcher import FileWatcher

sched = Scheduler()
proc1 = FileWatcher("proc1", "file1")
proc2 = FileWatcher("proc2", "file2")

sched.add_process(proc1)
sched.add_process(proc2)

while not sched.finished():
	sched.check_events()
	sched.run_next()
