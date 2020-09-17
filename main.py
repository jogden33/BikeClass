# Jenny Ogden
# Purpose: Create a Class called Bike
#
# Properties
#  gears (number of gears): getGears(), setGears()
#  current (current number of gears): getCurrent(), setCurrent()
#  wheels (number of wheels): getWheels(), setWheels()
#  braketype (brake type): getBrakeType(), setBrakeType()
#
# Methods
#  ResetGears()
#  IncreaseGears()
#  DecreaseGears()

class Bike:

    # Instantiate a copy of the class and set all of the properties
    def __init__(self, gears, current, wheels, braketype):
        self.setGears(gears)
        self.setCurrent(current)
        self.setWheels(wheels)
        self.setBrakeType(braketype)

    ######################################################
    # Getter and setter for the gears property
    def getGears(self) -> int:
        return self.gears

    def setGears(self, gears: int) -> None:
        try:
            gears = float(gears)
        except Exception as e:
            raise e
        try:
            if gears in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15):
                gears = int(gears)
                self.gears = gears
            else:
                print(f"ERROR: Gears must be an integer between 1 and 15\n")
        except Exception as e:
            raise e

    ######################################################
    # Getter and setter for the current property
    def getCurrent(self) -> int:
        return self.current

    def setCurrent(self, current: int) -> None:
        try:
            current = float(current)
        except Exception as e:
            raise e
        try:
            if current <= self.gears and current in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15):
                current = int(current)
                self.current = current
            elif current > self.gears:
                print("ERROR: Current gears must be less than or equal to the total number of gears\n")
            else:
                print(f"ERROR: Gears must be an integer between 1 and 15\n")
        except Exception as e:
            raise e

    ######################################################
    # Getter and setter for the wheels property
    def getWheels(self) -> int:
        return self.wheels

    def setWheels(self, wheels: int) -> None:
        try:
            wheels = float(wheels)
        except Exception as e:
            raise e
        try:
            if wheels in (1, 2, 3, 4):
                wheels = int(wheels)
                self.wheels = wheels
            else:
                print(f"ERROR: The number of wheels must be an integer between 1 and 4\n")
        except Exception as e:
            raise e

    ######################################################
    # Getter and setter for the braketype property
    def getBrakeType(self) -> str:
        return self.braketype

    def setBrakeType(self, braketype: str) -> None:
        try:
            if braketype in ("hand brakes", "foot brakes"):
                self.braketype = braketype
            else:
                print(f"ERROR: Brake Type must be 'hand brakes' or 'foot brakes'")
        except Exception as e:
            raise e

    ######################################################
    # Reset the current gears to 1
    def ResetGears(self) -> None:
        try:
            self.current = 1
        except Exception as e:
            raise e

    ######################################################
    # Increase the current gears by an increment of 1
    def IncreaseGears(self) -> int:
        while self.current < self.gears:
            self.current += 1
            return self.current
        else:
            print(f"ERROR: Gear increase cannot exceed the number of gears")

    ######################################################
    # Decrease the current gears by an increment of 1
    def DecreaseGears(self) -> int:
        try:
            if self.current > 1:
                self.current = self.current - 1
                return self.current
            else:
                print(f"ERROR: Gears cannot go below 1")
        except Exception as e:
            raise e

#################### END OF CLASS ####################


# Instantiate a new bike object
JennyBike = Bike(14, 1, 4, 'foot brakes')
print(f"Number of Gears: {JennyBike.getGears()}")
print(f"Current Gear: {JennyBike.getCurrent()}")
print(f"Number of Wheels: {JennyBike.getWheels()}")
print(f"Bike Type: {JennyBike.getBrakeType()}")

# Set gear to 10
JennyBike.setCurrent(10)
print()
print(f"Current gear: {JennyBike.getCurrent()}")

# Increase the gear
JennyBike.IncreaseGears()
print(f"Increased Gear: {JennyBike.getCurrent()}")

# Try to bypass the maximum gear of 15
print()
JennyBike.setGears(20)

# Try to bypass the minimum gear of 1
print()
JennyBike.setGears(0)

# Try to set bike type to 'electric'
print()
JennyBike.setBrakeType('electric')


















