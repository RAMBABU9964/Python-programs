my_dict1={'name':'ram','age':30,'status':'pass'}#key:value pair-duplicates not allowed #similar-key or not allowed
#duplicat values allowed

my_dict1['name']='prakash' #updating specific value of key in my_dict1
#my_dict1.pop('age')# valied to delect the key value pair
#my_dict1.popitem()#it alwayes delect last key-value pair
#del my_dict1['age']# valied to delect the key value pair
#my_dict1.clear() #{}#delect the my_dict1 completely


print(my_dict1)





my_dict2={'name':'rahul','age':26,'status':'fail'}
print(my_dict2)

#print(my_dict1.update(my_dict2))


student_names={'s1':'akash','s2':'vikas','s3':'reshma','s4':'pooja'}
print(student_names)
print(student_names.values())
print(student_names.keys())
print(student_names.items())

'''
values()-to display all the values from the dict
key()-to display all the keys from the dict
items()-to display all the key:value pair of the dict
'''
