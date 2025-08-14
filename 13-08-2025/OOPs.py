# class student :

# student1 = ("name":"rohan", "age":17, "course":"Mern")
# student2 = ("name":"amit", "age":25, "course":"Mern")
# student3 = ("name":"shahil", "age":22, "course":"Mern")
# student4 = ("name":"Rishabh", "age":23, "course":"Mern")

class student:
    def __init__(self,name,course,age ): #constructor will initialize and object and attach property
        self.name = name
        self.course = course
        self.age = age

s1 = student("Rohan" , 17, "Mern")
s2 = student("amit" , 17, "Mern")
s3 = student("Rahul" , 17, "Mern")
s4 = student("Rohit" , 17, "Mern")



print(s1)
print(s1.name)
print(s1.course)
print(s1.age)

        