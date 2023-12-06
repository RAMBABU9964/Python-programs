s1={10,40,30,20,60}
print(s1)
#set is not an ordered collection of data
#s2={10,40,30,20,60,60,30,10,40}  #sets do not allow duplicates

s1.add(500)
print(s1)

s1.remove(500)
print(s1)

s1.discard(600) #if the value is not present in the set it will not show the error 
print(s1)

#del s1  ==>to delect the complitly the set


s1.add(True)
print(s1)


s1.add("Ram")
print(s1)


s2={1,2,3}
s3={3,4,5}
union_set=s2.union(s3) #{1,2,3,4,5}
print(union_set)

union_result=s2|s3
print(union_result)#{1,2,3,4,5}

print(s2.intersection(s3))#{3}
print(s2&s3)#{3}


difference=s2-s3
print(difference)#{1,2}
print(s2.difference(s3))#{1,2}


s4={1,2,3}
s5={1,2}
#subset,superset
subset=s5.issubset(s4)
print(subset)

superset=s4.issuperset(s5)
print(superset)

set1={10,20,30,50,70,80}
#set2={500,600,700,800,True,"kodnest"}
set1.update({500,600,700,800,True,"kodnest"})
print(len(set1))
