def more_than_20(file):
    open(file)
    for i in file:
        if len(i) > 20:
            print (i)

def has_no_e(word):
    for z in word:
        if 'e' in word:
            print(False)
        else:
            print(True)

def uses_only(word,letters):
    for word in letters:
        if letters not in word:
            print(False)
        else:
            print(True)

def all_uses_only(file, letters):
    uses_only(word,letters)
    for y in file:
        if letters in file:
            print (y)