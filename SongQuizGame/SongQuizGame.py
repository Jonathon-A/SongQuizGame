
# Imports random and time
import random
import time

# Register function
def register():
    print("Please create an account ")
    # Username input
    username = input("Please create your username: ")
    # Password input
    password = input("Please create your password: ")
    file = open("Accounts.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    login()

# Login function
def login():
    print ("Please login ")
    # Username input
    username = input("Please enter your username: ")
    # Password input
    password = input("Please enter your password: ")  
    for line in open("Accounts.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials, you are now logged in... ")
            return True
    print("Incorrect credentials, you are not logged in... ")
    return False, exit()

choice = input("Would you like to register or login to your account (register / login): ")
# Account register or login
if choice in ("REGISTER","register", "Register"," REGISTER"," register"," Register"):
    register()
if choice in ("LOGIN","login","Login"," LOGIN"," login"," Login"):   
    login()
if choice not in ("REGISTER","register", "Register"," REGISTER"," register"," Register","LOGIN","login","Login"," LOGIN"," login"," Login"):
    exit()

# Introduction
print ("Welcome to the Song Quiz Game - You have 2 chances to quess the name of each song")
time.sleep(0.5)
print ("You will recieve 3 points for a correct answer on the first guess and 1 point for a correct answer on the second guess")
time.sleep(0.5)
print ("The game will end when you incorrectly guess the name of a song")
time.sleep(0.5)
print ("Please type in lower case, good luck!")
time.sleep(0.5)
print ("")

# Defines goes
goes = 1

# Defines score
score = 0

while goes > 0:

    # Imports Songs.py
    import Songs

    # Defines variable from external file
    chosensong = Songs.song()

    # START OF LOOP (song generator and guesses)

    # defines guesses
    guesses = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ -123456789")

    # Number of turns
    turns = 2


    # Checks for letters in word                 
    for char in chosensong:

        if char in guesses:
        # Replaces letters specified with said letter
            time.sleep(0.1)
            print (char, end='')
            
        # Replaces letters that are not specified with "_"
        else:    
            time.sleep(0.1)
            print ("_ ", end='')

    print("")

    # START OF LOOP (song generator and guesses)
    while turns > 0:         
        
        # Guess input
        time.sleep(0.5)
        guess = input ("Guess the song: ")
        print ("")

        guesses += guess
            
        fails = 0             

        for char in chosensong:
            
            if char in guesses:
            # Replaces letters specified with themselves
                print (char, end='')
                
            # Replaces letters that are not specified with "_"
            else:    
                time.sleep(0.1)
                print ("_ ", end='')   
                #Add 1 to fails
                fails += 1
                   
        # Breaks loop if you guess correctly
        if fails == 0:
            #Counts score
            if turns == 2:
                score += 3
            if turns == 1:
                score += 1
            print ("")
            print ("Correct! Your current score is " + str(score) + " points")
            # Displays score
            print ("Next song:")
            print ("")
            
            break   

        # Looses turns if guess not correct   

        turns -= 1
        # Displays turn
        if turns == 1:
            print ("")
            print ("Incorrect! you have one more guess")
                
    # END OF LOOP (song generator and guesses)

    # Ends when turns hit 0
    if turns == 0:
        print ("")
        print ("Incorrect! the song was: " + chosensong)
        print ("")
        print ("Your total score was " + str(score) + " points")
        goes -= 1
        print ("")
        again = input("Would you like to try again (yes / no): ")
        if again in ("yes","YES","Yes"," yes"," YES"," Yes","y","Y","ye","YE","Ye"):   
            goes += 1
            score = 0
            print("")
        if again not in ("yes","YES","Yes"," yes"," YES"," Yes","y","Y","ye","YE","Ye"):
            exit()
        
