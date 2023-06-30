import sys
import string


def encrypt(characterset, text, key, secret):
    result = ""
    secret = list(secret)
    secret_index = 0
    text = list(text)
    outer_index = characterset.index(key)
    # print("outer index: " + str(outer_index))

    for c in text:
        inner_index = characterset.index(secret[secret_index])
        # print("inner index: " + str(inner_index))

        if c not in characterset:
            print(
                "WARNING: Skipping character [" + c + "] not in characterset")
            continue

        char_index = characterset.index(c)
        # print("char index: " + str(char_index))

        if ((char_index - inner_index + outer_index) < len(characterset)):
            encrypted_char = characterset[char_index -
                                          inner_index + outer_index]
        else:
            encrypted_char = characterset[char_index -
                                          inner_index + outer_index - len(characterset)]
        if secret_index + 1 < len(secret):
            secret_index += 1
        else:
            secret_index = 0

        result += encrypted_char

    return result


def decrypt(characterset, text, key, secret):
    result = ""
    secret = list(secret)
    secret_index = 0
    text = list(text)
    outer_index = characterset.index(key)
    # print("outer index: " + str(outer_index))

    for c in text:
        inner_index = characterset.index(secret[secret_index])
        # print("inner index: " + str(inner_index))

        if c not in characterset:
            print(
                "WARNING: Skipping character [" + c + "] not in characterset")
            continue

        char_index = characterset.index(c)
        # print("char index: " + str(char_index))

        if ((char_index + inner_index - outer_index) < len(characterset)):
            encrypted_char = characterset[char_index +
                                          inner_index - outer_index]
        else:
            encrypted_char = characterset[char_index +
                                          inner_index - outer_index - len(characterset)]
        if secret_index + 1 < len(secret):
            secret_index += 1
        else:
            secret_index = 0

        result += encrypted_char

    return result


text = sys.argv[1]

characterset = string.ascii_lowercase
characterset += ' '
# characterset = list(string.printable)

key = 'l'
secret = 'crayon'

print("Text: " + text)

result = encrypt(characterset, text, key, secret)

print("Encrypt: " + result)
print("Decrypt: " + decrypt(characterset, result, key, secret))
