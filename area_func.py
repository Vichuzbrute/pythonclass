def sq_area(s):
     return s*s
def ret_area(l,b):
    return(l*b)
def tri_area(B,h):
    return 0.5*B*h
s=int(input("enter side of square to find its area"))
l,b = map(int,input("enter the length and breadth of rectangle seperated by space to find its area").split())
B,h= map(int,input("enter the base and height of triangle seperated by space to find its area").split())
print("area of the square is", sq_area(s))
print("area of the rectangle is", ret_area(l,b))
print("area of the triangle is", tri_area(B,h))
