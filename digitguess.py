print("-----digit guess game---")
import random
number=random.randint(1,10)
attempts=0
max_attempt = 5
for attempts in range(max_attempt):
    try:
        guess=int(input("guess a number between 1 and 10: "))
        if guess<1 or guess>10:
            print("enter a number between 1 and 10")
            continue
        attempts+=1 
        if guess==number:  
            print("you win") 
            break
        elif guess<number:
            print("too low")
        else:
            print("too high")
    except ValueError:
        print("enter only integer")

if number!=guess:
    print(f"you lose. the number was {number}")



