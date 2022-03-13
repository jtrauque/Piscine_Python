languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }
for cle, value in languages.items(): #The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
    print("%s was created by %s" %(cle, value))
