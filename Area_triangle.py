"""
semi perimeter (s) = (a+b+c)/2
area = square root of (s*(s-a)*(s-b)*(s-c))
"""
a= int(input("enter the first side: "))
b= int(input("enter the second side: "))
c= int(input("enter the third side: "))
s= (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area is :" , round(area,2))



