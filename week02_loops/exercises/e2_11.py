"""
Menu loop Show a 4-option menu ( 1 Scan , 2 Report , 3 Settings , 4 Exit ),
repeat until Exit, reject invalid input. Hint: while True plus if/elif/else . Expected: invalid
input → Unknown option, try again.
"""
def menu_loop():
  menuTuple = "1 Scan" , "2 Report" , "3 Settings" , "4 Exit"
  while True:
    for menu in menuTuple:
        print(menu)
    user_choice = input("Please chose  number : ").strip()
    if not user_choice.isdigit() or not 1 <= int(user_choice) <= 4:
        print("Unknown option, try again")
    else:
        if user_choice == "1":
            print("Scaning...")
        elif user_choice == "2":
            print("Download You Report By Clicking Here!")
        elif user_choice == "3":
            print("Settings...")
        elif user_choice == "4":
            print("Bye!")
            break
menu_loop()