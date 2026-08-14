"""
Goal: score a password and explain the score. 
Requirements:
* Check length, character variety, and presence in a small common-password list
* Return a score (e.g. 0–100) and a rating (weak/fair/strong)
* Give specific, actionable feedback ("add a symbol", "avoid 'password'")
* Never store or transmit the input
"""
import string
COMMON_PASSWORDS = [
    "123456",
    "123456789",
    "12345678",
    "password",
    "qwerty",
    "abc123",
    "111111",
    "12345",
    "123123",
    "1234567890",
    "1234567",
    "000000",
    "qwerty123",
    "iloveyou",
    "admin",
    "welcome",
    "monkey",
    "dragon",
    "letmein",
    "football",
]
def analyze(password):
    score = 0
    feedback=[]
    length = len(password)
    if length <= 8 :
        feedback.append("make it longer!")
        score=10
    elif length <= 12:
            score=25
    else:
            score=40
    if any(c in string.punctuation for c in password):
        score += 10
    else:
        feedback.append("add at least one symbol!")
    if any(c.isdigit()  for c in password):
        score += 10
    else:
        feedback.append("add a number!")
    if any(c.islower()  for c in password):
        score += 10
    else:
        feedback.append("add a lowercase letter!")
    if any(c.isupper()  for c in password):
        score += 10
    else:
        feedback.append("add an uppercase letter!")
    for common in COMMON_PASSWORDS:
        if common in password.lower():
            score -=50 
            feedback.append("avoid common passwords like 'password'!")
    score= max(0,score)
    return score, feedback
def rate(total):
    if total <= 39:
        return "weak"
    elif total <= 69:
        return "fair"
    else:
        return "strong"

if __name__ == "__main__":
    password = input("Enter a password to check : ")
    score, feedback = analyze(password)
    rating = rate(score)
    print(f"Score :{score}/100 - {rating}!")
    if feedback:
        print("Suggestions: "+", ".join(feedback))
    else:
        print("Excellent password!")

# TODO: stretch goals