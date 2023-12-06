#for loop:
#(initialization,condition,incrementatio/decrementation)
'''
for i in 'kodnest':
    print(i)
for i in 'kodnest':
    print(i,end='')
print()
'''
#-----------------------------------------------------------------------
# WAPP to print all the vowels present in the string entered by the user
'''
string=input("Enyter the string")
for ch in string:
    if ch in 'aeiouAEIOU':
        print(ch)
print()

for ch in string:
    if ch not in 'aeiouAEIOU':
        print(ch)
'''
#-------------------------------------------------------------------
#in operater use in list
'''
lst1=[10,20,True,'kodnest',7+8j]
print(20 not in lst1)#false

print(True in lst1)#true
'''
#-------------------------------------------------------------
#in operater use in dict
'''
d1={1:'one',2:'two'}
print(1 in d1)#true
print('one' in d1)#false because the in operator in dict only check the key not values
print('Two' not in d1)#true
'''
#----------------------------------------------------------------------
#range()
#WAPP to print number from 1-10 using for loop:
#-->range (Start ,end-1,steps)
#-->range(default_valu_is 0,mandatory to give(no default value),default_value_is+1)
#-->for positive steps-start_value<end_value
#-->negative steps-start_value>end_value
#-->end='':the end='' parameter in the print() specifies that a space character should be used
# at the end of the prit statement instead of the default newline character. this result in the number
# beigng printed on the same line separated by spaces.
'''for i in range(1,11,1):
    print(i,end='')'''
#------------------------------------------------------------------------------------------------------------------
#print(range(1,11,1))#(1,11)

#example
tup=tuple(range(1,11,1))#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lst=list(range(1,11,1))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#-------------------------------------------------------------------------------
#eval():it is used to evelate a string as apython expression and return the result.it allowes you to execte python code represented as string
#syntax:eval(expression)
#expression:A String containing the valid python expression
'''a='123+50'
print(eval(a))#173
b='123.66+66.99'
print(eval(b))#190.6499999999999
c='5+7j+6j'
print(eval(c))#(5+13j)
d='True'
print(eval(d))#True'''

#-----------------------------------------------------------------------------------
#WAPP to print all the even element from the list
#note:take the list element from the user
'''count=int(input("enter number of element in the list"))
lst1=[]
for i in range(count):
    ele=int(input("enter the list element"))
    lst1.append(ele)
print(lst1)
eve_lst=[]
for i in lst1:
    if i%2==0:
        even_lst.append(i)
print(even_lst)'''

#list comprehension:[expression for item in iterabble if condition]
'''lst=list(eval(input("enter comma seperated element for the list")))
print([i for i in lst if i%2==0])'''
#-----------------------------------------------------------------------------
'''lst=[1,2,3,4,5,6]
sq=[i**2 for i in lst]'''

'''lst1=[10,20,-50,-60,-30]
positive_lst=[i for i in lst1 if i>0]'''

'''names=['Anika','Ankit','Nikita','Ayush','Punith','Deep']
name_a=[i for i in names if i[0]=='A']'''
#---------------------------------------------------------------------------
''' list comprehension allows you to generate a new list by applying an expression
to each item in an iterable.(list,tuple,range)'''

#break and continue:
#WAPP to print number from 1-10 and stop the printing if number is 5.
for i in range(1,11):
    if i==5:
        break
    print(i)
print("The loop terminated")

for i in range(1,11):
    if i==5:
        continue
    print(i)
print("The loop terminated")

