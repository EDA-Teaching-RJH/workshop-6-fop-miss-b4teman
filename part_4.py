#Start:

#Initialize:
travel_log = []

#Loop:
while True:
    
    #Input/Validation:
    try:
        angle_input = input("Sensor Reading (Slope Angle): ")
        angle = float(angle_input) 
        
    except ValueError:
        print("Sensor Glitch")
        continue 

    #Safetey Check:
    if angle > 45:
        print("CRITICAL TILT! HALTING!")
        break

    #Logging:
    travel_log.append(angle)

    #Output:
    print("Path Stable. Moving forward")

print("Mission Terminated")
print("Total steps taken:", len(travel_log))
print("Travel Log:", travel_log)


