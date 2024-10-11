# Morse Code Decoder and Sound Player

This project decodes Morse code input into text and plays the corresponding Morse code sounds (dots and dashes). It provides a simple command-line interface where users can input Morse code, get the decoded text, and listen to the Morse code as sound.

## Features

- Decode Morse code into readable text.
- Play sound for Morse code (dot and dash sounds).
- Simple command-line interface for user input and output.

## Prerequisites

- Python 3.7 or above
- Virtual environment (recommended)

### Required Python Packages

- `pygame` - For playing sounds.
- `playsound==1.2.2` - For playing dot and dash sounds (version 1.2.2 to avoid compatibility issues).
- `gTTS` - Google Text-to-Speech for optional speech playback.

### Sound Files

Ensure that you have the following sound files in the same directory as the script:

- `dot.wav` - Sound for Morse code dot (`.`).
- `dash.wav` - Sound for Morse code dash (`-`).

## Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory:
```
cd morse_decode
```
3. Create a virtual environment (optional but recommended):
```
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

4. Install the required packages:
```
pip install pygame playsound==1.2.2 gTTS
```

# Usage

To run the script:

1. Activate the virtual environment:

```
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```
2. Run the Morse code decoder script:

```
python app.py
```
3. Enter your Morse code when prompted. Use / to separate words (e.g., ... --- ... / .... . .-.. .--.).
4. The decoded message will be displayed, and the Morse code will be played as sound.

### Example
```
Enter the Morse code (Use '/' for space between words): ... --- ... / .... . .-.. .--.
Decoded Text: SOS HELP

Playing Morse code sound...
```
### Troubleshooting

- Make sure that the sound files dot.wav and dash.wav are in the same directory as the script.
- Ensure that you have installed the required Python packages.

### License

This project is licensed under the MIT License.