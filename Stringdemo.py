#Strings:
#different types of creating the strings:
s1="I'm Kodnest"#I'm Kodnest(invalid)

print(s1)
s2='''I'am "Kodnest" student''' #I'am "Kodnest" student  (invalid)            #this are differnt ways to declear the string in python

print(s2)
s3='''I
        am
             Kodnest'''#multiline string

print(s3)
s4="""I
        am
            Kodnest"""#multiline string

print(s4)
#___________________________________________________________________________________
#comparing mutable and inmutable
lst=[10,20,30]
print(lst)
lst.append(400)
print(lst)

#inmutable
s1="Hema"
print(s1)
s1.upper()
print(s1)
s2=s1.upper()
print(s2)

'''in python string are inmutable means onces we creat the strings we cant
modifey the string if the string triyed to be modifyed it will create new
string and new string object as to be printed then reference verable shoud
be ther pointing towards new string object'''

#title
s="the TimeS Of iNDia"
print(s.title())#The Times Of India ====>#it print all the first crater are in the uppercase
print(s.capitalize())#The times of india ===>it will print the first caracter in the uppercase

'''title(): is used to conver first character of each world present in the string in upper case
            and all the remaining characters in lowercase

   capitalize():is used to convert first character of the first world in string in
                 upper case and all the remaining character in lower case'''

s7='The time of india'
print(s7.split())

#____________________________________________________________________________________
# DAY-11
s1="Hello"
s2="World"
print(id(s1))
print(id(s2))
print(id(s1[2]))
print(id(s2[3]))

'''
String interning is like a memory-saving strategy where, instead of creating a new
memory space for each string, python checks if a string with in the same content a
already exists.
if it does the new string is just a reference to the existing one saving memory by
avoiding duplicate storage.
this process is called as string interning in python.
'''
#_________________________________________________________________________________


#Comparison of Strings:
#case:1=>
v1='Kodnest'
v2='Happy'
if v1==v2:                          #values are not same
    print("values are same")
else:
    print("values are not same")

if id(v1)==id(v2):                   #id are not equal
     print("id are equal")
else:
    print("id are not equal")



#CASE:2=>

v3='kodnest'
v4='KODNEST'

if v3==v4:                          #values are not same
    print("values are same")
else:
    print("values are not same")

if id(v3)==id(v4):                   #id are not equal
     print("id are equal")
else:
    print("id are not equal")



#CASE:3=>


v5='kodnest'
v6='KODNEST'
v5=v5.lower()
v6=v6.lower()
if v5==v6:                          #values are same
    print("values are same")
else:
    print("values are not same")

if id(v5)==id(v6):                   #id are not equal
     print("id are equal")
else:
    print("id are not equal")


#CASE:4=>

v7='kodnest'
v8='kodnest'

if v7==v8:                          #values are same
    print("values are same")
else:
    print("values are not same")

if id(v7)==id(v8):                   #id are equal
     print("id are equal")
else:
    print("id are not equal")


#____________________________________________________________________________

#STRING FORMATTING:-->

name='ram'
age=25
print(f"My name if{name} and My age is{age}")

print("My name if {} and My age is {}".format(name,age))


r1='Python'
r2='Java'
r3='SQL'
print("{1},{0} and {2} are amazing language".format(r3,r2,r1))
#Java,SQL and Python are amazing language

#______________________________________________________________________________
#DAY-12==>
'''
String Fromatting=>

in python the f string prefix and the .format() method are both used for string
formatting allowing you to embed expression and variable within string. They are
usefull for creating dynamic string where the values can changes.
'''

























