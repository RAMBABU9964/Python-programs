#types of Methods
#1.Inheritance Method 2.Specialized Method 3.Overidden method
#example:
'''
class Demo:
    def play(self):                    #Inherited method
        print("Player is playing")
    def cook(self):
        print("Parent is cooking")
class Demo1(Demo):
    def Study(self):               #Specialized method
        print("studying")
    def cook(self):                #Overidden method
        print"child is cooking")

'''
'''
Inherited method:- are such method which are inhereted from parent class and its used as its
in child class in the above ex play method can be called as the inherited method

Overidden methodes:- are such methodes which are inherited frm parent class and modefied
occering to the child class requriment in above cook method is called as overidden meyhod

Specialized method:-are such methodes which are present in only in the child class
not in the parent class in the above ex study method also called as specilized method
'''

#super():
'''
class Demo:
    def __init__(self):
        self.x=20
class Demo1(Demo):
    def __init__(self):
        self.x=40
        super().__init__()
d1=Demo1()
print(d1.x)


#Method Chaining:

class GreatGrandParent:
    def cook(self):
        print("GreatGrandParent is cooking")
class GrandParent(GreatGrandParent):
    def cook(self):
        print("GrandParent is cook")
        super().cook()
class Parent(GrandParent):
    def cook(self):
        print("Parent is cooking")
        super().cook()
class child(Parent):
    def cook(self):
        print("child is cooking")
        super().cook()
        super(Parent,self).cook()
        super(GrandParent,self).cook()
c1=child()
c1.cook()
'''
'''
method chaining is process of calling one method from the another method
'''

#Constructor chaining
'''
Constructor chaining:- is the process of calling one constructor to the another constructor. constructor
chining or method chining are usefull when u want to invoke multiple constructor or methodes
one ofter another by instlizing only one insteanc of a class
'''

#Specialized method/magic method/dunder methode:
'''

the methodes which as  __ as the safex and __ perfex in there method name such methoder
are called as magic and dunder method

ex:-
     __init__
     __add__
     __sub__
     __mul__
     __str__
'''
























