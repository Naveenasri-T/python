def gcd(x,y):
 while y!= 0:

  x,y = y , x%y
  print(x)
a= int(input("enter the number:"))
b= int(input("enter the number:"))
print(gcd(a,b))
