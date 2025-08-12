print("1")
print("2")
print("3")
print("4")
x = 45
print(x)
y= 56
x = 23
print(x)

# using square brackets
fruits = ["apple", "banana","cherry"]

# using list function
fruits2 = list(("apple", "banana","cherry","mango","kiwi" ,"mango"))

# print(fruits)
# print(fruits2)


# access elements of list
print(fruits[0])
print(fruits[-2])
print(fruits[-2])
print(fruits[0:3])

#change elements in list

fruits2[1] = "Kiwi"

print(fruits2)

# adding element
fruits2.append("grapes")

print(fruits2)
# add at specific position
fruits2.insert(1,"orange")

# add multiple elements
fruits2.extend(["pineapple","watermelon"])
print(fruits2)

# removing elements

fruits2.remove("mango")

#by index 
fruits2.pop(2)

#delete
#del fruits2

print(fruits2)

#useful methods in list

numbers = [4,3,2,8,7,6,9]
#numbers.sort()
#numbers.sort(reverse=True)

numbers.reverse()
print(numbers.count(7))
print(numbers)

a = "she is going to school"
b =a.capitalize()
print(b)
print(a.count("going"))


#dictionary
# d = {}
# print(type(d))


#using dict() function or constructor
my_dict = dict(name="Deepak Pal", age=20)
#print(type(my_dict))
print(my_dict.get("course"))
