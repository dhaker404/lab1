#functions
def readn(ch): #funtion to read input from user
    n=float(input("enter "+ch+" number: ")) #reads the input number
    return n
def readop():#function to read the operator
     op=input("enter an operator(+,-,*,/) or 'q' to quit: ")#reading the operator
     if op not in('+','-','*','/','q'):#check the operator 
         print("invalide")
         return readop()#recursive call until the operator is valid
     return op
#function to calculate the result
def result(x,y,op):
    if(op=='+'):
        return x+y#perform addition
    if(op=='-'):
        return x-y#perform substraction
    if(op=='*'):
        return x*y#perform multiplication
    else:
        return x/y#perform division 
    
#main calculator function
def calculator():
    while True:
        ch="first"
        x=readn(ch)#read the first number
        op=readop()#read the operator
        if(op=='q'):#check if the user wants to quit
            print("calculation stoped")
            break#exit the loop     
        else:
            ch="second"
            y=readn(ch)#read the second number
            print(x,op,y,'=',result(x,y,op))#calculate the result
        break



#main
calculator()#run the calculator