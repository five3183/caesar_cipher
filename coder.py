import string
alpha = string.ascii_lowercase

def code_this_word(key, word):
    if key > 25:
        key = key%25
        print(key)
    offset = alpha[key::]
    offset = offset + alpha[:key:]
    code_word = ''
    for letter in word:
        if letter == ' ':
            letter == ' '
            code_word = code_word + letter     
        else:
            position = alpha.find(letter.lower())
            code_word = code_word + offset[position]
    return code_word

def decode_this_word(key, word):
    if key > 25:
        key = key%25
    offset = alpha[key::]
    offset = offset + alpha[:key:]
    decode_word = ''
    for letter in word:
        if letter == ' ':
            letter == ' '
            decode_word = decode_word + letter    
        else:
            position = offset.find(letter.lower())
            decode_word = decode_word + alpha[position]
    return decode_word

z = 26
test1 = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'

test2 = code_this_word(z, test1)

print('Coded word: ' + code_this_word(z, test1))
print('Decoded word: ' + decode_this_word(z, test2))
