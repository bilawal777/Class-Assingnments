# Version 3 Default Parameter

def box(a, b=3):
    return a+b

sum = box(2)
print(sum)

def func(a,b):
    a+b

c = func(2,3)

print(c)


#METHOD TODAY CLASS

name:str = "pakistan"
print(type(name))

name1 = name.capitalize()
print(name.count("a"))
print(len(name))
print(name.find("P"))
print(name1)
print(name)

name: str = "My name is Aisha My natonality is Pakistani"
name1 = name.capitalize()
print(name1)
print(name.replace("Pakistani","Malidives").upper())


#LIST METHOD
#append,reverse,sort,insert,remove,pop,extend

#LIST
my_list = ['abdul', 'roshan', "anjali",]

#APPEND

my_list.append("abdul")
print(my_list)

#INSERT

my_list.insert(1,'roshan')
print(my_list)

#REVERSE

my_list.reverse()
print(my_list)

#POP

my_list.pop()
print(my_list)

#REMOVE

#my_list.remove('Anna Gulu gulab khatri')
print(my_list)

#SORT

my_list.sort()
print(my_list)

#EXTEND
 
new_teachers = ['Abdullah', 'Ghous']
print('Old List', my_list)
my_list.extend(new_teachers)

print('Updated List', new_teachers)



#Dictionary

# # get() 
# # keys()
# # values()
# # item()
# # update()
# # clear()
# # pop()

new_dic = {
          'Name': 'AISHA',
          'Gender': 'Female',
          'Age' : 27
}

print(new_dic)

#keys
print(new_dic.keys())

#values
print(new_dic.values())

#items
print(new_dic.items())

#get
print(new_dic.get("Name"))

#update
new_dic1 = {"city" : "Islamabad"}
new_dic2 = {"Country": "Pakistan"}
new_dic.update(new_dic1)
new_dic.update(new_dic2)
print(new_dic1)
print(new_dic2)


#pop in dictionary
print(new_dic.pop("Age"))
print(new_dic)


#clear
new_dic.clear()
print(new_dic)