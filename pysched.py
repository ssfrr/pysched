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



""" pySched - a nonpremptive process scheduler

pySched is an scheduler demo example. It isn't intended to do anything useful.

"""
# define states
class State:
	WAITING = 0
	RUNNABLE = 1
	DONE = 2
	DEAD = 3

class Process:
	"""A base class for an empty process

	Process should be subclassed with the run() function
	overridden to provide that process's functionality.

	"""
	def __init__(self):
		self.name = ""
		self.state = State.DONE
		# lower-value priority runs first
		self.priority = 100;
		self.wake_event = None
		self.parent = None
	# subclasses override run() to do their work
	def run(self):
		pass
	def runnable(self):
		return self.state == State.RUNNABLE
	def waiting(self):
		return self.state == State.WAITING
	def done(self):
		return self.state == State.DONE
	def wait(self, wake_event):
		self.wake_event = wake_event
		self.state = State.WAITING

class Event:
	"""A base class for an empty event that never occurs

	"""
	def occured():
		return 0

class Runqueue:
	def __init__(self):
		self.processes = []
	def add(self, new_process):
		"""Adds a new process to the list using a linear search. Blech"""
		for index in range(len(self.processes)):
			if new_process.priority < self.processes[index].priority:
				self.processes.insert(index, new_process)
				return
		self.processes.append(new_process)
	def pop(self):
		return self.processes.pop(0)
	def __len__(self):
		return len(self.processes)

class Scheduler:
	def __init__(self):
		self.runnable_processes = Runqueue()
		self.waiting_processes = []
	def add_process(self, new_process):
		if new_process.runnable():
			self.runnable_processes.add(new_process)
		if new_process.waiting():
			self.waiting_processes.append(new_process)
	def idle(self):
		return len(self.runnable_processes) == 0
	def finished(self):
		return (len(self.runnable_processes) == 0 and
				len(self.waiting_processes) == 0)
	def check_events(self):
		for process in self.waiting_processes:
			if process.wake_event.occurred():
				process.state = State.RUNNABLE
				self.add_process(process)
				self.waiting_processes.remove(process)
	def run_next(self):
		if len(self.runnable_processes) > 0:
			process = self.runnable_processes.pop()
			process.run()
			if not process.done():
				self.add_process(process)
