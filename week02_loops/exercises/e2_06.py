"""
Digit sum Sum the digits of an integer without converting to a string. Hint: % 10
gets the last digit, // 10 removes it. Expected: 9875 → 29
"""
def digit_sum(digit):
    total = 0
    while digit > 0:
          total += digit % 10
          digit //=10
    return total
x = digit_sum(152)
print(x)