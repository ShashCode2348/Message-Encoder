from tkinter import messagebox, simpledialog, Tk
from random import choice, randrange

#Functions

#Gets the message
def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message:')
    return message

#Swaps the characters
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

#Character shifter
def character_shifter_encrypt(message, characters):
    returnMessage = ''
    shift = randrange(5, len(characters) - 5)
    for character in message:
        if character in characters:
            position = characters.find(character)
            newPosition = (position + shift) % len(characters)
            character = characters[newPosition]
        returnMessage += character
    return shift, returnMessage

def character_shifter_decrypt(message, shift, characters):
    returnMessage = ''
    shift *= -1
    for character in message:
        if character in characters:
            position = characters.find(character)
            newPosition = (position + shift) % len(characters)
            character = characters[newPosition]
        returnMessage += character
    return returnMessage

def encrypt(message, characters):
    encrypt1 = swap_letters(message)
    shift, encrypt2 = character_shifter_encrypt(encrypt1, characters)
    encrypt3_list = []
    for counter in range(0, len(encrypt2)):
        encrypt3_list.append(encrypt2[counter])
        encrypt3_list.append(choice(characters))
    encrypt3 = ''.join(encrypt3_list)
    encrypt4 = ''.join(reversed(encrypt3))
    encrypt5 = f"{encrypt4}{shift:02}"
    print(encrypt5)
    return encrypt5

def decrypt(message, characters):
    shift = int(message[-2:])
    decrypt1 = message[:-2]
    decrypt2 = ''.join(reversed(decrypt1))
    decrypt3_list = get_even_letters(decrypt2)
    decrypt3 = ''.join(decrypt3_list)
    decrypt4 = character_shifter_decrypt(decrypt3, shift, characters)
    decrypt5 = swap_letters(decrypt4)
    print(decrypt5)
    return decrypt5


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
