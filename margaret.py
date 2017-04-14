import sys
import pickle

class Margaret:
	def __init__(self):
		self.note_dict = dict()
		self.margaret_notes = list()
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
			self.margaret_notes = self.note_dict['Margaret']
		except KeyError:
			self.note_dict['Margaret'] = list()
			self.margaret_notes = self.note_dict['Margaret']
		self.margaret_notes.append(note)
		self.note_dict['Margaret'] = self.margaret_notes
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
    if sys.argv[0] == "margaret.py":
        margaret = Margaret()
        if sys.argv[1] == "w":
        	margaret.write(sys.argv[2])
        if sys.argv[1] == "r":
        	margaret.read()

