"""
Collatz length For a starting number, count the steps to reach 1 using: if even,
halve it; if odd, 3n+1 . Hint: while n != 1 , count each iteration. Expected: 27 → 111 steps
"""
def collatz_length(userInput):
    counter = 0
    while userInput != 1:
      if userInput % 2 == 0:
        userInput //= 2
      else:
          userInput  = userInput * 3 + 1
      counter+=1
    return counter
x = collatz_length(27)
print(x)
