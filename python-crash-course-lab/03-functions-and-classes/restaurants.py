class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def increment_number_served(self, peoples_plus):
        self.number_served += peoples_plus

    def describe_restaurant(self):
        print(f'\nRestaurant Name: "{self.restaurant_name}".')
        print(f'Cuisine Type: {self.cuisine_type}.')
        print(f"Number of customers served: {self.number_served}.")
    
    def open_restaurant(self):
        print("The restaurant is now open!")

    def set_number_served(self, peoples):
        if peoples >= self.number_served:
            self.number_served = peoples
        else:
            print("\nError: The new value cannot be less than the current number of served customers.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def IceCreamSorted(self):
        print(f"Available ice cream flavors: {', '.join(self.flavors)}.")


# Creating objects with standard English names
icecream = IceCreamStand("Sweet Island", "Desserts")
restaurant1 = Restaurant("The Cozy Courtyard", "European Cuisine")
restaurant2 = Restaurant("Panorama", "Italian Cuisine")
restaurant3 = Restaurant("The Olive Branch", "Mediterranean Cuisine")

# Testing the methods
icecream.describe_restaurant()
icecream.IceCreamSorted()

restaurant1.number_served = 25
restaurant1.describe_restaurant()

restaurant2.set_number_served(75)
restaurant2.set_number_served(70)  # This will trigger the error message
restaurant2.describe_restaurant()

restaurant3.set_number_served(25)
restaurant3.increment_number_served(25)
restaurant3.describe_restaurant()