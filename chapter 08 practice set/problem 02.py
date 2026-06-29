f = int(input("enter temperature in fahrenheit : "))

def f_to_c(f):
    return 5*(f-32)/9
print(f"{round(f_to_c(f), 2)} Celsius")

