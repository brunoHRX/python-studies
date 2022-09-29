# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
genered_password = []
final_password = ""
password_lenght = nr_letters + nr_symbols + nr_numbers
l = 0
s = 0
n = 0

for lenght in range(1, (password_lenght + 1)):
    counter = random.randint(0, 3)
    if l < nr_letters:
        l += 1
        password = str(letters[random.randint(0, len(letters)-1)])
        genered_password.append(password)
    if s < nr_symbols:
        s += 1
        password = str(symbols[random.randint(0, len(symbols)-1)])
        genered_password.append(password)
    if n < nr_numbers:
        n += 1
        password = str(numbers[random.randint(0, len(numbers)-1)])
        genered_password.append(password)

random.shuffle(genered_password)
for character in genered_password:
    final_password += str(character)

print(f"Here is your password: {final_password}")
