"""
Login attempt limiter Ask for a password up to 3 times. On success print Access
granted ; after 3 failures print Account locked . Hint: a for loop over range(3) with break ,
and else on the loop. Expected: Attempt 2 of 3 … Account locked
"""
def login_attempt_limiter():
    password = "password@123"
    attempts = 3
    # while True:
    #     usercode = input("Enter Your Password : ").strip()
    #     if usercode == password:
    #         print("Access granted")
    #         break
    #     else:
    #         Attempt+=1
    #         if Attempt == 3 :
    #             print("Account locked")
    #             break
    #         print(f"Attempt {Attempt} of 3")
    for attempt in range(attempts):
        userPassword = input("Enter the password : ").strip()
        if userPassword == password:
            print("Access granted")
            break
        else:
            print(f"Attempt {attempt+1} of 3")
    else:
        print("Account locked")
login_attempt_limiter()
