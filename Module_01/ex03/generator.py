import random

def	generator(text, sep=" ", option=None):
	if not isinstance(text, str):
		print("Error")
		quit()

	new = text.split()
	if not new:
		exit() 
	if option == "shuffle":
		new = random.sample(new, len(new))
	elif option == "unique":
		new = list(dict.fromkeys(new))
	elif option == "ordered":
		new.sort()
	for i in new:
		yield i


for word in generator("hello ca va hello toi", " "):
	print(word)
