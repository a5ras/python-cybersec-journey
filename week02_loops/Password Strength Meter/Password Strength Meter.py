"""
Goal: produce strong, customisable passwords on demand. 
Requirements:
Accept desired length and which character sets to include (lower, upper, digits, symbols)
Guarantee at least one character from each selected set
Use secrets , never random
Generate several at once on request
Modules: secrets , string , argparse (once you reach week 10) Sample I/O: length=16,
all sets → k9#mQ2$vX7@pL4wR Stretch goals: a passphrase mode ( correct-horse-batterystaple from a wordlist); an entropy estimate in bits printed alongside each password.
"""
import string, secrets

def userChoice():
    choices = (("1. lower", "2. upper", "3. digits", "4. symbols", "5. generate"))
    charset =""
    for choice in choices:
        print(choice)
    while True:
        choice = input("chose a number : ")
        if int(choice) == 5:
            break
        if choice == "1":
            charset += string.ascii_lowercase
        if choice == "2":
            charset += string.ascii_uppercase
        if choice == "3":
            charset += string.digits
        if choice == "4":
            charset += string.punctuation
    return charset
def generatePassword(charset):
    length = int(input("What is the length you want : "))
    password = ""
    for _ in range(length):
        password += secrets.choice(charset)
    print(password)

x = userChoice()
generatePassword(x)