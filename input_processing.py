# input_processing.py

# Nathan De Oliveira, ENSF 692 P24

# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:

    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"
        pass

    def update_status(self):
        """
        This method continuously prompts the user to input changes detected in the vision input 
        (light status, pedestrian presence, or vehicle presence) and updates the sensor's status 
        accordingly. It prints the action message and current status after each update.        
        """
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
        """
        Prompts the user to select the type of vision input change from the menu.
        Returns:
            int: The user's input representing the type of change detected.
        """

        print("Are changes detected in the vision input?")
        user_in = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "))
        return user_in
    
    def input_status(self, user_in):
        """
        Updates the status of the sensor based on the user's input change.
        Args:
            user_in (int): The type of vision input change as selected by the user.
        """

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
            print("Invalid vision change.")

def print_message(sensor):
    """
    Prints the action message and current status based on the sensor's status.
    Args:
        sensor (Sensor): The Sensor object whose status needs to be printed.
    """

    action = "Proceed"
    if (sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes"):
        action = "STOP"
    elif (sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no"):
        action = "Caution"
    
    print(f"\n{action}")
    print(f"\nLight: {sensor.light}, Pedestrian: {sensor.pedestrian}, Vehicle: {sensor.vehicle}.\n")



def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    sensor = Sensor()
    sensor.update_status()


if __name__ == '__main__':
    main()

