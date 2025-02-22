#functions

def read(): #funtion to read input from user
    ch=input("ch=") #reads the input string
    return ch

#function to find the longest substring with unique characters
def lsub(ch):
    ch1=""#substring to store unique characters
    sub=""#variable to store the longuest substring so far
    
    for i in range(len(ch)):#go through each character in the string
        
        if(ch1.find(ch[i])==-1):#if the charcter isn't in ch1, append it
            ch1+=ch[i]
        else:
            if(len(ch1)>len(sub)):
                sub=ch1#if ch1 is the current longuet substring, update it
                ch1=ch[i]#starts a new substring
    return sub#returns the longuest substring



#main
ch=read() #read input from user
print("longuest unique substring: ",lsub(ch)) #display resolt
