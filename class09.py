
#LOCAL & GLOBAL VARABILES
#local variables jo function andar define kia jata h surf is function ma acessable hota h jo wo local varaiables hota h
#global varabiles jo function bhay define krta h program k jagha acess hota h global varabiles


def my_function():
   x=30 #
   print("inside function:" , x)
my_function()
#print("outside function:", x) #error generate

#global varabiles
Y=50
def designers():
   print("inside function:" , Y)
designers()
print("outside function:" , Y)

#DOC STRING 
def add(num1:int,num2:int)->int:
   return num1 +num2
result=add(5,7)
print(add.__doc__)
print(result)

#SET METHOD;
#ADD
#REMOVE
#DISCAED
#POP
#UNION
#INTERSECTION

#ADD
names_set = {"Asad","A.Jabbar","Yoha","Aisha"}
names_set.add("Eman")
print(names_set)

#REMOVE
names_set ={"Asad","yoha","aisha","eman","A.jabbar"}
names_set.remove("Asad")
print(names_set)

#DISCARD
names_set ={"Asad","yoha","aisha","eman","A.jabbar"}
names_set.discard( "Asad")
print("discard:",names_set) 

#POP
names_set ={"Asad","yoha","aisha","eman","A.jabbar"}
names_set.pop()
print(names_set) 

#POP WITH UNION
num_set1 ={1,2,3,4,5}
num_set2 ={6,7,8,9,10}
result=num_set1.union(num_set2)
print("result",result) 

#INTERSECTION

num_set1 ={1,2,3,4,5}
num_set2 ={6,7,8,9,10}
result=num_set2.intersection(num_set1)
print("result",result)
