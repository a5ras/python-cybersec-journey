"""
IPv4 validator Validate an IPv4 address: exactly four parts, each numeric, each 0–255.
Hint: isdigit() , then range check inside a loop. Expected: 
"192.168.1.1" → valid
"192.168.1.256" → invalid
"1.2.3" → invalid
"""
def ipv4_validator(ipv4):
    ipv4_list = ipv4.split(".")
    if len(ipv4_list) != 4:
        return f"{ipv4} - invalid"
    for i in ipv4_list:
        if not i.isdigit() or int(i) > 255:
            return f"{ipv4} - invalid"
    return f"{ipv4} - valid"
        
        
        
ip = input("Enter Your IPv4 : ")
x  = ipv4_validator(ip)
print(x)