import random as r

def game():

    options = ["R", "P", "S"]
    user = input ("Please choose your charecter (Rock as R, Paper as P, Scissors as S). :D ")
    user = user.strip()
    choose = r.choice(options)
    
    if user == choose:
        print("Computer = " + choose)
        print("TIE")
        print(":D")

    elif user == "R" and choose == "S":
        print("Computer = Scissors")
        print("USER WINS")
        print("CONGRATS!!! :D")
        
    elif user == "S" and choose == "R":
        print("Computer = Rock")
        print("COMPUTER WINS")
        print("BETTER LUCK NEXT TIME!!! :D")

    elif user == "R" and choose == "P":
        print("Computer = Paper")
        print("COMPUTER WINS")
        print("BETTER LUCK NEXT TIME!!! :D")
        
    elif user == "P" and choose == "R":
        print("Computer = Rock")
        print("USER WINS")
        print("CONGRATS!!! :D")

    elif user == "P" and choose == "S":
        print("Computer = Scissors")
        print("COMPUTER WINS")
        print("BETTER LUCK NEXT TIME!!! :D")

    elif user == "S" and choose == "P":
        print("Computer = Paper")
        print("USER WINS")
        print("CONGRATS!!! :D")
