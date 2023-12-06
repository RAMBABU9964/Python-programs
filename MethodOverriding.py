'''
Method overloding is the process of creating multipal method having same name but different parameter
inside the same class
'''
#constructor overding is the process as creating multipale constructors having
#different parameter inside the same class.
#example
class Employee:
    def work(self):
        print("Employee-01 is working")
    def work(self,name):
        print("Employee-02 is working")
    def work(self,name,age):
        print("Employee-03 is working")
emp1=Employee()
#emp1.work()#error
#emp1.work('Akash')#error
emp1.work('Akash',36)


'''
1.Method overloading is not possible in python.
2.Whenever we are trying to creat multiple methods having same name with different
parameters, only the last defined method can be invoked.
and all the previous method become useless as well cannot invoke them.
'''
