class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if not coefs or not words or len(coefs) != len(words):
            return -1
        ret = 0
        for c, w in zip(coefs, words):
            if not isinstance(w, str) or not isinstance(c, (int, float)):
                print(type(w), type(c))
                return -1
            ret += (c * len(w))
        return ret

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not coefs or not words or len(coefs) != len(words):
            return -1
        ret = 0
        # w[0] est le compteur et w[1] l elemt de la liste
        for w in enumerate(words):
            if not isinstance(w[1], str) or\
                  not isinstance(coefs[w[0]], (int, float)):
                return -1
            ret += (coefs[w[0]] * len(w[1]))
        return ret


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.enumerate_evaluate(coefs, words))
print(Evaluator.zip_evaluate(coefs, words))

print("--------------Error Management--------------")
print(Evaluator.enumerate_evaluate(None, None))
print(Evaluator.enumerate_evaluate([1, 2, 3], []))
print(Evaluator.enumerate_evaluate([1, 2, 3], ["word", 2, "wordo"]))

words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(coefs, words))
print(Evaluator.zip_evaluate(coefs, words))
