print("Hello World")
# variable and data types 
# int, float, string, boolean

x = 10 #int
y = 3.14 #float
name = "Alice" #string
is_student = True #boolean

x = 56
y = 4.5

print(x + y)

#ways of writing variables #camelCase
FirstName = "John" #snakecase
LastName = "Doe" #camelcase
FullName = FirstName + " " + LastName #concatentation
print("FullName:", FullName)

#arithemic oprtations# addition, subtraction, multiplication, division
a = 10 
b = 5

#addition 
z = a + b
print("Addition Result", z)

#subraction 
c = a - b
print("Subtraction Result", c)

#multiplication
d = a * b
print("Multiplication Result", d)

#division
c = a / b
print("Division Result", c)

# Functions in Python
def greet():
    print("Hello, welcome to Python programming")
greet() # calling the function 

# Function with parameters
def add_numbers(num1, num2):
  return num1 + num2 #returns the sum of two numbers
result = add_numbers(5, 10) #calling the function with arguments
print("Sum of 5 and 10 is:", result) #printing the result of 

myList = ["apple", "banana", "chery"] #list of fruits
i = 0 #initalizing index
while i < len(myList): #while loop to iterate through the list
   print("Fruit at index", i, "is", myList[i]) #printing each fruit with it's index
   i += 1 #incrementing the index
   print("My List", myList) #printing the list

print("First fruit in the list:", myList[0]) #accessing the first element of the list
len_of_list = len(myList) #getting the lenght of the list
print("Lenght of the list:", len_of_list) #printing the lenght
# looping through the list
for fruit in myList:
   print("Fruit:", fruit) #printing each fruit in the list

   #if condition
   age = 20 #age variable 
   if age >= 18: #checking if age is greater than or equal to 18
      print ("You are an adult.") #printing if the condition is true
   else:
      print("You are minor.")   

      #switch case
      def switch_case_example(value):
         match value: #using match-case for switch-like behaviour
            case 1:
               return "You selected option 1."
            case 2:
               return "You selected option 2."
            case 3:
               return "You selected option 3."
            case _:
               return "Invalid option selected."

# calling the switch case function
print(switch_case_example(2)) #should print "You selected option 2"

#Arrays in Python
my_array = [1, 2, 3, 4, 5] #creating an array
print("My Array:", my_array) #printing the array
print("First element of the array:", my_array[0]) #accessing the first 
#looping through the array
for num in my_array:
   print("Number:", num) #printing each number in the array

   mydb = mysql.connector.connect 

   