# lecture 4

'''
dictionary: Dict type, mutuable, unordered, dont duplicate keys
starts with, = {} and use :

manner= "key" : value
for print, specific key, use[] like print(disc["..."])
'''
# info={
# "name" : "siddharth",
# "age" : 26,
# "height" : 5.10,
# "marks" : [12,15,95],
# "loyality" : True

# }
# print(type(info))
# # print(info)
# print((info["name"]),(info ["age"]))



# info ={
# "name" : "siddharth",
# "age" : 26,
# "height": 5.10,
# "marks" : [12, 12, 56],
# "loyal" : True,
# 26.99: 56}
# info["name"] = "sid" #mutable
# info["surname" ] = "kumar" # we add anything later


# print("Name: " , info["name"])
# print(info["surname"])
# print(info["age"])
# print(info["height"])
# print(info["marks"])
# print(info["loyal"])
# print(info[26.99])
# -------------------------
# print(info)
# print(type(info))
''' we above or below code for sepearate line print
# for key, value in info.items():
#     print(key, ":", value)
'''
#null Dictionary

# null_Dict = {}

# print(null_Dict)
# print(type(null_Dict))

# null_dic ={}
# print(null_dic)
# print(type(null_dic))
# ----------------
#nested disctionary: ek ke andar ek aur disctionary same like if if if or ifeliflelif

# student= {
# "name" :"siddharth kumar",
# "subject" : {
#     "maths": 98,
#     "chemistry": 78,
#     "physics" : 93
# }


# 
# print(student["subject"]["physics"])
##LEft to right ----> solve: if we want physics marks then think like open folders 

# again practice disc nest
# student ={
# "name" : "Siddharth kumar",
# "age" : 26,
# "subject": {
#     "maths": 56,
#     "chem" : 58,
#     "phy" : 87
# }
# }
#keys: immutable | values: mutable or changeable
# print(student)
# print(type(student))
# print(student["subject"])
# print(student.values()) #prints values of dictionary shows
# print(student.keys()) # prints keys of dictionary shows
# print(student.items()) #all items get in Tuple form
# print(list(student.items())) # list ke form me items(key with values) milega 

#in other ways if i get items (key with value) by index value, 
#so firstly we need convert in list[](because tuple is immutable so index or saving not worked)
# pairs = list(student.items()) # list me convert for saving
# print(pairs[0])
# # Below both worked: main catch of using method rather [] is to not get errors
# print(student["name"])
# print(student.get("name"))
#  #hypotecally if we write wrong key then 
# # print(student["name2"]) #error give 
# print(student.get("name2")) # None give
# #  in long programs, if we get errors then whole programs 
# get struck or Error. so we use methods like d.get("") rather directly indexing
# ----------------
 
# student ={
# "name" : "Siddharth kumar",
# "age" : 26,
# "subject": {
#     "maths": 56,
#     "chem" : 58,
#     "phy" : 87
# }
# }
# new_add = {"city" : "bilaspur" ,"name": "Sid" }
# student.update(new_add)
# print(student)
# d.update se new add ho jata h, if we use old key then new name change with old
# ---------------------------------------
#Sets: **uniques values and immutable values stored. that why list & disc not stored in SETS
#sets are mutable but elements are immutable

# collection ={1, 2, 2, 3,3, 4 , "world"}

# print(collection) # unordered h , world middle me print hua
# print(type(collection)) #**duplicate value ignore #not shows error
# print(len(collection)) #length of elements only unique

# set1 = {} #empty dictionary : Syntax
# set2 =set() #empty set : Syntax
# print(set1)
# print(type(set1)) # dict type
# print(set2)
# print(type(set2)) #set type

#Set: unique values | dict: anyvalue
#Set methods

# collection = set()

# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add("python")
# collection.add(2) # only unique value store, duplicate ignored

# collection.add([1]) #list mutable h , so error comes in set

#collection.remove(3) #remove 3 from set
#collection.clear() # clear or remove all set element
# set2 = { "python", "java", "sql", "c++"}

# set2.pop() #random any value comes
 
# collection.union(set2) #combine full set or combo of two sets of unique elements
# collection.intersection(set2)

# # print(set2)
# print(collection)
# ------------------------------------------------------
# set1 = {1 , 2, 3}
# set2 = {3, 4, 5}
# ch = set1.union(set2) # {1, 2,3,4,5}
# ch1 = set1.intersection(set2) #{3}

# print(ch)
# print(ch1)
# ------------------------------------------
#Question/ Practice
# 1
# dict1 ={
#     "table": (" a piece of furniture", "list of facts & figures"), # two value ko tuple() or list[] ke form me save kr sakte h 
#     "cat" : "a small animal"
# }

# print(dict1)
# print(type(dict1))
# ----------------------------------------
#2 one classroom needs for every subject: unique value find vy SETS
# subject= {"pyhton", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# #"c++","C++" are differently treat in sets, so carefully write it
# print(subject)
# print(len(subject)) # 6 clasroom need
#--------------------------------------------------------
#3 dictionary me add ke liye d.update() we use, for sets, s.add()

# mam version 

# marks = {}
# x = int(input("Enter phy:"))
# marks.update({"phy" : x})  # use {} this under update
# x = int(input("enter chem:"))
# marks.update({"chem" : x})
# x =int(input("enter maths:"))
# marks.update({"maths" : x})
# print(marks)

# My way

# marks ={}
# x = int(input("Enter phy:"))
# y = int(input("Enter chem:"))
# z= int(input("Enter math:"))

# marks.update({"phy" : x})
# marks.update({"chem" : y})
# marks.update({"maths" : z})
# print(marks)

# #optimised version
# marks = {
#     "phy": int(input("Enter phy: ")),
#     "chem": int(input("Enter chem: ")),
#     "maths": int(input("Enter maths: "))
# }

# print(marks)
#-----------------------------------------
#4

# # values ={9, 9.0}
# # values ={9, "9.0"} #using as string then save both

# values ={(int, 9), (float, 9.0)} # stores diffently inside tuples(immuatble) not like list(mutable)

# print(values) # only 9 comes , python assume 9 = 9.0














