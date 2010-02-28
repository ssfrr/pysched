from pysched import State, Process 
from timerevents import RelativeTimer

class Counter(Process):
	def __init__(self, name, lifetime):
		self.name = name
		self.tics_left = lifetime
		if lifetime > 0:
			self.state = State.RUNNABLE
		else:
			self.state = State.DONE
	def run(self):
		print "Name: %s, Tics Remaining: %d" % (self.name, self.tics_left)
		self.tics_left -= 1
		if self.tics_left < 0:
			self.state = State.DONE

class SlowCounter(Counter):
	def __init__(self, name, lifetime, rate=1):
		Counter.__init__(self, name, lifetime)
		self.wait_time = rate
	def run(self):
		Counter.run(self)
		if not self.done():
			self.wait(RelativeTimer(self.wait_time))

