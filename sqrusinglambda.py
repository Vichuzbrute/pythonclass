square = lambda a: a*a
rectangle = lambda l,b:l*b
triangle = lambda B,h:0.5*B*h

a=float(input("enter side of square:"))
print ("area of square=", square (a))

l= float(input ("enter length of rectange :"))
b= float(input ("enter breadth of rectangle :"))
print ("area of rectangle=",rectangle(l,b))

B= float(input ("enter base of triangle :"))
h= float(input ("enter height of triangle :"))

print("area of triangle",triangle (b,h))
