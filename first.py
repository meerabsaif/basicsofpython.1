#BASICS OF PYTHON   
#DAY 2 | 27TH AUG, 2023.

"""
language assists in communicating with the computer.
so break that language barrier 
python is a multipurpose language.  
python has a nice aroma, addictive scent. Python is very interesting and easy tbvh
PS:thats how you can comment multiple lines using docstring.but what is a comment? dont worry the program wont not read whatever gibberish i wrote. 
THAT IS THE GOOD PART. enough of these tales, come lets dig into basics of python language 
"""
#basic syntax 
print("my first python file")
print("it covers all the basics")
print("computer doesnt reads whats written in the double quotes")
print("we can use python to perform calculations")
print(109+453)
print(34*3)
print(((20/4)*3)-5)
print("the answer will be showed in the output")

print(6) 
print("6")
#line 24 and 25 give the same output, written with and without string. As numbers are universal. whereas "print(hello world)" will give an error.  

#___________________________________________________________________DATA TYPES
"""
here comes the concept of DATA TYPES. some of the most common data types in python are :
1. Integer : 3 ,4 ,567 , 345, 34554. 87463.
2. String (text in inverted commas) : ' ', " ". 
3. Float (known as continous numbers) : 3.4 , 34.5 , 345.6 
4. Boolean : true, false 

"""
#we can also find the data types 
print (type(76))
print (type("hey"))
print (type(3.2))

#___________________________________________________________________VARIABLE (container storing data)
#variables prevent repeatitions. and a good programmer doesnt repeats. got it
#we assign values to our variables using assignment operator (=). 
#rules to assign variable: No space, Only underscore allowed as special symbol, Never start with integer, For two words use camelCase, No key words allowed. 
a=10 
b="ten"
#python detects the data type itself
print(type(a))
print(type(b))
#OR 
print("data type of 10 is:", type(a))
print("data type of ten is:", type(b))

a1= "hey,"
a2= "how are you?"
a3= a1+a2 
print(a3)
#only possible for variables belonging to the same data types

#________________________________________________________________COMMENTS (sticky notes)
#comments are used to explain or add additional information about your code. comments dont affect the execution of your program. they aren't read by program. 
print("we use # to comment a single line")
print("we use Docstring to comment multiple lines ") 

#________________________________________________________________TAKING INPUT FROM USER 
name= input("write your name:")
age = input("enter your age:")
print("your name is:", name)
print("your age is:", age)
      
#________________________________________________________________TYPECASTING (changing datatype of a variable)
s=20
print("before typecasting", type(s))
s=str(s)
print("after typecasting", type(s))

t=98
t=float(t)
print("after typecasting",type(t), "value of t is:", t)

#________________________________________________________________INDEXING (an index is assigned to a string)
#index starts from zero
phrase= "dolce far niente"
print(phrase[0])
print(phrase[1])
print(phrase[2])
#name[starting index : ending index]
print(phrase[6:8])
print(phrase[ :4]) #empty in beginning means from start 
print(phrase[7: ]) #empty at last means till end 
#name[starting index : ending index : steps] 
print(phrase[0: 15: 2])
print(phrase[0: 15: 3])
print(phrase[3: 12: 4])
#to print upside down 
print(phrase)
print(phrase[::-1])
print(name)
print(name[::-1])

#________________________________________________________________CONDITION 
#if else 
age = input("write your age:")
age = int (age)
if (age> 18) :
    print ("you are eligible")
else:
    print ("you are not eligible")

#else if
marks = input("write your marks:")
marks = int (marks)
if (marks >= 40):
    print ("A grade")
elif (marks >= 28) :
    print ("B grade")
elif (marks >= 18) :
    print ("C grade")
else:
    print ("F grade")

#_____________________________________________________________CONCEPT OF FOUR SPACES 
points = input("enter points:")
points = int (points)
if (points==100) :
    print ("great job")
    print ("your grade is A ")      #four spaces indicate that if is applicable 
print("now you are out of if")   

#_____________________________________________________________LOOPS 
#for loop (when we know how many times we need to repeat)
for i in range (7) :
    print ("value of i=" ,i )

#while loop (when we don't know the exact number of times we need to repeat)

z = 1
while z <= 10 :
    print ("value of z is:", z)
    z = z + 1

#______________________________________________________________FUNCTIONS (performing a specific task)
#1.Built in function: for example= print and input
#2.User defined (these are functions we create for performing a specific task)
#this is how we create a function:
#DEFINING FUNCTION
def addition() :
    a=12
    b=23
    c=a+b
    print(c)
#FUNCTION CALLING
addition()

def subtraction() :
    w=2
    e=8
    r=w-e
    print(r)
subtraction()

#another way to create a function
def multiplication():
    x=4
    y=5
    return x*y
multiply= multiplication()
multiply= multiply * 2
print(multiply)

    

    