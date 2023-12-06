#day-19
#Printing an object reference:
#print(object)--->(__str__())

class Demo:
    def __init__(self):
        self.name='ram'
    def disp(self):
        print("Inside disp")
    def __str__(self):
        return self.name
d1=Demo()
print(d1)
d2=Demo()
print(d2)


#Adding object reference using+:
class Demo1:
    def __init__(self):
        self.x=10
    def __add__(self,other):
        return self.x+other.x
d3=Demo1()
d4=Demo1()
print(d3+d4)


#object-object(__sub__())
class Demo2:
    def __init__(self):
        self.x=10
        self.y=20
    def __sub__(self,other):
        return self.x-other.y
d5=Demo2()
d6=Demo2()
print(d6-d5)


'''

Operater overloading:- is the process of providing and additional meaning to an operater
so that an operater can profam the additional task other then its orginal meaning
'''
'''
class Calculator:
    def calculate(self,a,b):
        print("calculator function")
class add(Calculator):
    def calculate(self,a,b):
         print(a+b)
class sub(Calculator):
    def calculate(self,a,b):
         print(a-b)
class mul(Calculator):
    def calculate(self,a,b):
         print(a*b)
class div(Calculator):
    pass
def permit(ref,a,b):
    ref.calculate(a,b)

def main():
    a=int(input("enter first number"))
    b=int(input("enter first number"))
    ca=add()
    permit(ca,a,b)
    permit(sub(),a,b)
    permit(mul(),a,b)
    permit(div(),a,b)
main()   
'''




class add:
    def calculate(self,a,b):
         print(a+b)
class sub:
    def calculate(self,a,b):
         print(a-b)
class mul:
    def calculate(self,a,b):
         print(a*b)
class div:
    pass
def permit(ref,a,b):
    if type(ref).__name__=='div':
        print("Div class does not have calculate function")
    else:
        ref.calculate(a,b)

def main():
    a=int(input("enter first number"))
    b=int(input("enter first number"))
    ca=add()
    permit(ca,a,b)
    permit(sub(),a,b)
    permit(mul(),a,b)
    permit(div(),a,b)
main()   



#Day-20
#Duck Typing/Dynamic Typing
'''
Duck typing is also called as Dynamic typing which is allowes objects of different types
(class) to be passes for the same type referencess Duck typing is came for the folling
statemnt " If walks like a duck,
            if it quads like a duck
           then it must be a duck "

        



























    
    
        
   






































