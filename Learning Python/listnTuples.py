# List are created via [] brackets

# a = [1,2, 'Arjun', 4.1, True, False, None] #
# print (a)
# print(a[1])
# print(a[10])# shall throw error because this is out of range 
# a[0]= 100 # we can update the list however this is always in order
# print(a)
# print(a.sort())
# print(a)

# l1 = [1,2,3,7,0,2]
# l1.sort()
# l1.reverse()
# l1.append(99) # adds at the end of the list
# l1.insert(2,455) # updates at the set index
# print(l1)


#Tuples

# t = ( 1, 3,5,8,9, 199, 'arjun')
# q =(1,)# you always keep comma to have it a tuple
# #Cannot update the tuple 
# print(type(t))
# print(type(q))
# print(q.count(3)) # gives you the value of how many times a particular object exists

#Enter the list of fruites

f1 = str(input("Enter the name of the fruit please\n "))
f2 = str(input("Enter the name of the fruit please\n "))
f3 = str(input("Enter the name of the fruit please\n "))
f4 = str(input("Enter the name of the fruit please\n "))
f5 = str(input("Enter the name of the fruit please\n "))
f6 = str(input("Enter the name of the fruit please\n "))
fruitList = (f1,f2,f3,f4,f5,f6)
print(fruitList)