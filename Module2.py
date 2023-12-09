#module2

#name for this module is( __name__='__Modules1__')
'''
#Operation-01

import Modules1

Modules1.add(40,30)
Modules1.sub(40,30)
Modules1.mul(40,30)


this one currect way of importing the other class
'''
#__________________________________________________________

#Operation-02

from Modules1 import add,sub

add(30,60)
#mul(30,30)#error-> becasues we can'nt called this in the import funcation
sub(50,30)

'''
output=>
30
-10
200
90
0
'''
#---------------------------------------------------
import Module_aliasing as a

#Module_aliasing.add()  #===>Error
a.add()
