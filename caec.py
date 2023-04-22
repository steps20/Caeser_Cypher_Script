import argparse
import string

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--decrypt", action="store_true", help="Apply if you want to decrypt", required=False)
    parser.add_argument("-e", "--encrypt", action="store_true", help="Apply to encrypt a message.", required=False)
    parser.add_argument("-s", "--shift", dest="shift", help="Choose the encryption or decryption shift amount.", required=False)
    parser.add_argument("-f", "--file", dest="file", help="Enter your specified file path here.", required=False)
    parser.add_argument("-t", "--text", dest="text", help="Enter the text to be decrypted or encrytped.", required=False)
    args = parser.parse_args()
    if args.file and args.text:
        print("Error, you can only encrypt OR decrypt from one source at a time [-t] or [-f]")
        quit()
    elif args.decrypt and args.encrypt:
        print("Error, you can only encrypt OR decrypt; not both simultaneously.")
        quit()
    elif not args.decrypt and not args.encrypt:
        print("Error, choose an option with either '-e'(encrypt) or '-d'(decrypt)")
        quit()
    elif not args.file and not args.text:
        print("Error, choose an option of text to decrypt with either '-t'(text) or '-f'(file)")
        quit()
    elif args.encrypt and not args.shift:
        print("When choosing to encrypt you must enter the shift key with [-s]")
        quit()
    return args

def decrypt_caesar_shift(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            plaintext += chr((ord(char.lower()) - int(shift) - 97) % 26 + 97)
        else:
            plaintext += char
    print(f"The decrypted text is: {plaintext}")

def decrypt_caesar(ciphertext):
    for i in range(26):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                shifted_char = chr((ord(char.lower()) - 97 - i) % 26 + 97)
                plaintext += shifted_char
            else:
                plaintext += char
        print(f"Shift {i}: {plaintext}")

def read_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return " ".join(lines)

def caesar_encrypt(text, shift):
    ciphertext = ""
    for char in text:
        if char.isalpha():
            ciphertext += chr((ord(char.lower()) - 97 + int(shift)) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext


options = get_arguments()
if options.decrypt:
    if options.shift:
        if options.file:
            text = decrypt_caesar_shift(read_file(options.file), options.shift)
        else:
            text = decrypt_caesar_shift(options.text, options.shift)
    else:
        if options.file:
            text = decrypt_caesar(read_file(options.file))
        else:
            text = decrypt_caesar(options.text)

elif options.encrypt:
    if options.file:
        text = caesar_encrypt(read_file(options.file), options.shift)
    else:
        text = caesar_encrypt(options.text, options.shift)
    print(f"Encrypted text is: {text}")
