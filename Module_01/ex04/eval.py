class Evaluator:
	@staticmethod
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		ret = 0
		for c, w in zip(coefs, words):
			ret += (c * len(w))
		return ret
 
	@staticmethod
	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		ret = 0
		for w in enumerate(words): # w[0] est le compteur et w[1] l elemt de la liste
			ret += (coefs[w[0]] * len(w[1]))
		return ret
