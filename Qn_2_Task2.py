def to_ascii(s):
    return [ord(c) for c in s]

def from_ascii(ascii_list):
    return ''.join(chr(i) for i in ascii_list)



def process_string(user_input):
    letters = []
    digits = []
    even_digits = []
    uppercase_letters = []

    for char in user_input:
        if char.isdigit():
            digits.append(char)
            if int(char) % 2 == 0:
                even_digits.append(char)
        elif char.isalpha():
            if char.isupper():
                uppercase_letters.append(char)
            letters.append(char)

    # Convert even digits and uppercase letters to ASCII
    ascii_even_digits = [ord(c) for c in even_digits]
    ascii_uppercase_letters = [ord(c) for c in uppercase_letters]

    print(f"Letters: {letters}")
    print(f"Digits: {digits}")
    print(f"Even Digits: {even_digits}")
    print(f"Uppercase Letters: {uppercase_letters}")
    print(f"ASCII values of Even Digits: {ascii_even_digits}")
    print(f"ASCII values of Uppercase Letters: {ascii_uppercase_letters}")

def main():
    user_input = input("Enter a string: ")
    process_string(user_input)



if __name__ == "__main__":
    main()
from collections import Counter

# Function to decrypt the Caesar cipher text based on the given shift value
def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Check if the character is an alphabet letter
            shift_base = 65 if char.isupper() else 97  # Choose base for uppercase or lowercase letters
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char  # Append decrypted letter
        else:
            decrypted_text += char  # Keep non-letter characters as they are
    return decrypted_text

# Function to score the readability of the decrypted text based on word frequency
def score_text(text, common_words):
    words = text.split()
    word_count = Counter(words)
    score = sum(word_count[word] for word in common_words if word in word_count)
    return score

# Function to find the best shift key based on scoring
def find_best_shift_and_decrypt(ciphertext):
    common_words = {"the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "we", "his", "from", "they", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me"}
    
    best_shift = None
    best_score = 0
    best_decrypted_text = ""
    
    for shift in range(1, 26):  # Loop through all possible shift values
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
        score = score_text(decrypted_text, common_words)
        if score > best_score:
            best_score = score
            best_shift = shift
            best_decrypted_text = decrypted_text
    
    return best_shift, best_decrypted_text

# Provided cryptogram
ciphertext = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAONG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Find the best shift key and the corresponding decrypted text
best_shift, best_decrypted_text = find_best_shift_and_decrypt(ciphertext)

print(f"Best shift: {best_shift}")
print(f"Decrypted text: {best_decrypted_text}")

