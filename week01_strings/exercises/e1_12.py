"""
Convert a byte count to a human-readable string with one
decimal place (B, KB, MB, GB)
"""
def byte_size_formatte(userInput, value):
    byteList = ["b", "kb", "mb", "gb"]
    if not userInput in byteList:
        print('Invalide Value')
    else:
        if userInput == "b":
            print(f"{value}B")
        elif userInput == "kb":
            print(f"{round(value/1024)}KB")
        elif userInput == "mb":
            print(f"{round(value/(1024*1024))}MB")  
        elif userInput == "gb":
            print(f"{round(value/(1024*1024*1024))}GB")
userInput = int(input("Enter A Value : "))
unit = input("Enter The Unit : ")
byte_size_formatte(unit,userInput)