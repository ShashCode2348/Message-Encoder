from random import choice, randrange

#Functions

#Gets the message
def get_task():
    task = input('Do you want to encrypt or decrypt(e/d)? ')
    return task

def get_message():
    message = inputFull('Enter the message:')
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
    returnMessage += str(shift)
    return returnMessage

def character_shifter_decrypt(message, characters):
    shift = int(message[-2:])
    message.rstrip().rstrip()
    returnMessage = ''
    shift *= -1
    for character in message:
        if character in characters:
            position = characters.find(character)
            newPosition = (position + shift) % len(characters)
            character = characters[newPosition]
        returnMessage += character
    return returnMessage

#Main(encrypt and decrypt)
def encrypt(message, characters):
    encrypt1 = swap_letters(message)
    encrypt2 = character_shifter_encrypt(encrypt1, characters)
    encrypt3_list = []
    for counter in range(0, len(encrypt2)):
        encrypt3_list.append(encrypt2[counter])
        encrypt3_list.append(choice(characters))
        print(encrypt3_list[-1])
    encrypt3 = ''.join(encrypt3_list)
    encrypt4 = ''.join(reversed(encrypt3))
    return encrypt4

def decrypt(message, characters):
    decrypt1 = ''.join(reversed(message))
    decrypt2_list = get_even_letters(decrypt1)
    decrypt2 = ''.join(decrypt2_list)
    decrypt3 = character_shifter_decrypt(decrypt2, characters)
    decrypt4 = swap_letters(decrypt3)
    return decrypt4

#Gets the input for more than 1 line of text
def inputFull(inpText):
    input_received = True
    input_string = ""
    print(inpText, end="")
    while input_received:
      new_input = input()
      if new_input:
        input_string += (new_input + "\n")
      else:
        input_received = False
    return input_string

#Variables
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"£$%^&* \()-_=+[]{};:@#~,<.>/?¬'|\n"

#Main code
task = get_task()
message = get_message()
if task.lower() == 'e':
    print('Message to encrypt is:', message, "\n")
    encrypted = encrypt(message, characters)
    print('Ciphertext of the secret message is:' + encrypted)
elif task.lower() == 'd':
    print('Message to decrypt is:', message)
    decrypted = decrypt(message, characters)
    print('Plaintext of the secret message is:' + decrypted)
else:
    quit()
