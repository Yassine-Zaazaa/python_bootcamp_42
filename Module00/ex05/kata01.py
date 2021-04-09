languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }

KEYS = list(languages.keys())
VALUES = list(languages.values())

for i in range(len(languages)):
    print(KEYS[i],'was created by',VALUES[i])