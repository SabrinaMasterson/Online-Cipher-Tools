#Sabrina Masterson
import base64

#Cesar Cipher:
#Code comes from a GeeksforGeeks Tutorial:
#https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
def encryptCaesar(text, s):
    result=""

    if (str(s).isdigit() == False):
        result = "Please input a number for shift"
        return result
    #Move through text
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        #for uppercase
        elif (char.islower()):
            result += chr((ord(char) + s-97) % 26 +97)
        #upper and lowercase letters have different ASCII numbers
        else:
            result += char
        #else, it's likely just a character like a period or comma
    return result

def decryptCaesar(text, s):
    s = 26-s
    result=""
    if (str(s).isdigit() == False):
        result = "Please input a number for shift"
        return result
    #Move through text
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        #for uppercase
        elif (char.islower()):
            result += chr((ord(char) + s-97) % 26 +97)
        #upper and lowercase letters have different ASCII numbers
        else:
            result += char
        #else, it's likely just a character like a period or comma

    return result


#Affine Cipher:
#code comes from GeeksforGeeks Tutorial:
#https://www.geeksforgeeks.org/implementation-affine-cipher/
def encryptAffine(text, a, b):
    result=""
    if (str(a).isdigit() == False or str(b).isdigit() == False):
        result = "Please input a number for shift or multiplier"
        return result
    elif (is_coprime(int(a), 26) == False):
        result = "Please input a coprime of 26 for multiplier"
        return result

    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((a*ord(char) +b-65) % 26 + 65)
        #for uppercase
        elif (char.islower()):
            result += chr((a*ord(char) +b-97) % 26 + 97)
        #upper and lowercase letters have different ASCII numbers
        else:
            result += char
        #else, it's likely just a character like a period or comma
    return result

def decryptAffine(text, a, b):
    result=""
    if (str(a).isdigit() == False or str(b).isdigit() == False):
        result = "Please input a number for shift or multiplier"
        return result
    elif (is_coprime(int(a), 26) == False):
        result = "Please input a coprime of 26 for multiplier"
        return result

    b = 26-b
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((a*ord(char) +b-65) % 26 + 65)
        #for uppercase
        elif (char.islower()):
            result += chr((a*ord(char) +b-97) % 26 + 97)
        #upper and lowercase letters have different ASCII numbers
        else:
            result += char
        #else, it's likely just a character like a period or comma
    return result

#check for coprime
#From w3resource, because the GeeksforGeeks explanation,
#of seeking an inverse modular made no sense
#https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-119.php
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

#atbash cipher
#has to use a lookup array, but theirs only has uppercase letters
#no key is needed, simple to implement, but I kept the names/systems from other ciphers
#https://www.geeksforgeeks.org/implementing-atbash-cipher/

