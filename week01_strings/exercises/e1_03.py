word = "The quick brown fox jumps over the lazy dog."
vowels ="aeiou"
counter = 0
for i in word:
    if i in vowels:
        counter+=1
print(counter)