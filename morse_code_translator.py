import tkinter as tk
from tkinter import ttk

# Dictionary representing the Morse code chart
MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----", ", ": "--..--", ".": ".-.-.-", "?": "..--..",
    "/": "-..-.", "-": "-....-", "(": "-.--.", ")": "-.--.-",
}

# Function to encrypt the string into Morse code
def encrypt(message):
    cipher = ""
    for letter in message.upper():
        if letter != " ":
            cipher += MORSE_CODE_DICT.get(letter, "") + " "
        else:
            cipher += " "
    return cipher

# Function to decrypt the Morse code into English
def decrypt(message):
    message += " "
    decipher = ""
    citext = ""
    for letter in message:
        if letter != " ":
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += " "
            else:
                decipher += list(MORSE_CODE_DICT.keys())[
                    list(MORSE_CODE_DICT.values()).index(citext)
                ] if citext in MORSE_CODE_DICT.values() else "?"
                citext = ""
    return decipher

# Function to handle encryption
def handle_encrypt():
    input_text = english_input.get("1.0", tk.END).strip()
    result = encrypt(input_text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# Function to handle decryption
def handle_decrypt():
    input_text = morse_input.get("1.0", tk.END).strip()
    result = decrypt(input_text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# Creating the main Tkinter window
root = tk.Tk()
root.title("Morse Code Translator")

# Setting up the grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

# Widgets for English to Morse encryption
ttk.Label(root, text="Enter English Text:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
english_input = tk.Text(root, height=4, width=50)
english_input.grid(row=0, column=1, padx=5, pady=5)

encrypt_button = ttk.Button(root, text="Encrypt to Morse", command=handle_encrypt)
encrypt_button.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# Widgets for Morse to English decryption
ttk.Label(root, text="Enter Morse Code:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
morse_input = tk.Text(root, height=4, width=50)
morse_input.grid(row=2, column=1, padx=5, pady=5)

decrypt_button = ttk.Button(root, text="Decrypt to English", command=handle_decrypt)
decrypt_button.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)

# Text widget for displaying results
ttk.Label(root, text="Output:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
output_text = tk.Text(root, height=4, width=50)
output_text.grid(row=4, column=1, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
