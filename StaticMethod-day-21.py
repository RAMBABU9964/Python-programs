#Static-variables and Static-methods
'''
@StaticMethod-->no default parameter
instanceMethod-->self default parameter
@abstrastmethod-->self as default parameter
@classmethod--> cls as default parameter

'''
#EX:-1
class student:
    @staticmethod
    def disp():
        student.name='ram'
        student.age=25
student.disp()
print(student.name)
print(student.age)

#creating Static Variable inside the constructor:-
class Demo:
    age=45#creating static variable outside any method and inside the class
    def __init__(self):
        self.x=10
        Demo.y=20 #creating static variable inside the constructor
    @staticmethod
    def disp():
        Demo.z=30 #creating static variable inside the ststicmethod
#print(Demo.y)3error
Demo.disp()
print(Demo.z)#30
d=Demo()
print(Demo.y)#20
print(Demo.age)#45
#---------------------------------------------------------------------------------
#EX:-2
class Table:
    @staticmethod
    def calculate(num):
        for i in range(1,11):
            print(num*i)
Table.calculate(int(input("Enter the number to display the table")))
