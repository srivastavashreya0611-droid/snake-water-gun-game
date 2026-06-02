import random
'''-1 --->snake,
    0 --->water,
    1 --->gun
'''
print("Welcome to the Snake, Water, Gun Game!")
print("Rules: Snake drinks Water, Water douses Gun, Gun kills Snake\n")

d={'snake':-1,'water':0,'gun':1}
d1={-1:'snake',0:'water',1:'gun'}

user_score = 0
computer_score = 0

for i in range(5):
    print("\nRound", i+1)
    
    user = input("Enter your choice(snake, gun, water): ")
    usernew=user.lower()

    if usernew not in d:
        print("Invalid input")
        continue

    computer=random.randint(-1,1)
    u=d[usernew]

    print("Computer chose:", d1[computer])
    print("You chose:", usernew)
    
    if(computer==u):
        print("It's a tie!")
    elif((computer==-1 and u==0) or
        (computer==0 and u==1) or 
        (computer==1 and u==-1)):
        print("You lose!")
        computer_score += 1
    else:
        print("You win!")
        user_score += 1
    print("Current score:")
    print("Your score:", user_score, '| Computer score:', computer_score)    
    

print("Final score:")
print("Your score:", user_score)
print("Computer score:", computer_score) 

if user_score > computer_score:
    print("Congratulations! You won the game!🎉🎉")
elif user_score < computer_score:
    print("Sorry! You lost the game.😢😢")      
else:    
    print("It's a tie!")
