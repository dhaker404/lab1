#functions

def read(): #funtion to read input from user
    n=int(input("n=")) #reads the input number
    return n

def fact(n): #function to calculate the factorial of a given number n
    f=n #initialise f with the input number
    
    for i in range(n-1,1,-1):#loop that goes from n-1 to 2
        f*=i #multiplies f by i
    return f #returns the result



#main
n=read() #read imput from user
print("fact(",n,")=",fact(n)) #factorial and display