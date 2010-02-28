from time import time
from pysched import Event

class RelativeTimer(Event):
	def __init__(self, relative_time):
		self.wake_time = time() + relative_time;
	def occurred(self):
		return time() > self.wake_time

class AbsoluteTimer(Event):
	pass
