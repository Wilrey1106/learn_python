first_name = "Wilmer"
last_name = "Ortega"
full_name = first_name + " " + last_name    # Concatenation of strings
country = "República Dominicana"
city = "Santo Domingo"
age = 19
year = 2025
is_married = False
is_true = True
is_light_on = True
first_name, last_name,country, age = 'Wilmer', 'Ortega', 'República Dominicana'

#MULTIPLES VARIABLES
print(first_name, last_name, country, age)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)

#type of variables
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#LENGTH OF A STRING
print(len(first_name)) #length of first name
print(len(last_name)) #length of last name
print(len(country)) #length of country
print(len(city)) #length of city
print(len(age)) #length of age
print(len(year)) #length of year
print(len(is_married)) #length of is married
print(len(is_true)) #length of is true
print(len(is_light_on)) #length of is light on
print(len(full_name)) #length of full name

num_one = 5
num_two = 4
product_total = num_one + num_two
print(product_total)
product_restado = num_one - num_two
print(product_restado)
product_multiplicado = num_one * num_two
print(product_multiplicado)
product_dividido = num_one / num_two
print(product_dividido)
product_modulo = num_one % num_two
print(product_modulo)
product_exponencial = num_one ** num_two
print(product_exponencial)
product_division_entera = num_one // num_two
print(product_division_entera)

#radio de un circulo
pi = 3.14
radio = 5
area_circulo = pi * (radio ** 2)
print(area_circulo)
print('El area del circulo es:', area_circulo)

#input de datos
first_name,last_name,country,age = input('Ingrerse sus Datos ', first_name, last_name, country, age)
print('Hola', first_name, last_name, 'de', country, 'tienes', age, 'años')
#input de datos con formato
