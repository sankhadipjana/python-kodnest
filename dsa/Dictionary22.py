print("\n\nstart Dictionary methods")
student = {
     'name': 'Amit',
     'age': 21,
     'age': 22,
     'course': 'Computer Science',
     'Tech': {'Computer Science', 'Python','Django', 'React'} 
}

    # student["age"] = 25
print(student, type(student), len (student))
print (student ["Tech"])
print(student. get("course"))
print (student. get("name"))
print(student.keys())
print(student.values())
print(student.items())
student. update({f"pincode" : 500008, "address" :
"hyd"})

student. pop("age")
student.popitem() # last element student. clear() # clears the dictionary
del student
print(student)

print("next part")

student = {
"name" : "Ravi",
"age" : 22,
"course": "Computer Science",
"Tech" : ["Computer Science", "Python",
"Django", "React"]
}
for x in student:
  print(x, "-", student[x])
for i in student.keys() :
  print(i)
for i in student. values():
    print(i)
for i in student.items():
  print(i)
stu_dic = student. copy()
stu_dic["rollno"] = 20
print (stu_dic)
print (student)


#Nestesd
stus = {
    "stu1": {
        "name" : "Ravi",
        "age" : 22
    },
    "stu2": {
        "name" : "Amit",
        "age" : 21
    },
    "stu3": {
        "name" : "Rahul",
        "age" : 23
    },
}
print (stus)
print (stus["stu2"]["name" ])