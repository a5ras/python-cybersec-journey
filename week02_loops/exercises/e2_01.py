"""
FizzBuzz Print 1 to 100; multiples of 3 → Fizz , of 5 → Buzz , of both → FizzBuzz .
Hint: test the both-case first. Expected: 1 2 Fizz 4 Buzz ... 14 FizzBuzz 16
"""
def fizzBuzz():
  for i in range(1,101):
      if i % 5 == 0 and i % 3 == 0:
          print(f"FizzBuzz")
      elif i % 5 == 0:
          print(f"Buzz")
      elif i % 3 == 0:
          print(f"Fizz")
      else:
          print(i)
fizzBuzz()


