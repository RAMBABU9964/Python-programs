#Methods in python:
#1.no input and no output
def add():
    a=10
    b=20
    c=a+b
    print(c)
add()
#___________________________________________________________________
#2.no input but output
def add():
    a=10
    b=20
    c=a+b
    return c
result=add()
print(result)
#__________________________________________________________________________
#3.input and output
def add(a,b):
    return a+b
print(add(10,20))
     
#__________________________________________________________________________
#4.input and no output
def add(a,b):
    print(a+b)
print(add(10,20))#None
