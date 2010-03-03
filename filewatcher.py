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



from pysched import State, Process, Event
import os

class FileWatcher(Process):
	def __init__(self, name, filename):
		self.name = name
		self.filename = filename
		self.wait(FileExistsEvent(filename))
	def run(self):
		print "Process " + self.name + " running"
		print "File Found: " + self.filename
		self.state = State.DONE

class FileExistsEvent(Event):
	def __init__(self, filename):
		self.filename = filename
	def occurred(self):
		return self.filename in os.listdir(".")
