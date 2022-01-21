from tkinter import messagebox, simpledialog, Tk
from random import choice

#Functions
def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message:')
    return message

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + ' '
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def character_shifter(message, encrypt, characters):
    returnMessage = ''
    if encrypt == True:
        shift = 8
    else:
        shift = -8
    for character in message:
        if character in characters:
            position = characters.find(character)
            newPosition = (position + shift) % len(characters)
            character = characters[newPosition]
        returnMessage += character
    return returnMessage

def encrypt(message, characters):
    encrypt1 = swap_letters(message)
    encrypt2 = character_shifter(encrypt1, True, characters)
    encrypt3_list = []
    for counter in range(0, len(encrypt2)):
        encrypt3_list.append(encrypt2[counter])
        encrypt3_list.append(choice(characters))
    encrypt3 = ''.join(encrypt3_list)
    encrypt4 = ''.join(reversed(encrypt3))
    print(encrypt4)
    return encrypt4

def decrypt(message, characters):
    decrypt1 = ''.join(reversed(message))
    decrypt2_list = get_even_letters(decrypt1)
    decrypt2 = ''.join(decrypt2_list)
    decrypt3 = character_shifter(decrypt2, False, characters)
    decrypt4 = swap_letters(decrypt3)
    print(decrypt4)
    return decrypt4


#Variables
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"£$%^&* \()-_=+[]{};:@#~,<.>/?`¬\'|'

#Main code
root = Tk()

while True:
    task = get_task()
    message = get_message()
    if task.lower() == 'encrypt':
        messagebox.showinfo('Message to encrypt is:', message)
        encrypted = encrypt(message, characters)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
    elif task.lower() == 'decrypt':
        messagebox.showinfo('Message to decrypt is:', message)
        decrypted = decrypt(message, characters)
        messagebox.showinfo('Plaintext of the secret message is:', decrypted)
    else:
        break
root.mainloop()
