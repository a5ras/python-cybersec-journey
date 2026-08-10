word = "security"
# x=word[::-1]
# print(x)
result = ""
for i in range(len(word)):
    result = word[i] + result
print(result)