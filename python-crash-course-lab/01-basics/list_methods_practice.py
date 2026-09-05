cars = [' Lexus ', ' Mersedes ', ' KIA ']  # List of 3 cars
cars[1] = ' Audi '  # Change 'Mersedes' to 'Audi' in the list
cars.append(' BMW ')  # Add a new element to the end using append method
cars.insert(0, ' Mazda ')  # Insert a new element at index 0 using insert method
del cars[0]  # Delete the element at index 0 using del statement
car = f"{cars[1]}".strip()  # Create an f-string with the element at index 1 and strip whitespace
text_car = "cool car!"  # Variable text_car containing text string
print(f"{car} {text_car}".title())  # Print the title-cased f-string to the terminal