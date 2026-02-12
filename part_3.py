#Task 3.1:
try:
    speed_input = input("Enter Motor Speed: ")
    speed = int(speed_input)
    print("Speed set to:", speed)
except ValueError:
    print("Error: Corrupted Signal. Maintaining current speed.")
#Coding version of try this and if it doesnt work (valuerror) then dont and do this

#Task 3.2:
def get_coordinate():
    while True:
        try:
            user_input = input("Enter X-coordinate: ")
            coordinate = int(user_input)
            return coordinate  #Valid input, exit loop
        except ValueError:
            print("Invalid coordinate")

x = get_coordinate()
print("Coordinate received:", x)

#Task 3.3: 
def get_coordinate():
    while True:
        try:
            user_input = input("Enter X-coordinate: ")
            coordinate = int(user_input)

            if coordinate > 100 or coordinate < -100:
                print("Coordinate out of range")
            else:
                return coordinate

        except ValueError:
            print("Invalid coordinate")

x = get_coordinate()
print("Safe coordinate received:", x)

