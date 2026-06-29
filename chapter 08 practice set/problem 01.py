a = int(input("enter number a : "))
b = int(input("enter number b : "))
c = int(input("enter number c : "))

def greatest(a,b,c):
    if(a>b and a>c):
        print("a is greatest")
    elif(b>a and b>c):
        print("b is greatest")
    elif(c>a and c>b):
        print("c is greatest")        

greatest(a,b,c)        