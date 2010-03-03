#! /usr/bin/python

# Copyright 2010 Spencer Russell
# 
# This file is part of pysched.
# 
# pysched is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# pysched is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with pysched.  If not, see <http://www.gnu.org/licenses/>.


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
