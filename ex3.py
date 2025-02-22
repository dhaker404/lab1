#functions

def read(): #funtion to read input from user
    ch=input("pw=") #reads the input password
    return ch

#function to find the longest substring with unique characters
def StrongIndependentPw(ch):
    if(len(ch)<8): #checking the length of the pw
        return False
    else:
        num=False #variable for numerical charcters
        up=False #variable for upercase charcters
        low=False #variable for lowercase charcters
        spe=False #variable for special charcters
        
        #checking each charcter in the password
        i=0
        while(i<len(ch)):
            print(i," ",ch[i]," ",num," ",up," ",low," ",spe," ",i<len(ch))
            if("0"<=ch[i]<="9"): #check for numerical charcters
                num=True
            elif("a"<=ch[i]<="z"): #check for upercase charcters
                low=True
            elif("A"<=ch[i]<="Z"): #check for lowercase charcters
                up=True
            else: #considering it's a special charcters
                spe=True
            if(num and up and low and spe): #stop the while loop if all conditions are met
                break
            i+=1
            
    return num and up and low and spe #returning ttrue if all conditions are met
            
            

#main


pw=read() #read imput from user
if(StrongIndependentPw(pw)):
    print("Pasword accepted") 
else:
    print("Password not strong enough")
