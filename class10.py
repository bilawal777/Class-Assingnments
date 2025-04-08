
#TOPIC
# Short Hand Else/Ternary Opperators  

num: int =17

if num >17:
    print("number is greaters then 17")
else:
    print("number is less then <17")

#second 
#if condition:
   # statment:

# if statement if condition else statement
#else:
num:int = 9
print("num is greater then 10") if num>10 else print("number is lees then 10")
#3
num =5 
#num2 =agr condition ture value 20 warna 10
num2 =20 if num < 10 else 7 
print("num>>>",num2)

#ENUMANTED FUNCTION

#EXAMPLE
#          0         1      2      3
names = ["aisha","jabbar","eman","yoha"]
for name in names:
   print(name)

#2
#          0         1      2      3
names = ["aisha","jabbar","eman","yoha"]
print(names[2])

#3
for name in names:
    if names[1] == "jabbar":
        print("ADAB Jabbar")
        print(name)

#4
#           0         1      2      3
names = ["aisha","jabbar","eman","yoha"]
# print(names[1])
index =0
for name in names:
    print("index",index)
    print(name)
    index =index +1

#5
#           0         1      2      3
names = ["aisha","jabbar","eman","yoha"]
index =0
for name in names: 
    print(f"name{index}: {name}")

#6
#          0         1      2      3
names = ["aisha","jabbar","eman","yoha"]
for index,name in enumerate(names):
  print(f"name{index}: {name}")

# Map,Filter,Reduce Function

#LOOP
numbers =[1,2,3,4,5]
def square(num:int) :
    return num * num
new_list =[]
print
for num in numbers:
    print("num>>>",num)
    print("calling square function")
    num_sqr =square(num)
    print("num_sqr>>>",num_sqr)
    print("new_list>>>",new_list)

#Map
numbers =[1,2,3,4,5]
def square(num:int) :
    return num * num

new_list = list(map(square,numbers))
print("numbers",numbers)
print("new_list>>>",new_list)

#Filters
numbers =[1,2,3,4,5]
def filter_function(num:int):
    return num >3

filtered_list =list(filter(filter_function,numbers))
print("filtered_list",filtered_list)

#MAP
numbers =[1,2,3,4,5]
def filter_function(num:int):
    return num >3

filtered_list =list(map(filter_function,numbers))
print("filtered_list",filtered_list)
