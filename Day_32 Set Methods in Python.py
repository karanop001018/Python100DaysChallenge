s1 = {1,2,5,6}
s2 = {3,4,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)





cities1 = {'Tokyo','Madrid','Berlin','Delhi'}
cities2 = {'Tokyo','Seoul','Kabul','Madrid'}
cities3 = cities1.union(cities2) # prints all values in both sets
print(cities3)

cities3 = cities1.intersection(cities2) # prints those values which are common in both sets
print(cities3)
cities1.intersection_update(cities2) # prints those value which are in both sets
print(cities1)

# Symmetric difference = (A U B) - (A ∩ B)
cities3 = cities1.symmetric_difference(cities2) # (A U B) - (A ∩ B)
print(cities3)

cities3 = cities1.difference(cities2)
print(cities3)


cities1 = {'Tokyo','Madrid','Berlin','Delhi'}
cities2 = {'Tokyo','Seoul','Kabul','Madrid'}
print(cities1.isdisjoint(cities2))


cities1 = {'Tokyo2','Madrid2','Berlin','Delhi'}
cities2 = {'Tokyo','Seoul','Kabul','Madrid'}
print(cities1.isdisjoint(cities2))


cities1 = {'Tokyo','Madrid','Berlin','Delhi'}
cities2 = {'Seoul','Kabul'}
print(cities1.issuperset(cities2))


cities1 = {'Tokyo','Madrid','Berlin','Delhi'}
cities2 = {'Seoul','Madrid','Kabul'}
print(cities1.issuperset(cities2))


cities1 = {'Tokyo','Madrid','Berlin','Delhi','Seoul','Kabul'}
cities2 = {'Seoul','Madrid','Kabul'}
print(cities1.issuperset(cities2)) # all elements of set2 must  be present in set1 then set1 is superset of set2
print(cities2.issubset(cities1))


cars1 = {'Lamborgini','Bugati','Supra','Range Rover'}
cars2 = {'Supra','Range Rover'}
print('\n',cars1,'\n',cars2)
print(cars2.issubset(cars1))
cars2.add('Lamborgini')
print(cars2)
cars1.remove('Range Rover')
# we can also use discard() instead of remove()


college = {'KPGU','Parul','GSFC'}
print(college)
cname = college.pop()
print(cname)

name = {'Karan','Omkar','Ansh','Tanisha'}
print(name)
del name
#used to delete a set, here 'name'
# print(name) #if we try to print name after deleting it then it will give us an error
name1 = {'Karan','Krishna','Krish','Kunal'}
print(name1)
name1.clear()
# clear() deletes all the members of the set instead of deleting the set itself like 'del'
#So, here  {'Karan','Krishna','Krish','Kunal'} the element of set name are deleted but the set name still exists
print(name1)


# checking that is the given element is present in the set or not
info = {'Karan','Omkar',19,True,3.6}
if 'Karan' in info:
    print('Karan is present in set info')
else:
    print('Karan is not present in set info')