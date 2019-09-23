class servo:
	description = ""
	boardpin = 0
	frequency = 0

	def __init__(self, description = "servo", boardpin = 0, frequency = 50):
		self.description=description
		self.boardpin=boardpin
		self.frequency=frequency

	def getinfo(self):
		print("{}: board pin is {} and frequency is {}").format(self.description, self.boardpin, self.frequency)

