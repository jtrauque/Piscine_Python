import sys 

if len(sys.argv) > 1:
	sys.argv.remove(sys.argv[0])
	str2=sys.argv[0] #on enregistre le premier
	for arg in sys.argv[1:]: #on commence la boucle au second element comme ca pas d espace au debut ! 
		str2 += ' ' + arg
	print(str2[::-1].swapcase())
