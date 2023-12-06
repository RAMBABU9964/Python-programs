#Exception Handling:-
'''
a=10
if a>20:
print(a)

-->try
-->except
-->else
-->finally

#UDEH:-User Defined Exception Handler.
*)Exception present-->except,finally
*)Exception not present-->else,finally
'''
#ex:-1
'''
def div(a,b):
    try:
        print(a/b)
    except:
        print("Exception occoured and handled")
    else:
        print("Present in else block")
    finally:
        print("Present inside finally block")
div(10,0)
'''
'''
def mydiv(func):
    def wrapper(a,b):
        if b==0:
            print("cannot divide by zero")
        else:
            func(a,b)
    return wrapper
@mydiv
def div(a,b):
    print(a/b)
div(10,0)
'''
#_______________________________________________________________________
#ex:-2
'''
def check(func):
    def wrapper(name):
        if name=='hi':
            print("cannot process")
        else:
            func(name)
    return wrapper
@check
def string_check(name):
    print(name)
string_check('hi')
'''
#***************************************************************************
#Ex-3
'''
Explaation:
the check_account_decorator takes a function func as an argument and defines a
wrapper function.

inside the wrapper function it check if the account number is in the specified
set of invalid account number.

if it is, it print a message. otherwise, it calls the original function (func)
with the provided account number.

the decorator is then applied to a sample function, process_account.
the decorated function, process_account is called with an account number as an argument.


decorators are used to add functionalities to the original functio, without
modifying the implimention original function.(original source code)
'''
'''
def check_account_decorator(func):
    def wrapper(kodnest_ID):
        blocked_kodnest_ids=(12345,1212,1313,1414)
        if kodnest_ID in blocked_kodnest_ids:
            print("cannot process account with blocked kodnest ID",kodnest_ID)
        else:
            func(kodnest_ID)
        return wrapper
@check_account_decorator
def process_account(kodnest_ID):
    print("processing account with kodnest ID:",kodnest_ID)

kodnest_ID=int(input("enter kodnest ID:"))
process_account(kodnest_ID)
'''
#*****************************************************************************
#Ex:-4


def disp(a,b):
    try:
        print(a/b)
    except:
        print("ZeroDivisionError:Exception Handled")
disp(10,0)

















































