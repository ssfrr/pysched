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



from time import time
from pysched import Event

class RelativeTimer(Event):
	def __init__(self, relative_time):
		self.wake_time = time() + relative_time;
	def occurred(self):
		return time() > self.wake_time

class AbsoluteTimer(Event):
	pass
