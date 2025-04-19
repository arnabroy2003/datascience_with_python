# fruits = ["apple","banana","cherry","orange"]
            #0      #1         #2       #3
         #-4       #-3         #-2      #-1

# fruits[1] = "Mango"

# fruits.append("grapes")
# fruits.append("Kiwi")
# print(fruits)

# fruits.insert(1,"grapes")
# fruits.insert(4, "kiwi")
# print(fruits)

# fruits.remove("banana")
# print(fruits)

# fruits.pop()
# print(fruits)

# print(len(fruits))

# fruits = ["apple","banana","cherry","orange"]

# for i in fruits:
#     print(i)

# animallist = []
# for i in range(4):
#     value = input("animal name: ")
#     animallist.append(value)
# print("list:", animallist)

# user= input("Enter all items with space: ").split()
# print("user list:", user)

# numbers = [1,2,3,4,5,6,7]
# print(numbers[::2])

# fruits = ("apple","banana","orange")

# student = {"name":"John","age":19,"course":"python"}
# # print(student["name"])
# # print(type(student))
# student["city"] = "Kolkata"

# student["age"] = 20

# student.pop("course")
# print(student)

# print(student.keys())
# print(student.values())
# print(student.items())

# if "age" in student:
#     print("Present")
# else:
#     print("Not present")

# a,b = 10,20

# for key,value in student.items():
#     print(key,":",value)

# student = {
#     "s1": {"name":"Siddhant","age":19},
#     "s2": {"name":"Debipankaj","age":20}
# }

# print(student["s2"]["age"])

friends = {
    "sid": "112345678",
    "raj": "9876543210",
    "hari": "00000000"
}
name = input("Enter a friend's name: ")
if name in friends:
    print(f"{name}'s phone number is: {friends[name]}")
else:
    print("Friend not there.")
