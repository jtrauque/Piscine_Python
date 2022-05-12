import random

def	generator(text, sep=" ", option=None):
	if not isinstance(text, str):
		print("Error")
		quit()

	new = text.split
	if option == "shuffle":
		tmp = random.sample(new, len(new))
		print(tmp)
		for i in tmp:
			yield i
	elif option == "unique":
		tmp = list(dict.fromkeys(new))
		print(tmp)
		for i in tmp:
			yield i


for word in generator("hello ca va hello toi", " ", "unique"):
	print(word)
