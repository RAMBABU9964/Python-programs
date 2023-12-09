#modules in python===>
'''
1.a python module is a file cantaning python functiones, class and other statements or instraction
2. we can import one module into another module with the help of import statement
3. to import Secific function or statement we have to use the sentxes from module name import sentex name

Spical variable __name__ :=>
1. If you want to run specific code only when a module is executed directly (not
   imported as a module into another script), you can use the __name__ variable
2. When a python script is executed, the __name__ variable is set to " __main__" if the
    Script is being run directly.
3. If the script is being imported as a module into another script , __name__ is set
   to the name of the imported module.

'''

#module1

#name for this module is( __name__='__main__')

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)

#operation-03:
    '''
if __name__=='__main__':
    add(10,20)
    sub(10,20)
    mul(10,20)
'''

#operation-04:
    
if __name__=='Modules1':
    add(10,20)
    sub(10,20)
    mul(10,20)
    
