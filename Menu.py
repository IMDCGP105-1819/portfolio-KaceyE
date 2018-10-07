import time
import sys


ans = True

while ans:


    menu = input ("""

    1. Beer bottles

    2. Info sheet

    3. End
    
    Please select and option: """)

    if menu == "1":
        bottles = 99

        while bottles != 0:
            bottlesFalling = bottles - 1
            print (str(bottles) + (" bottles of beer on the wall, ") + str(bottles) + (" bottles of beer. Take one down, pass it around, ") +  str(bottlesFalling) + (" bottles of beer on the wall... "))
            time.sleep(0.5)
            bottles = bottles - 1
            
            if bottles == 0:
                print ("No more bottles of beer on the wall, no more bottles of beer.")
                sys.exit
    
    elif menu == "2":
        gdpr = input ("Are we able to collect some information about you?: ")

        if gdpr == "yes":
            name = input ("What is your name: ")
            if len(name) > 3:
                print("Please enter more than 3 characters")


    elif menu == "3":
        sys.exit
