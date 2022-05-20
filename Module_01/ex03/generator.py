import random


def generator(text, sep=" ", option=None):
    if not text or not isinstance(text, str):
        print("Error")
        quit()

    new = text.split(sep)
    if not new:
        exit()
    if not option:
        pass
    elif not isinstance(option, str) or option not in ["shuffle", "unique", "ordered"]:
        raise ValueError("The option is not valid")
    elif option == "shuffle":
        new = random.sample(new, len(new))
    elif option == "unique":
        new = list(dict.fromkeys(new))
    elif option == "ordered":
        new.sort()
    for i in new:
        yield i


for word in generator("This is a simple string for a basic test. Very simple.", " "):
    print(word)
for word in generator("hello ca va hello toi", " "):
    print(word)
print("-------------------------------------------")
for word in generator("hello ca va hello toi", " ", "unique"):
    print(word)
print("-------------------------------------------")
for word in generator("a b c d e", " ", "shuffle"):
    print(word)
print("-------------------------------------------")
for word in generator("b e c a d", " ", "ordered"):
    print(word)
print("++++++++++++TEST CORRECTION++++++++++++")
for word in generator("This is a simple string for a basic test. Very simple.", " "):
    print(word)
print("-----------")
for word in generator("This is a simple string for a basic test. Very simple.", "."):
    print(word)
print("-----------")
for word in generator("This is a simple string for a basic test. Very simple.", "i"):
    print(word)
print("-----------")
for word in generator("This is a simple string for a basic test. Very simple.", "si"):
    print(word)


