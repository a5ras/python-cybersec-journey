email =  "ahmad@hello.com"
def email_domain_extractor(email):
    if not "@" in email:
        print("Invalid Email")
    else:
        x = email.rsplit("@",2)
        print(email)
        print(x)
        print(x[-1])
email_domain_extractor(email)