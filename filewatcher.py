from pysched import State, Process, Event
import os

class FileWatcher(Process):
	def __init__(self, name, filename):
		self.name = name
		self.filename = filename
		self.wait(FileExistsEvent(filename))
	def run(self):
		print "File Found: " + self.filename
		self.state = State.DONE

class FileExistsEvent(Event):
	def __init__(self, filename):
		self.filename = filename
	def occurred(self):
		return self.filename in os.listdir(".")
