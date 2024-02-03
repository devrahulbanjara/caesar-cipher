import os
def welcome():
    """
    Displays a welcome message for the Caesar Cipher program.
    """
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")





def enter_message():
    """
    Gets user input for encryption or decryption mode, user message, and shift number.

    Returns:
    - user_mode (str): The selected mode ('e' for encryption, 'd' for decryption).
    - user_message (str): The message entered by the user.
    - shift_number (int): The shift number for the Caesar Cipher.
    """
    # Get encryption (e) or decryption (d) mode from the user
    user_mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

    # Validate the user input for mode
    while user_mode not in "ed":
        print("Invalid Mode")
        user_mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

    # Get the user message based on the selected mode
    if user_mode == "e":
        user_message = input("What message would you like to encrypt: ")
    else:
        user_message = input("What message would you like to decrypt: ")

    # Get the shift number from the user
    shift_number = input("What is the shift number: ")

    # Validate the user input for the shift number
    while (not shift_number.isdigit()) or int(shift_number) < 0:
        print("Invalid Shift")
        shift_number = input("What is the shift number: ")

    # Return the user mode, user message, and the shift number as integers
    return user_mode, user_message, int(shift_number)





def encrypt(message, shift):
    """
    Encrypts the input message using the Caesar Cipher with the specified shift.

    Parameters:
    - message (str): The message to be encrypted.
    - shift (int): The shift value for the Caesar Cipher.

    Returns:
    - encrypted_text (str): The encrypted message.
    """
    encrypted_text = ""
    for char in message:
        if char.isalpha():  # Check if the character is an alphabet letter
            # Convert character to ASCII value
            ascii_value = ord(char.upper())
            # Apply the Caesar Cipher shift
            shifted_ascii_value = (ascii_value - 65 + shift) % 26 + 65
            # Convert back to character and maintain the case
            shifted_char = chr(shifted_ascii_value)
            encrypted_text += shifted_char
        else:
            # If the character is not an alphabet letter, keep it unchanged
            encrypted_text += char
    return encrypted_text





def decrypt(message, shift):
    """
    Decrypts the input message using the Caesar Cipher with the specified shift.

    Parameters:
    - message (str): The message to be decrypted.
    - shift (int): The shift value for the Caesar Cipher.

    Returns:
    - decrypted_text (str): The decrypted message.
    """
    decrypted_text = ""
    for char in message:
        if char.isalpha():  # Check if the character is an alphabet letter
            # Convert character to ASCII value
            ascii_value = ord(char.upper())
            # Apply the Caesar Cipher shift for decryption
            shifted_ascii_value = (ascii_value - 65 - shift) % 26 + 65
            # Convert back to character and maintain the case
            shifted_char = chr(shifted_ascii_value)
            decrypted_text += shifted_char
        else:
            # If the character is not an alphabet letter, keep it unchanged
            decrypted_text += char
    return decrypted_text





def process_file(filename, mode):
    """
    Processes a file for encryption or decryption and returns a list of messages.

    Parameters:
    - filename (str): The name of the file to be processed.
    - mode (str): The mode ('e' for encryption, 'd' for decryption).

    Returns:
    - messages (list): A list of processed messages.
    """
    messages = []
    shift = int(input("What is the shift number: "))
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if mode == "e":
                messages.append(encrypt(line, shift))
            elif mode == "d":
                messages.append(decrypt(line, shift))
    return messages





def write_messages(messages):
    """
    Writes a list of messages to a file named "results.txt".

    Parameters:
    - messages (list): The list of messages to be written to the file.
    """
    with open("results.txt", "w") as file:
        file.write(" ".join(messages))





def message_or_file():
    """
    Gets user input for message or file-based encryption/decryption.

    Returns:
    - mode (str): The selected mode ('e' for encryption, 'd' for decryption).
    - message (str): The message entered by the user (or None if reading from a file).
    - filename (str): The filename entered by the user (or None if reading from the console).
    """
    # Get encryption (e) or decryption (d) mode from the user
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ["e", "d"]:
            break
        else:
            print("Invalid Mode")

    # Get source from the user - file (f) or console (c)
    while True:
        source = input(
            "Would you like to read from a file (f) or the console (c)? ").lower()
        if source in ["f", "c"]:
            break
        else:
            print("Invalid Source")

    # If the source is a file, get the filename
    if source == "f":
        while True:
            filename = input("Enter a filename: ")
            # Check if the file exists
            if is_file(filename):
                break
            else:
                print("Invalid Filename")

        # Return the mode (e/d), None for message, and the filename for file
        return mode, None, filename
    # If the source is the console, get the message from the user
    else:
        # Get the message to be encrypted or decrypted
        message = input(f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: ")
        # Return the mode (e/d), the message in uppercase, and None for filename
        return mode, message.upper(), None






def is_file(filename):
    """
    Checks if a file exists.

    Parameters:
    - filename (str): The name of the file to be checked.

    Returns:
    - bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(filename)






def main():
    """
    Executes the main program logic for the Caesar Cipher.
    """
    # Display a welcome message
    welcome()

    while True:
        # Get user input for mode, message, and filename
        mode, message, filename = message_or_file()

        # Check if a filename is provided
        if filename is not None:
            # Process file based on mode (encrypt or decrypt)
            messages = process_file(filename, mode)
            # Write processed messages to results.txt
            write_messages(messages)
            print("Output written to results.txt")
        else:
            # Get the shift number from the user
            shift = int(input("What is the shift number: "))
            # Encrypt or decrypt based on the chosen mode
            if mode == "e":
                result = encrypt(message, shift)
                print(result)
            else:
                result = decrypt(message, shift)
                print(result)

        # Ask the user if they want to encrypt or decrypt another message
        another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()

        # Check the user's response
        if another_message == "n":
            print("Thanks for using the program, goodbye!")
            break
        elif another_message == "y":
            # Continue the loop for another message
            pass
        else:
            print("Invalid response")


main()
