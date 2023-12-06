'''
Access Modifier :- Are used to determind accessiablety of data member in pythod
they are three access modifier as shown below
1)--> a(public)
2)--> _a( _:-Protected)
3)--> __a( __:-private)
'''
#Take the string input from the user and the first character of every string should be capital
'''s=input("Enter the String")
print(s.title())'''

#enter two input from the user one is string and another one is acharacter
'''
r=input('Enter the string')
c=input('enter the character which you want to remove from the string')
print(r.replace(c,''))
'''

#append() and extend():
'''
lst=[10,20,30]
lst.append(40)
lst.extend([50,60,70])
'''

#wapp tp print
'''
******
******
******

row=int(input("enter the "))
col=int(input("enter col "))
for i in range(row):
    for j in range(col):
        print("*",end='')
    print()
'''
#incresing patter
'''
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()
'''
#decreasing start pattern
'''
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end='')
    print()
'''





#Examples of access modifiers:
#public access Modifiers:
'''
class Employee:
    def __init__(self):
        self.x=10
    def disp(self):
        print(self.x)#Accessing inside the same class in which it has declared
e=Employee()
print(e.x)#Accessing outside the class
e.disp()
class Employee1:
    def disp1(self):
        print(e.x)#Accessing inside another class
        #print(self.x)#Error
e1=Employee1()
e1.disp1()

class Employee2(Employee):
    def disp2(self):
        print(self.x)#Accessing variableinside child class using self.
        print(e.x)
        print(e2.x)
e2=Employee2()
e2.disp2()
'''           
'''
public(members):
(attributes and methods) are accessible anywhere inside or outside the class in which
they are created as well as inside the another class
EX:-self.x<--This is instance variable which is publicy accessible.

--> In python there is no strict protected access modifier.
-->However ther is name convention(e.g__X) commonly used to indicate that the member
   (method and attributes) are created for internal use (within aclass and in it's
   subclass) it can be still accessed outside the class
'''

#Protected Access modifiers
'''
class Employee:
    def __init__(self):
        self._x=10
    def disp(self):
        print(self._x)#Accessing inside the same class in which it has declared
e=Employee()
#print(e._x)#Accessing outside the class
e.disp()
'''
'''class Employee1:
    def disp1(self):
        print(e._x)#Accessing inside another class
        #print(self._x)#Error
e1=Employee1()
e1.disp1()'''
'''
class Employee2(Employee):
    def disp2(self):
        print(self._x)#Accessing variableinside child class using self.
        print(e._x)
        print(e2._x)
e2=Employee2()
e2.disp2()
print("")
print("")
'''
#private Access modifiers:

class Employee:
    def __init__(self):
        self.__x=10
    def disp(self):
        print(self.__x)#Accessing inside the same class in which it has declared
e=Employee()
#print(e.x)#Error-Accessing outside the class
e.disp()
print(e._Employee__x)

class Employee1(Employee):
    def disp1(self):
        print(self._Employee__x)
        print(e._Employee__x)
        print(e1._Employee__x)
        #print(self.__x)#error
        #print(e.__x)#error
        #print(e1.__x)#error
e1=Employee1()
e1.disp1()

class Employee2:
    def disp2(self):
        print(e._Employee__x)#Accessing variableinside child class using self.
        
e2=Employee2()
e2.disp2()

'''
1.privite numbers (attrubat and methodes) can be access onely inside the same class
  in which they are decleared
'''
'''
#Data mangling / name mangling:-
                                is the process of providing new name for the privite
                        data member or member function in the format of _className__
                        variableName
            ex:- self.__x/def__disp(self):
               _Employee__x/e._Employee__disp()//o/p
             e.__x/e.__disp()//error

'''







        
