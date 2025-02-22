from random import randint #import the randint function

def game(r): #main function for game    
    while True:
        n=int(input("guess the number between 1 and 100: ")) #read user input
        if not(1<=n<=100):#check if the users number is in the valid range
            print("number invalide")
            game(r)
        #checks if the users number is hight or low
        elif(n>r):
            print("too hight")
            game(r)
        elif(n<r):
            print("too low")
            game(r)
        else:#consider the users number equals the rgenerated number
            print("you win")
            break #ends the game


#main
r=randint(1,100) #generate the random number to guess
game(r)#run the game