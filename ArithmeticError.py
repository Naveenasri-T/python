a=int(input("enter the number:"))
b=int(input("enter the number:"))
try:
    c=a/b
    print(c)
except ArithmeticError:#error ocured during the calculation 
    print("it make a Arithematic error")