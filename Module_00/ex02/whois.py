import sys
sys.tracebacklimit = 0 

if len(sys.argv) > 2:
	assert len(sys.argv) == 2, "more than one argument is provided" 
	#similaire a try si la condition est pas respecter cela retourne une erreur et la lecture s arrete
elif len(sys.argv) == 2:
	assert sys.argv[1].isdigit(), "argument is not integer"
	x = int(sys.argv[1])
	who="I'm "
	if x == 0:
		who+="Zero."
	elif x % 2 == 0:
		who+="Even."
	else:
		who+="Odd."
	print(who)
