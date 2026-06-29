a = int(input("enter your age : "))

if(a>=18):
    print("you are above the age of consent")

elif(a<0):
    print("you are entering an invalid negative age")

elif(a==0):
    print("you are entering 0 which is an invalid age")
    
else:    
    print("you are below the age of consent")

print("end of program")     