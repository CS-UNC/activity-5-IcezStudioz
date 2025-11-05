words_file = open('CROSSWD.txt','r')

def more_than_20(file):
    count = 0
    for file in words_file:
        if len(file) > 20:
            count += 1
            print (file)

def has_no_e(word):
    for word in words_file:
        if 'e' not in word:
            print(True)
        else:
            print(False)

def uses_only(word,letters):
    for word in words_file:
        if letters not in word:
            print(False)
        else:
            print(True)

def all_uses_only(file, letters):
    for file in words_file:
        if letters in file:
            print (file)