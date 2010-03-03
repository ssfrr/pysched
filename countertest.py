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
from counters import Counter, SlowCounter
from timers import RelativeTimer

sched = Scheduler()
counter1 = SlowCounter("First", 9)
counter1.priority = 20
counter2 = SlowCounter("Second", 5)
counter2.priority = 50
counter3 = SlowCounter("Third", 13, 2)
counter3.priority = 10
counter4 = Counter("Fourth", 20)
counter4.priority = 20
counter4.wait(RelativeTimer(4))

sched.add_process(counter1)
sched.add_process(counter2)
sched.add_process(counter3)
sched.add_process(counter4)

while not sched.finished():
	sched.check_events()
	sched.run_next()
