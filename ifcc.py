#syntax and example of if-else statement
'''
if condition:
    statement1 to be executed if condition is true
else:
    statement2 to be executed if condition is false
'''

#example
'''
age=
if age>18:
        print("he is eligible")

else:
    print("he is not eligible")

print("i am here")

'''
#syntax and example of if-elif-else statement
'''
if condition 1:
       statement to be exectued if condition is true
elif condition 2:
        statement to be exectued if condition is true
elif condition 3:
        statement to be exectued if condition is true
else condition 4:
        statement to be exectued if condition is false

'''

#example
'''
a=int(input("enter the age"))
if a>20:
        print("Yes")
elif a>=10:
         print("Yes1")
elif a>=30:
         print("Yes2")
else:
         print("Else part got executed")
'''

#Example
'''       
ch=input("Enter character ")
if ch=='a' or ch=='A':
        print(ch,'is vowel')
elif ch=='e' or ch=='E':
        print(ch,'is vowel')
elif ch=='i' or ch=='I':
        print(ch,'is vowel')
elif ch=='o' or ch=='O':
        print(ch,'is vowel')
elif ch=='u' or ch=='U':
        print(ch,'is vowel')
else:
        print(ch,'is consonal')
'''


#IN:

ch1=input("Enter character ").lower()
if ch1 in 'aeiou':
        print(ch1,'is vowel')
else:
        print(ch1,'is consoual')
#------------------------------------------
my_string="Hello world.."
if "Hello" in my_string:
        print("substring found")
#----------------------------------------
if 'Ram' in "Raja ram mohan roy":
        print("substring found")
else:
        print("Not found")
#-------------------------------------------------------
# 1.WWAP to check whether the number is present b/t 1-10.
num=int(input("enter the number"))
if num>1 or num<10:
        print("yes it is in rang of 1 to 10")
else:
      print("No it is not in the rang of 1 to 10")  
#--------------------------------------------------------------------
# 2.write a program to check whether a number is divisble by 5 or not
num1=int(input("enter the number"))
if num1%5==0:
        print("The given number is divided by 5")
else:
        print("The given number is not divided by 5")
#-----------------------------------------------------------------------

#calculater

