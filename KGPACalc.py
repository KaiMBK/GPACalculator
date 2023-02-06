#This is a standard GPA calculator. 

classnum = int(input("Welcome to Kai's GPA Calculator. To begin, enter the number of classes you have taken:" ))
i=0
#classnum & i, defined above, are used to control how many times the code iterates.
cc=0
cp=0
#cc & cp stand for 'cumulative credits' and 'cumulative points' respectively. 
#These will be used to calculate the final GPA, and must be defined outside of the while loop below.

while i<classnum:
    i+=1
    grade=int(input("What was your grade for class #" +str(i)+"? Enter a number(A=4, B=3, etc.): "))
    credits=int(input("How many credits was class #" +str(i)+"? Enter a number: "))
    cc=cc+credits
    cp=cp+(grade*credits)
    ans=str(input("Your grade in class #"+str(i)+" was "+str(grade)+", and it was worth "+str(credits)+" credits. Is this correct?(y/n)"))
    if ans=="y":
        continue
    elif ans=="n":
        i+=-1
        cc=cc-credits
        cp=cp-(grade*credits)
    else:
        ans=str(input("Please respond with either 'y' or 'n': "))
        if ans=="y":
            continue
        elif ans=="n":
            i+=-1
            cc=cc-credits
            cp=cp-(grade*credits)
        else:
            ans=str(input("Please respond with either 'y' or 'n': "))
#lines 17 ~ 33 are to enable users to correct a mistaken input without having to run the whole code again. 
#the multiple if/else statements are necessary to deal with users giving input other than the anticipated "y" or "n".
#lines 26~33 are a secondary safety net to catch inputs other than "y" or "n".

cgpa=cp/cc
print("Your GPA is: " +str(cgpa))