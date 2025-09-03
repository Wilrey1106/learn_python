print("==================")
print("Area Calculator 📐")
print("==================")
print()
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

shape = input("Which shape: ")

if shape == "1":
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = 0.5 * base * height

    print(f"The area is {area}")
elif shape == "2":
    width = float(input("Width: "))
    height = float(input("Height: "))
    area = width * height

    print(f"The area is {area}")
elif shape == "3":
    side = float(input("Side: "))
    area = side * side

    print(f"The area is {area}")
elif shape == "4":
    radius = float(input("Radius: "))
    area = 3.14159 * radius * radius

    print(f"The area is {area}")
elif shape == "5":
    print("Goodbye!")
else:
    print("Invalid option")