#Operations on list using built-in functions in python
lst1=[10,20,30,40,40,20]#===>we can store duplicat values into list
#add new value to lst1 we shoud append comend
lst1.append(500)#===>[10,20,30,40,40,20,500]  #list are mutable in nature meaning you can chang their contents(add,remove,modifyelement)#list are ordered collection of item
#list are defined using square brackets#in list we can store duplicate value
#lst1.pop(6)  ==>#[10,20,30,40,40,20]     #remove the indixe value through pop methode #lst1.pop() if u not pass any value on that time by defult valu last indixe value should be remove from the list
#lst1.remove(500) ==>#[10,20,30,40,40,20]  #this one also used to remove the value but not by indiex by telling value
#del lst1[6] ==> #[10,20,30,40,40,20] #del is keyworld to delect the value frome the list
#del lst1 ==> error #it will delect all the value in the list
#lst1.clear()#[] #===> it will clear the all data in the list it will not delect completly
print(lst1)
