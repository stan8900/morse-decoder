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

# Function to play the Morse code sound
def play_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            playsound('dot.wav')  # Play dot sound
            time.sleep(0.1)  # Pause between dots and dashes
        elif symbol == '-':
            playsound('dash.wav')  # Play dash sound
            time.sleep(0.2)
        elif symbol == ' ':
            time.sleep(0.5)  # Pause between letters
        elif symbol == '/':
            time.sleep(0.7)  # Pause between words

# Main function
def main():
    morse_code_input = input("Enter the Morse code (Use '/' for space between words): ").strip()
    
    decoded_message = morse_to_text(morse_code_input)
    print(f"Decoded Text: {decoded_message}")
    
    print("\nPlaying Morse code sound...")
    play_morse_code(morse_code_input)

if __name__ == "__main__":
    main()
