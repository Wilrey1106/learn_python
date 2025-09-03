# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2
# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)
# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

#Exercises declare this variables
age = 19
height = 1.80
complex_number  = 2 + 3j

#script
Enter_base = 20
Enter_height = 10
area_of_triangle = 0.5 * Enter_base * Enter_height
print('Area of triangle:', area_of_triangle)

#script
a = 5
b = 4 
c = 3
perimetro_triangulo = a + b + c
print ('Perimetro del triangulo es', perimetro_triangulo)

#script
#get length and width of rectangle
height = 10
area_of_triangle = 100
length = area_of_triangle / height
print('length of rectangle:', length)
#script
length = 10
height = 10
perimeter = 2 * (length + height)
print('Perimeter of rectangle:', perimeter)

#scrip radio de un circulo
pi = 3.14
radius = 5
area_of_circle = pi * (radius ** 2)
print('Area of circle:', area_of_circle)

circunference = 2 * pi * radius
print('Circunference of circle:', circunference)

#script
m = 2
b= -2
intersecion_y = b
intersecion_x = -b / m
print("pendiente: (m)", m)
print('intersecion_y:', intersecion_y)
print('intersecion_x:', intersecion_x)

#script
y2 = 10
y1 = 2
x2 = 6
x1 = 2
eculidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('Eculidean distance:', eculidean_distance)

#script
sentece = 'I Hope this course is not full of jargon'
print('jargon' in  sentece)
print('on' in 'jargon' and 'on' in 'python')
text = "python" 
length = len(text) #search quanty of letters in the string
length_float = float(length) #convert the length to float
string = str(length_float) #and now converto the float to string
print('Length of the string:', length_float) # now, use print to show a result
#script
a = 2
b = 0
division = a/b #create to variables to divide
#Ain't would division by zero

#script
a=7
b=3
floor_division = a // b #floor division
print('Floor division:', floor_division) #floor division
print(7//3 == int(2.7)) #floor division

print('10' == 10) #False, because 10 is a string and 10 is an integer
print(10 == int('9.8'))

#script
Enter_hours = 40
Enter_rate_per_hour = 28
weekly_earning = Enter_hours * Enter_rate_per_hour
print('Your weekly earning:', weekly_earning)

#script
enter_number_of_years_you_have_lived = 100
enter_number_of_days_you_have_lived = 100 * 365
enter_number_of_minutes_you_have_lived = enter_number_of_days_you_have_lived * 24 * 60
enter_number_of_seconds_you_have_lived = enter_number_of_days_you_have_lived * 24 * 60 * 60
print('You have lived:', enter_number_of_seconds_you_have_lived, 'seconds')

#SCRIPT
a = "1 1 1 1 1" 
b = "2 1 2 4 8"
c = "3 1 3 9 27"
d = "4 1 4 16 64"
e = "5 1 5 25 125"
print(a)
print(b)  
print(c)
print(d)
print(e)