
#ERROR HANDLING

#Try except

num1: int  =10
num2: int  =0

result =num1 / num2
print(result)

#EXPCEPT EXPITION AS ERROR (e)
try:
   result=num1/ num2
   print(result)
except Exception as e:
   print(e)

# zero division error  (zero sa divide krna k khosish)
#key error  (dictornay ma invalid key acess krna)
#index error (list ya tuple k bhar index acess krna)
#value error    (invalid data type input)
#import error

# ZERO DIVISION
try:
   num1 =10
   num2 = 0

   result = num1 / num2
   print(result)
except ZeroDivisionError:
   print("this is error for zero value")
except IndexError:
   print("this is error with index")

#LIST K ANDR ERROR
list =["asad","aisha"]
try:
   result = list[2]
   print(result)
except ZeroDivisionError:
   print("this is error for zero value")
except IndexError:
   print("this is error with Index error")
