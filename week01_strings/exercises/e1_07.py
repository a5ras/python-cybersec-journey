cars_number = "4532015112830366"
counter = len(cars_number)
result = (counter -4)*"*"+cars_number[-1:-3:-1]
print(result)