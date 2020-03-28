import string as str


def encrypt(text):
    encryption = ''
    for letter in text:
        if letter in str.punctuation:
            encryption += letter
        if letter in str.whitespace:
            encryption += letter
        if letter in str.ascii_lowercase:
            i = str.ascii_lowercase.find(letter) - 13
            encryption += str.ascii_lowercase[i]
        if letter in str.ascii_uppercase:
            i = str.ascii_uppercase.find(letter) - 13
            encryption += str.ascii_uppercase[i]
    return encryption

def decrypt(text):
    decryption = ''
    for letter in text:
        if letter in str.punctuation:
            decryption += letter
        if letter in str.whitespace:
            decryption += letter
        if letter in str.ascii_lowercase:
            i = (str.ascii_lowercase.find(letter) + 13) % len(str.ascii_lowercase)
            decryption += str.ascii_lowercase[i]
        if letter in str.ascii_uppercase:
            i = (str.ascii_uppercase.find(letter) + 13) % len(str.ascii_uppercase)
            decryption += str.ascii_uppercase[i]
    return decryption

# print(decrypt("Mrffntr zr lbhe svefg naq ynfg anzr, naq jung glcr bs jbex lbh ubcr gb qb jura lbh tenqhngr. Ayfb fraq zr n cnentencu funevat ubj lbh orpnzr vagrerfgrq va pbzchgre cebtenzzvat."))

print(encrypt('Hello. My name is Devan. '))
print(decrypt('Uryyb. Zl anzr vf Qrina.'))
