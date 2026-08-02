# 1. Defining a Class (The Blueprint)
class Car:
    
    # 2. The Constructor (__init__ method)
    # This runs automatically whenever we create a new Car object
    def __init__(self, brand, model, color):
        # 3. Attributes (Characteristics of the car)
        self.brand = brand
        self.model = model
        self.color = color
        self.is_engine_on = False  # Default state

    # 4. Methods (Actions the car can perform)
    def start_engine(self):
        if not self.is_engine_on:
            self.is_engine_on = True
            print(f"Vroom! The {self.color} {self.brand} {self.model}'s engine is now ON.")
        else:
            print(f"The {self.brand} {self.model}'s engine is already running.")

    def stop_engine(self):
        if self.is_engine_on:
            self.is_engine_on = False
            print(f"The {self.brand} {self.model}'s engine is now OFF.")
        else:
            print("The engine is already off.")

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model} | Color: {self.color}")


print("--- Creating Objects ---")
# Creating objects (Instances of the Car class)
car1 = Car("Toyota", "Corolla", "Blue")
car2 = Car("Ford", "Mustang", "Red")

print("\n--- Accessing Attributes and Methods ---")
# Viewing their information using the method we built
car1.display_info()
car2.display_info()

print("\n--- Interacting with Car 1 ---")
car1.start_engine()
car1.start_engine() # Trying to start it again
car1.stop_engine()

print("\n--- Interacting with Car 2 ---")
car2.start_engine()