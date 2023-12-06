#inheritances in python
#singel inheritance:-
'''
class Demo1:
    def __init__(self):
        self.x=10
    def disp1(self):
        print("disp1 method of class demo1")
class Demo2(Demo1):
    def __init__(self):
        self.y=20
    def disp2(self):
        print("inside disp2 of class demo2")
d2=Demo2()
d2.disp2()
d2.disp1()
print(d2.y)
'''
#print(d2.x)#error-because child class has its own constructor so parent class
#constructor wont be invoked while creating an object of child class.
'''
while performing inheritance in python if child class dosent have his wone contracter
then his parent class will be called while creating an object of child class
'''

#2.Hierarchical inhreritance:
'''
class Demo1:
    def __init__(self):
        self.x=10
    def disp1(self):
        print("disp1 method of class demo1")
class Demo2(Demo1):
    def disp2(self):
        print("inside disp2 of class demo2")
class Demo3(Demo1):
    def disp3(self):
        print("inside disp3 of class demo3")
class Demo4(Demo1):
    def disp4(self):
        print("inside disp4 of class demo4")
        
d3=Demo3()
d3.disp1()
d3.disp3()
d4=Demo4()
d4.disp1()
d4.disp4()

'''

#Multilevel inheritance:
'''
class Demo1:
    def __init__(self):
        self.x=10
    def disp1(self):
        print("disp1 method of class demo1")
class Demo2(Demo1):
    def disp2(self):
        print("inside disp2 of class demo2")
class Demo3(Demo2):
    def disp3(self):
        print("inside disp3 of class demo3")
d3=Demo3()
d3.disp3()
d3.disp2()
d3.disp1()
'''
#3.Multiple inheritance:
class Demo1:
    def disp1(self):
        print("disp1 method of class demo1")
class Demo2:
    def disp2(self):
        print("inside disp2 of class demo2")
class Demo3(Demo1,Demo2):
    def disp3(self):
        print("inside disp3 of class demo3")

d3=Demo3()
d3.disp3()
d3.disp1()
d3.disp2()


'''
MRO(Method resolution order):conspect used in inheritance. its defind the order in which
the property or method serch form in the class mro is very use full in python
because python support multiple inheritanc
MRO followes below
1.first data meber r number function in child class checked in child 3 if its not present in child 3
then follow step 2
2. now data number r number function in to parent function left to right
every class will be serch for single number












