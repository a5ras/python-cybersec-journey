def hash_type_guesser(hex_string):
    lenght = len(hex_string)
    if lenght == 32:
        print("MD5")
    elif lenght == 40:
        print("SHA-128")
    elif lenght == 64:
        print("SHA-256")
    else:
        print("Unrecognized Hash")
hash = "5d41402abc4b2a76b9719d911017c592"
hash_type_guesser(hash)