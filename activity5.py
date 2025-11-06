def more_than_20(file_name):
    with open (file_name, "r") as file:
        h = []
        for i in file:
            i = i.strip()
            if len(i) > 20:
                h.append(i)
    return h

def has_no_e(word):
    result = True
    for z in word:
        if z == "e":
            result = False
    return result

def uses_only(word,letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

def all_uses_only(file,letters):
    with open (file, "r") as f:
        goodWords = []
        for word in f:
            word = word.strip()
            if uses_only(word,letters):
                goodWords.append(word)
    return goodWords