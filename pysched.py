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
