# Day 1 - 30DaysOfPython Challenge
print ("Python --Version 3.10.4")
print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

print ('Wilmer')
print ('Wilmer' + ' ' + 'Ortega')
print ('Santo domingo')
print ('República Dominicana')
print ('''Wilmer Ortega,Santo Domingo,República Dominicana''')
print ("""i AM ENJOYING 30 DAYS OF PYTHON CHALLENGE""")
print (type(10))
print (type(9.8))
print (type(3.14))
print (type(4-4j))
print (type(['Asabeneh', 'Python', 'Finland']))
print (type('Wilmer'))
print (type('Wilmer Ortega'))
print (type('Santo Domingo'))

import math

# Define the points
point1 = (2, 3)
point2 = (10, 8)

# Calculate differences and distance
distance = math.hypot(point2[0] - point1[0], point2[1] - point1[1])

print("Euclidean distance:", distance)