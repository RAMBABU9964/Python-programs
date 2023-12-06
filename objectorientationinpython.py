#Object Orientation in python
'''
class Student:
    def _init_(self):
        self.marks=34
        self.age=20
        self.name='ram'
    def disp(self):
        a=50
        print(a," inside dicp method")
s1=Student()
s1.disp()
print(s1.marks)
'''

#day-13
'''
Self:will alwayes holds an address of an current object  'Self' is not a keyword
'self' is the default parameter for all tht method present inside class
#for self, programmer no need to send any argument.
'''
#Employee:
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age                          #Instance Variable
        self.salary=salary
    def work(self):                 #member function
        print(self.name,"is working") #self.name=Accessing instance variable inside class using self
    def play(self):
        print(self.name,"is playing")
emp1=Employee('Ram',25,85000)
emp2=Employee('shyam',25,58000)#creating an object
print(emp1.name)#Accessing instance variable using object name
print(emp1.age)
print(emp1.salary)

emp1.work()#Accessing member function for object having name emp1
emp1.play()#Accessing member function for object having name emp1

print(emp2.name)#Accessing data member for object emp2
print(emp2.age)
print(emp2.salary)

emp2.work()#invoking member function for object having name emp2.
emp2.play()#invoking member function for object having name emp2.


'''
__main method in python:
            in python main method is not mandatory but if programmer want
            creat main() yes he can creat like:-
            def main():
               //block of code inside main()

in this, if programmer wants to invoke main() he has to only call the main(), like
   main():-

   def main():
      print("I am inside main method")
   main() #calling main()


'''

print("Outside the class statement")
class Demo:
    print("Inside the class statement-01")
    def __init__(self):
        self.x=10
    def disp(self):
        print("inside disp()")
    print("Inside the class statement-02")
d1=Demo()
d2=Demo()

class Demo1:
    a=10
    print(a)


'''
1.the flow of execution refers the order ion which statement are executed.
2.the execution will always start from the first statemnt.
3.one line will be executed at atime from top to bottom.
4.Method/functions definition will not alter the fiow of execution as statement
inside the method will be executed when the programmer call/invoke the method.
5.When control comes inside the class all the statement which are not the part
of constructor and method , will be executed.
'''

















  
