# 11 - implement the ceasar ciper: http://practicalcryptography.com/ciphers/caesar-cipher/
# Must have two functions, encryptc(plaintext) and decryptc(encryptedtext)

alphabets = 'abcdefghijklmnopqrstuvwxyz'


# for i in range(len(list(alphabets))):
#     print(i,'|', alphabets[(i + 3) % len(list(alphabets))])

def encryptc(plaintext, shift=3):
    """ Encrypts the plaintext with a default shift of 3
    The character range is [a-z] """
    global alphabets

    encrypted_text = ''

    for i in plaintext:
        if i == " ":
            encrypted_text += '*'
        elif i == "\n":
            encrypted_text += '**'
        elif i == "\t":
            encrypted_text += '***'
        else:
            char_index = alphabets.index(i)
            encrypted_text += alphabets[(char_index + shift) % 26]

    return encrypted_text

def decryptc(encryptedtext, shift=-3):
    """ Decrypts the encryptedtext with a default shift of -3
    The character range is [a-z] """
    global alphabets
    decrypted_text = ''

    for i in encryptedtext:
        if i == '*':
            decrypted_text += ' '
        elif i == '**':
            decrypted_text += '\n'
        elif i == '***':
            decrypted_text += '\t'
        else:
            char_index = alphabets.index(i)
            decrypted_text += alphabets[(char_index + shift) % 26]

    return decrypted_text


strtext = 'i joined the pyhack python hackathon'
etxt = encryptc(strtext)
print(etxt)

print(decryptc(etxt))
