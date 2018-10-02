import string

def isCaps(word):
    for letter in word:
        if letter in string.ascii_lowercase:
            return False
    return True

str = input('Give me a string, mortal: ')
out = ''
str = str.split()

for word in str:
    meowDone = False
    for symbol in word:
        if symbol not in string.ascii_letters:
            out += symbol
        elif meowDone:
            pass
        else:
            if isCaps(word):
                out += 'MEOW'
                meowDone = True
            else:
                if word[0] in string.ascii_uppercase:
                    out += 'Meow'
                    meowDone = True
                else:
                    out += 'meow'
                    meowDone = True
    out += ' '

print(out)
