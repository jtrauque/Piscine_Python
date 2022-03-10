import string

def text_analyzer(*args):
	'''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
	if len(args) > 1:
		print("ERROR")
		return 
	elif len(args) < 1:
		print("No argument - the default text will be : If I was smart, I would have put an argument !")
		text = "If I was smart, I would have put an argument !"
	else:
		text = args[0]
	upper = 0
	lower = 0
	punc = 0
	spaces = 0

	for c in text:
		if c.isupper():
			upper+=1
		elif c.islower():
			lower+=1
		elif c == ' ':
			spaces+=1
		elif c in string.punctuation:
			punc+=1
	print("The text contains %d characters:\n- %d upper letters\n- %d lower letters\n- %d punctuation marks\n- %d spaces\n" %(len(text), upper, lower, punc, spaces))
