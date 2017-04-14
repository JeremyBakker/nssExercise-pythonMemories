import sys
import pickle

class Mary:
	def __init__(self):
		self.note_dict = dict()
		self.mary_notes = list()
		try:
			self.note_dict = self.deserialize()
		except FileNotFoundError:
			pass

	def write(self, note):
		'''Serializes and writes a note to the notes.txt file.

		Attributes:

		note (string)
		'''

		try:
			self.note_dict = self.deserialize()
		except FileNotFoundError:
			pass
		try:
			self.mary_notes = self.note_dict['Mary']
		except KeyError:
			self.note_dict['Mary'] = list()
			self.mary_notes = self.note_dict['Mary']
		self.mary_notes.append(note)
		self.note_dict['Mary'] = self.mary_notes
		self.serialize(self.note_dict)

	def read(self):
		'''Deserializes the notes.txt file and prints the output to the command line.command

		Attributes:

		NONE
		'''

		print(self.deserialize())

	def serialize(self, note_dict):
		'''Serializes the note dictionary and writes it to the notes.txt file

		Attributes:
		note_dict (dictionary)
		'''

		with open('notes.txt', 'wb+') as f:
			pickle.dump(note_dict, f)

	def deserialize(self):
		'''Deserializes the notes.txt file and returns the contents as self.note_dict
		
		Attributes:
		NONE
		'''
		
		try:
			with open('notes.txt', 'rb+') as f:
				self.note_dict = pickle.load(f)
				return self.note_dict
		except EOFError:
			pass


if __name__ == "__main__":
    if sys.argv[0] == "mary.py":
        mary = Mary()
        if sys.argv[1] == "w":
        	mary.write(sys.argv[2])
        if sys.argv[1] == "r":
        	mary.read()