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



from pysched import State, Process 
from timers import RelativeTimer

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

