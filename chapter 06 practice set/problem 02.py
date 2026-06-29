s1 = int(input("enter marks : "))
s2 = int(input("enter marks : "))
s3 = int(input("enter marks : "))

# check for total percentage
total_percentage = ((s1 + s2+ s3)/300)*100

if(total_percentage>=40 and s1>=33 and s2>=33 and s3>=33):
    print("you are passed")
    
else:
    print("you failed")    