def encryptAtbash(text):
    lookup_table_upper= {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}
    lookup_table_lower= {'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v',
        'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q',
        'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l',
        'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g',
        'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 'z' : 'a'}
    result=""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += lookup_table_upper[char]
        elif (char.islower()):
            result += lookup_table_lower[char]
        else:
            result += char
    return result

def decryptAtbash(text):
    lookup_table_upper = {'Z' : 'A', 'Y' : 'B', 'X' : 'C', 'W' : 'D', 'V' : 'E',
        'U' : 'F', 'T' : 'G', 'S' : 'H', 'R' : 'I', 'Q' : 'J',
        'P' : 'K', 'O' : 'L', 'N' : 'M', 'M' : 'N', 'L' : 'O',
        'K' : 'P', 'J' : 'Q', 'I' : 'R', 'H' : 'S', 'G' : 'T',
        'F' : 'U', 'E' : 'V', 'D' : 'W', 'C' : 'X', 'B' : 'Y', 'A' : 'Z'}
    lookup_table_lower = {'z' : 'a', 'y' : 'b', 'x' : 'c', 'w' : 'd', 'v' : 'e',
        'u' : 'f', 't' : 'g', 's' : 'h', 'r' : 'i', 'q' : 'j',
        'p' : 'k', 'o' : 'l', 'n' : 'm', 'm' : 'n', 'l' : 'o',
        'k' : 'p', 'j' : 'q', 'i' : 'r', 'h' : 's', 'g' : 't',
        'f' : 'u', 'e' : 'v', 'd' : 'w', 'c' : 'x', 'b' : 'y', 'a' : 'z'}
    result=""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += lookup_table_upper[char]
        elif (char.islower()):
            result += lookup_table_lower[char]
        else:
            result += char
    return result

#While I still got this from GeeksforGeeks,
#This can all be done with the base64 library, so that's nice
#here's the GeeksforGeeks and the Python3 documentation for it
#https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/
#https://docs.python.org/3/library/base64.html
def encryptBase64(text, type):
    result = ""
    result_bytes = ""
    if (type.isdigit() == False):
        result = "Please input a number for type"
        return result
    elif (type != '64' or type != '32' or type != '16'):
        result = "Type can only be '64', '32', or '16' "
        return result

    result_bytes = text.encode('ascii')
    if (type == 64):
        result = base64.b64encode(result_bytes)
    elif (type == 32):
        result = base64.b32encode(result_bytes)
    elif (type == 16):
        result = base64.b16encode(result_bytes)
    else:
        print("Error in type choice, number must be either 64, 32, or 16")
    result = result.decode('ascii')
    return result

def decryptBase64(text, type):
    result = ""
    result_bytes = ""
    if (type.isdigit() == False):
        result = "Please input a number for type"
        return result
    elif (type != '64' or type != '32' or type != '16'):
        result = "Type can only be '64', '32', or '16' "
        return result

    result_bytes = text.encode('ascii')
    if (type == 64):
        result_bytes = base64.b64decode(result_bytes)
    elif (type == 32):
        result_bytes = base64.b32decode(result_bytes)
    elif (type == 16):
        result_bytes = base64.b16decode(result_bytes)
    else:
        print("Error in type choice, number must be either 64, 32, or 16")
    result = result_bytes.decode('ascii')
    return result

#The baconian cipher is very similar to the atbash cipher in encryption
#https://www.geeksforgeeks.org/baconian-cipher/
def encryptBaconian(text):
    lookup_upper = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
          'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
          'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
          'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}
    lookup_lower = {'a': 'aaaaa', 'b': 'aaaab', 'c': 'aaaba', 'd': 'aaabb', 'e': 'aabaa',
          'f': 'aabab', 'g': 'aabba', 'h': 'aabbb', 'i': 'abaaa', 'j': 'abaab',
          'k': 'ababa', 'l': 'ababb', 'm': 'abbaa', 'n': 'abbab', 'o': 'abbba',
          'p': 'abbbb', 'q': 'baaaa', 'r': 'baaab', 's': 'baaba', 't': 'baabb',
          'u': 'babaa', 'v': 'babab', 'w': 'babba', 'x': 'babbb', 'y': 'bbaaa', 'z': 'bbaab'}
    result=""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += lookup_upper[char]
        elif (char.islower()):
            result += lookup_lower[char]
        else:
            result += char
    return result

def decryptBaconian(text):
    lookup_lower = {'a': 'aaaaa', 'b': 'aaaab', 'c': 'aaaba', 'd': 'aaabb', 'e': 'aabaa',
          'f': 'aabab', 'g': 'aabba', 'h': 'aabbb', 'i': 'abaaa', 'j': 'abaab',
          'k': 'ababa', 'l': 'ababb', 'm': 'abbaa', 'n': 'abbab', 'o': 'abbba',
          'p': 'abbbb', 'q': 'baaaa', 'r': 'baaab', 's': 'baaba', 't': 'baabb',
          'u': 'babaa', 'v': 'babab', 'w': 'babba', 'x': 'babbb', 'y': 'bbaaa', 'z': 'bbaab'}
    result=""
    i = 0
    while True:
        if (i < len(text)-4):
            substr = text[i:i + 5]
            if (substr[0] != ' '):
                result += list(lookup_lower.keys()
                                 )[list(lookup_lower.values()).index(substr)]
                i += 5
            else :
                result += ' '
                i += 1
        else :
            break
    return result

def combine_ciphs(text, eord, ciph1, ciph2, shift, mult, type):
    res_one = ""
    res_two = ""
    res_error = "An error occurred"
    if (eord == "Encrypt" or eord == "encrypt" or eord == "e"):
        if (ciph1 == "Caesar" or ciph1 == "caesar" or ciph1 == "c"):
            if (shift == 0 or shift.isdigit() == False):
                return "You must choose a digit for the shift"
            else:
                res_one = encryptCaesar(text, int(shift))
        elif (ciph1 == "Affine" or ciph1 == "affine" or ciph1 == "af"):
            if (shift == 0 or mult == 0 or shift.isdigit() == False or mult.isdigit() == False or is_coprime(int(mult), 26) == False):
                return "You must choose a digit for the shift and/or multiplier"
            else:
                res_one = encryptAffine(text, int(mult), int(shift))
        elif (ciph1 == "Base64" or ciph1 == "base64" or ciph1 == "base"):
            return "You cannot start encryption with Base64, it will break."
        elif (ciph1 == "Baconian" or ciph1 == "baconian" or ciph1 == "bacon"):
            res_one = encryptBaconian(text)
        elif (ciph1 == "Atbash" or ciph1 == "atbash" or ciph1 == "at"):
            res_one = encryptAtbash(text)
        else:
            return res_error

        if (ciph2 == "Caesar" or ciph2 == "caesar" or ciph2 == "c"):
            if (shift == 0 or shift.isdigit() == False):
                return "You must choose a digit for the shift"
            else:
                res_two = encryptCaesar(res_one, int(shift))
        elif (ciph2 == "Affine" or ciph2 == "affine" or ciph2 == "af"):
            if (shift == 0 or mult == 0 or shift.isdigit() == False or mult.isdigit() == False or is_coprime(int(mult), 26) == False):
                return "You must choose a digit for the shift and/or multiplier"
            else:
                res_two = encryptAffine(res_one, int(mult), int(shift))
        elif (ciph2 == "Base64" or ciph2 == "base64" or ciph2 == "base"):
            if (type == '64' or type == '32' or type == '16'):
                res_two = encryptBase64(res_one, int(type))
            else:
                return "You must choose a digit for the type, specifically a 16, 32, or 64"
        elif (ciph2 == "Baconian" or ciph2 == "baconian" or ciph2 == "bacon"):
            res_two = encryptBaconian(res_one)
        elif (ciph2 == "Atbash" or ciph2 == "atbash" or ciph2 == "at"):
            res_two = encryptAtbash(res_one)
        else:
            return res_error
        return res_two
        #end of encrypt

    elif (eord == "Decrypt" or eord == "decrypt" or eord == "d"):
        if (ciph1 == "Caesar" or ciph1 == "caesar" or ciph1 == "c"):
            if (shift == 0 or shift.isdigit() == False):
                return "You must choose a digit for the shift"
            else:
                res_one = decryptCaesar(text, int(shift))
        elif (ciph1 == "Affine" or ciph1 == "affine" or ciph1 == "af"):
            if (shift == 0 or mult == 0 or shift.isdigit() == False or mult.isdigit() == False or is_coprime(int(mult), 26) == False):
                return "You must choose a digit for the shift and/or multiplier"
            else:
                res_one = decryptAffine(text, int(mult), int(shift))
        elif (ciph1 == "Base64" or ciph1 == "base64" or ciph1 == "base"):
            if (type == '64' or type == '32' or type == '16'):
                res_one = decryptBase64(text, int(type))
            else:
                return "You must choose a digit for the type, specifically a 16, 32, or 64"
        elif (ciph1 == "Baconian" or ciph1 == "baconian" or ciph1 == "bacon"):
            res_one = decryptBaconian(text)
        elif (ciph1 == "Atbash" or ciph1 == "atbash" or ciph1 == "at"):
            res_one = decryptAtbash(text)
        else:
            return res_error

        if (ciph2 == "Caesar" or ciph2 == "caesar" or ciph2 == "c"):
            if (shift == 0 or shift.isdigit() == False):
                return "You must choose a digit for the shift"
            else:
                res_two = decryptCaesar(res_one, int(shift))
        elif (ciph2 == "Affine" or ciph2 == "affine" or ciph2 == "af"):
            if (shift == 0 or mult == 0 or shift.isdigit() == False or mult.isdigit() == False or is_coprime(int(mult), 26) == False):
                return "You must choose a digit for the shift and/or multiplier"
            else:
                res_two = decryptAffine(res_one, int(mult), int(shift))
        elif (ciph2 == "Base64" or ciph2 == "base64" or ciph2 == "base"):
            return "You cannot end decryption with Base64, it will break"
        elif (ciph2 == "Baconian" or ciph2 == "baconian" or ciph2 == "bacon"):
            res_two = decryptBaconian(res_one)
        elif (ciph2 == "Atbash" or ciph2 == "atbash" or ciph2 == "at"):
            res_two = decryptAtbash(res_one)
        else:
            return res_error
        return res_two
        #end of decrypt
    else:
        return res_error
    #end of combine_ciphs

