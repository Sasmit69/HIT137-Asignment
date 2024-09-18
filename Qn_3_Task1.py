def _code(pwd, shift):  # Function to decrypt text using a specified shift value
    decrypted_text = ""  # Initialize an empty string for the decrypted result

    # Iterate over each character in the encrypted text
    for char in pwd:
        if char.isalpha():  # Check if the character is a letter
            # Calculate the new character code by applying the shift
            shifted_code = ord(char) - shift

            # Adjust for uppercase letters
            if char.isupper():
                if shifted_code > ord('Z'):
                    shifted_code -= 26
                elif shifted_code < ord('A'):
                    shifted_code += 26

            # Adjust for lowercase letters
            elif char.islower():
                if shifted_code > ord('z'):
                    shifted_code -= 26
                elif shifted_code < ord('a'):
                    shifted_code += 26

            # Convert the new character code to a character and add it to the result
            decrypted_text += chr(shifted_code)

        else:
            # For non-letter characters, just append them to the result
            decrypted_text += char

    return decrypted_text  # Return the decrypted string


# Encrypted text to decode
pwd = '''tybony_inevnoyr = 100   #encrypted code
zl_qvpg = {'xr11': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'}
qrs cebprff_ahzoref():
tybony tybony_inevnoyr 
ybpny_inevnoyr = 5
ahzoref= [1, 2, 3, 4, 5]
juvyr ybpny_inevnoyr > 0:
vs ybpny_inevnoyr % 2 == 0: 
    ahzoref.erzbir (ybpny_inevnoyr)
ybpny_inevnoyr -= 1
erghea ahzoref
zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)
qrs zbqvsl_qvpg():
ybpny_inevnoyr = 10
zl_qvpg['xr14'] = ybpny_inevnoyr
zbqvsl_qvpg(5)
qrs hcqngr_tybony():
 tybony tybony_inevnoyr
 tybony_inevnoyr += 10
sbe v va enatr(5):
 cevag(v)
 V += 1
vs zl_frg vf abg Abar naq z1_qvpg['xr14'] == 10: 
    cevag("Pbaqvgvba zrg!")
vs 5 abg va zl_qvpg:
 cevag("5 abg sbhaq va gur qvpgvbanel!")
cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
'''

# Try all shift values from 1 to 25 to find the correct decryption
for i in range(1, 26):
    decrypted_message = _code(pwd, i)  # Decrypt the text with the current shift value
    print(f"Shift {i}:")
    print(decrypted_message)
