
#CLASS 12 TOPIC 
#RECURSIVE FUNCTION/ RECURSION

#example 
#def count_down():
 #count_down()
 #count_down()

def count_down(num:int)->int:
 print("num>>>",num)

 count_down(10)

def count_down(num:int)->int:
 print("num>>>",num) # 10  -> 9
 count_down(num - 1) # 9-1->8
count_down(10)

def count_down(num:int)->int:
 
 if num <=0: 
  print("count_down done")
 else:
  print("num>>>" , num)
 count_down(num - 1) # 9-1->8

 count_down(10)

def count_down(num:int)->int:
 if num == 0: 
  print("count_down done")
 else:
  print("num>>>",num)
  count_down(num =- 1) # 9-1->8

count_down(10)

#LAMBANDA FUN

def add(a:int,b:int) ->int:
    return a+b 
add (6,8)

#def add(a:int,b:int) ->int:
 #   return a+b 

#lambda argument:expression /statment
add = lambda a,b:a+b

result = add(6,8)
print(result)

sub = lambda a,b:a-b

result = sub(6,8)
print(result)

#operating System module

import os

print("cwd",os.getcwd()) #cwd -> current workeingdirectory
print("lis dir",os.listdir())
#print("new folder",os.mkdir("test"))
#print("rename",os.rename("test","test new"))
#os.rmdir("test new")

 #FILE OPERATIONS/fileIO

file =open("text.txt","r")
print("file>>>",file)
print(file.read())

file =open("text2.txt","w")
file.write("YA AISHA K STYLE HA RAY")
file.close()

file =open("text2.txt","a")
file.write("\nTU NIKAL")
file.close()

with open("text2.txt","a") as file:
 file.write("\nTU JAA RAY BABA")
