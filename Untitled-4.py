last_name = "Adebimpe"
print("my name is Zainab" +" " + last_name)
# Variable - a container for a value # the print function can only be used together with the same data type.# strings are always used in quotes.
# You can combine variables together as long as they are of the same type
# strings /letters are usually in "", floats are decimals, int-integers, boolean - True/False
#If you cannot combine to different data types, you should use print (" " + str(age)) or print (15 + int(babies))
#Multiple assignment - allows us to use multiple variables at the same time like; name ,age, attractive="zab",21,True or Joy=Zab=Amina=30
#string slicing - can be used to create a substituting extracting elements from another string with the use of indexing[] or slice() or [start:stop:step]
#type casting - converting the data type of a variable to another data type
# csv_df = pd.read_csv('Download/2006.csv')  
#while used for an infinnite argument
#loop/for - used for a finite argument
#Nested-loop : having a loop indside a loop
#loop control statements - change a loop exectution from it's normal sequence
#list - used to store multiple items in a single variable,items in a list are called 'elements'(str ot int) and they are enclosed in [] and ordered
#tuples - immutable, store related items in normal brackets
#set - unordered collection,unindexed,doesn't duplicate in curly braces
#dictionary - changable,unordered collection of unique keyvalue pairs in {}
#dictionary attributes - .keys,.values,.update,.remove,.items
#index operator []- gives access to a sequence element
#function - a block of code which is executed when it's called, we "define" a function(def)
#
#
#
#
first_name = last_name[0:3] #reverse [ : : -1]
age = 21
age += 1
print("My age is " + str(age))
print(type(last_name))
print(len(last_name))
print(len(str(age))) #len used with string alone
print(last_name.find("b")) #position of the letter and indexing in python starts from 0, this can be used with {capitalize,upper,lower,isdigit,isalpha,count,replace(" ","")}
print(first_name)
#age  = input("How  old are you ? ")
import math
pi = 3.1456
#va= {"x":1 , "y": 2 ,"z":3}
x,y,z = 1,2,3
print(round(pi))
print(math.ceil(pi))
print(max(x,y,z))
temp = float(input("What is the temperature today: "))
print(f'{temp} C')
if temp >= 0 and temp < 25:
    print("The temperarture is good today!")
    print("Go outside!!!")
elif temp < 0 or temp >25:
    print("Stay inside!!!")
else :
    print("It's your choice")
name = input("What is your name? :" )
#while True :
 #   if name == " ":
  #      break
   # if name == "ade":
  #      continue
#while i +1:
 #   i == 1
 #   print(i), pass - does nothing
import time 
for i in range(10, 0 ,-1):
    print(i)
    time.sleep(1)
print("Happy Birthday!!!")
rows = int(input("How many rows:"))
columns = int(input("How many columns:"))
symbol = input("Which symbol are you using:")
for i in range(rows):
    for j in range(columns):
        print(symbol,sep= " ",end= " ")#sep and end has to be none or str
    print()
food = ["pizza","yam","tea",5]
print(food[3])
for i in food:
    print(i, sep=" ",end=" ")
food.insert(1,"tomato")#add an item to a list in a specific position & append-add an element to a list
print(food)
drink = ["fanta","coke","tomato"]
dessert = ["cake","chocolate"]
menu = [food,drink,dessert]#2D list- list of lists
print(menu[0][ :1])
student = ("Zainab", 22, "dev")#tuples,attributes(.count,.index). set attributes(.update,.union,.difference,.intersection)
def hello(last_name):
    print("hello"+" " + last_name)
hello(first_name)
