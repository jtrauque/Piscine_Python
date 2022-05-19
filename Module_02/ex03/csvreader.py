#from csvreader import CsvReader 

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		if not filename:
			raise ValueError("No Filename")
		if not sep:
			raise ValueError("We neep separator to separate values")
	#	try:
	#		self.file = open(filename)
	#	except Exception :
	#		print("File corrupted")
#			exit()
		num_lines = sum(1 for line in open(filename))
		self.sep = sep
		self.header = header
		self.top = skip_top
		self.bot = num_lines - skip_bottom
		self.data = []
		self.size = 0
		self.first_line = ""
		self.file = filename

	def __enter__(self):
		i = 0
		#for line in self.file.readlines():
		with open(self.file) as file:
			for line in file:
				print(f"line = {line}")
				line.replace("\n", "")
				words = line.split(self.sep)
				print(f"word = {words}")
			if self.size == 0:
				self.size = len(words)
				if self.header:
					self.first_line = words	
			if self.size == len(words) and i >= self.top and i < self.bot:
				self.data.append(words)
			else:
				raise ValueError("File Corrupted")
			i += 1
		return self
			
	def	__exit__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		#self.data.close()
		pass

	def	getdata(self):
		return self.data

	def	getheader(self):
		return self.first_line


if __name__ == "__main__":
	with CsvReader('good.csv') as file:
		data = file.getdata()
		header = file.getheader()
		print(data)
