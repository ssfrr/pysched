#! /usr/bin/python

from pysched import Scheduler
from counterprocess import Counter, SlowCounter
from timerevents import RelativeTimer

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
