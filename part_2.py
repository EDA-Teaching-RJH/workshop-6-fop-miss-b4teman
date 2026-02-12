#Task 2.1:
#Create dictionary
rover_status = {
    "Battery": 100,
    "Heater": "Off",
    "Camera": "Standby"
}
#Key:value

# Print the Battery status
print("Battery status:", rover_status["Battery"])


#Task 2.2: Status Update
#Update values
rover_status["Battery"] = 85
rover_status["Heater"] = "On"

#Add new key-value pair
rover_status["Speed"] = 5

#Print full dictionary
print("Updated rover status:", rover_status)


#Task 2.3: Nesting
#Create list with two dictionaries inside
mission_log = [
    {"Site": "Crater A", "Radiation": "Low", "Water": False},
    {"Site": "Dune B", "Radiation": "High", "Water": True}
]

#Loop through mission_log
for site in mission_log:
    print("Site", site["Site"], "has", site["Radiation"], "radiation.")
