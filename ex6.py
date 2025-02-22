import random #import the randint function

def u_choice(options):#function for the users choice
    y=input("make a choice:rock, paper, sissors or q to quit: ") #get user input
    
    #check user input
    if (y not in options and y!='q'):
        print("invalide")
        u_choice(options)#recursive call until the choice is valid
    else:
        return y #return user choice

def game(): #main game function
    while True: #loop to keep the game running
        options=("rock","paper","sissors") #define possible choices
        pc=random.choice(options) #generate random choice
        user=u_choice(options) #users choice
        
        print(f"user: {user}") #display users choice
        print(f"computer: {pc}") #display computers choice
        
        #check if the user wants to quit
        if(user=='q'): 
            print("end game")
            break #break the loop
        #determine the games outcome
        else:
            if(user==pc):
                print("draw") #if voth choices are the same
            elif(((pc=="rock" and user=="sissors") or(pc=="paper" and user=="rock") or (pc=="sissors" and user=="paper"))):
                print("you loose") #conditions where the user looses
            else:
                print("you win") #conditions where the user wins
                
        print("play again or quit") #prompt user to continue or quit

#main
game()#run the game