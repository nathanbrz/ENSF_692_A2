# input_processing.py

# Nathan De Oliveira, ENSF 692 P24

# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"
        pass

    # Replace these comments with your function commenting
    def update_status(self): # You may decide how to implement the arguments for this function
        while True:
            try:
                user_input = self.input_status_type()
                if (user_input == 0):
                    break
                elif (0 <= user_input <= 3):
                    self.input_status(user_input)
                    print_message(self)
                else:
                    raise ValueError("Invalid input. Must select 1, 2, 3, or 0")
            except ValueError:
                print("Invalid input. Must select 1, 2, 3, or 0\n")
                continue

    def input_status_type(self):
        print("Are changes detected in the vision input?")
        user_in = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "))
        return user_in
    def input_status(self, user_in):
        try:
            user_in2 = input("What change has been identified: ")
            if (user_in2 == "red" or user_in2 == "green" or user_in2 == "yellow" or user_in2 == "yes" or user_in2 == "no"):
                if (user_in == 1):
                    self.light = user_in2
                elif (user_in == 2):
                    self.pedestrian = user_in2
                elif (user_in == 3):
                    self.vehicle = user_in2
            else:
                raise ValueError("Invalid input. Must select red, green, yellow, yes, or no")

        except ValueError:
            print("Invalid vision change. Must select red, green, yellow, yes, or no")

# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    action = "Proceed"
    if (sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes"):
        action = "STOP"
    elif (sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no"):
        action = "Caution"
    
    print(f"\n{action}")
    print(f"\nLight: {sensor.light}, Pedestrian: {sensor.pedestrian}, Vehicle: {sensor.vehicle}.\n")



# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()

    sensor.update_status()


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

