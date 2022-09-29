print('Hello World')

# For comments

# Type of data

int()
float()
str()

# checking Data Type
number = 22
type(number)

# Variables for print
angel = 12
print(f'{angel}')


# math operators

# 3+2 #Add
# 4-1 #Subtract
# 2*3 #Multiply
# 5/2 #Divide
# 5**2 #Exponent


# lists

letters = ["a", "b", "c"]
letters[0]
# Result:"a"
letters[-1]
#Result: "c"

# dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}


print(programming_dictionary["Bug"])

# Alterar ou adicionar valores

programming_dictionary["Loop"] = "Novo valor para adicionar"

print(programming_dictionary["Loop"])


# limpar a lista

programming_dictionary = {}


# Functions

def my_function():
    print("Hello")
    name = input("Your name:")
    print("Hello")


my_function()


# Operators
# Comparison

# > Greater than
# < Lesser than
# >= Greater than or equal to
# <= Lesser than or equal to
# == Is equal to
# != Is not equal to


# range(start, end, step)
for i in range(6, 0, -2):
    print(i)
# result: 6, 4, 2
# 0 is not included.
