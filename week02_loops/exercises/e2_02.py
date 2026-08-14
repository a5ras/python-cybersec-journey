"""
Multiplication table Print the times tables from 1 to 9 in an aligned grid. Hint:
nested loops, and f-string width formatting like f"{n:4}" . Expected: a 9×9 grid of aligned
numbers
"""
# def multiplication_table(number):
#     for i in range(1,11):
#         print(f"{i} * {number} = ",i*number)

# multiplication_table(2)
def multiplication_table():
    for i in range(1,10):
        for j in range(1,10):
            print(f"{i*j:4}", end="")
        print("")
multiplication_table()