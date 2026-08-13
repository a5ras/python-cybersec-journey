def key_value_splitter(keyValue):
    if not "=" in keyValue:
        print("invalid key or value")
    else: 
        key,value = keyValue.split("=",1)
    return key, value
k , v = key_value_splitter("password=abc=123")
print(f"key is : {k}, value is {v}!")
