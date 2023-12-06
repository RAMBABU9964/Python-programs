#List with integer elements
'''
list = list(eval(input()))
#number (n) to be removed
n=int(input())

#loop to traverse each element in list
#and,remove elements
#which are equals to n
for x in list:
    if x==n:
        list.remove(n)

#print list after removing given element
print(list)
'''

#single except block
def div():
    try:
        a=10
        b=0
        c=a/z
        print(c)
    except:
        print("ZeroDivisionError Handled")
div()

#Multiple Except Blocks

def dive():
    try:
        a=10
        b='kmoo'
        c=a/b
        print(c)
    except ZeroDivisionError:
        print("ZeroDivisionError")#10/0
    except NameError:
        print("NameError")#a/z(z is not defined)
    except TypeError:
        print("TypeError")#10/'kkk'
    except:
        print("some error handle")#default except block must be at last
dive()

'''
DrawBack of Multiple except block:in above example for NameError, TypeError or ZeroDivisionError it will
display the same message which is not proper so thata why we need to use multiple
blocks to display proper message or to perform certain tasks based on type of exception.
'''
#Exception handle in multiple method
def alpha():
    print("Connection of alpha established")
    a=10
    b=0
    print(a/b)
    print("Connection of alpha ended")
def beta():
    try:
         print("Connection of beta established")
         alpha()
         print("Connection of beta ended")
    except:
        print("Exception Handles")
def gamma():
     print("Connection of gamma established")
     beta()
     print("Connection of gamma ended")
    
gamma()
























     
    
