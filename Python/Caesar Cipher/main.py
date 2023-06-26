from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
recall = "yes"


def encrypt(plain_text, shift_amount):
    cipher_index = []
    cipher_text = ""
    if shift_amount > 25:
        shift_amount = shift_amount % 26
    for letters in plain_text:
        if letters in alphabet:
            text_index = alphabet.index(letters)
            plus_index = (text_index + shift_amount)

            cipher_index.append(alphabet[plus_index])
        else:
            cipher_index.append(" ")

    for index in cipher_index:
        cipher_text += str(index)

    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    cipher_index = []
    plain_text = ""
    if shift_amount > 25:
        shift_amount = shift_amount % 26
    for letters in cipher_text:
        if letters != " ":
            text_index = alphabet.index(letters)
            minus_index = (text_index - shift_amount)
            cipher_index.append(alphabet[minus_index])
        else:
            cipher_index.append(" ")

    for index in cipher_index:
        plain_text += str(index)

    print(f"The decoded text is {plain_text}")


def direction_chose(choice):
    if choice == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    else:
        decrypt(cipher_text=text, shift_amount=shift)


while recall != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    direction_chose(choice=direction)
    recall = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
