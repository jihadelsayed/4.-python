import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&'#, '(', ')'
, '*', '+']

numberLetters = int(input("How many letters(10)?\n") or 10) 
numberNumbers = int(input(f"How many numbers would you like(4)?\n") or 4)
numberSymbols = int(input(f"How many symbols would you like(1)?\n") or 1)
WebsiteName = str(input(f"What is the website that are you going to use(Neetechs)?\n") or "Neetechs")

passwordList = []
for char in range(1, numberLetters + 1):
    passwordList.append(random.choice(letters))
for char in range(1, numberNumbers + 1):
    passwordList.append(random.choice(numbers))
for char in range(1, numberSymbols + 1):
    passwordList.append(random.choice(symbols))
random.shuffle(passwordList)

password = ""
for char in passwordList:
    password += char

print(f"Your random password is: {password}")

with open("password.txt", "a") as myfile:
    myfile.write(WebsiteName + ":" + password+"\n")
