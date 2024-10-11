import time
from playsound import playsound

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

# Function to decode Morse code
def morse_to_text(morse_code):
    words = morse_code.split(' / ')  # Words separated by '/'
    decoded_message = []
    
    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join([key for letter in letters for key, value in MORSE_CODE_DICT.items() if value == letter])
        decoded_message.append(decoded_word)
    
    return ' '.join(decoded_message)

