def character_shifter(char, n=3):
    number  = ord(char)
    number -= ord("a")
    number += n
    number %= 26
    number += ord("a")
    return chr(number)
x = character_shifter("z")
print(x)
