info = {
    "key" : "task",
    "name" : "Krish",
    "learning": "Python"
}

print(info)

dict= {
"name" : "Krish" ,
"cgpa" : "9.0",
"marks" : [98,97,96]
}

print(dict)

dict= {
"name" : "Krish" ,
"cgpa" : "9.0",
"marks" : [98,97,96],
"age" : 19,
"can_drive" : True
}

print(dict)

print(type(dict))

dict= {
"name" : "Krish" ,
"cgpa" : "9.0",
"marks" : [98,97,96],
"age" : 19,
"can_drive" : True
}


dict["name"] = "Rakazaka"

print(dict["name"])
dict["surname"]= "Jain"

print(dict["name"])
print(dict["surname"])

student = {
"name" : "Krish",
"age" : {
    "of your friend" : 18,
    "of your brother" : 19,
    "of your best friend" : 18
}
}

print(student)

dict= {
"name" : "Krish" ,
"cgpa" : "9.0",
"marks" : [98,97,96],
"age" : 19,
"can_drive" : True
}

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("cgpa"))
dict.update({"city":"Hyderabad"})
print(dict)

collection = {1,2,3,4,1,2,4,1,3,12,3,4,2,4,}
print(collection)

print(type(collection))
print(len(collection)) #this gives us the number of unique elements in the set

collection = {1,2,3,4,5}
collection.add(6)
collection.remove(4)

print(collection)
print(collection)


collection = {1,2,3,4,2,5,3,4,2,4,5}
collection.clear()
print(collection)

collection = {1,2,3,5,8,21}
collection.pop()
print(collection)

collection.pop()
print(collection)

collection.pop()
print(collection)

print(collection.pop())
print(collection.pop())

collection_1 = {1,2,3}
collection_2 = {4,5,6}

rakazaka= collection_1.union(collection_2)

print(rakazaka)

collection_1 = {1,2,3,4,5,6}
collection_2 = {4,5,6,7,8,9}

shimataro= collection_1.intersection(collection_2)

print(shimataro)


subjects = { "python" , "java", "C++" , "python" , "javascript" , "java", "python", "java", "C++" , "C"}

print(len(subjects))















