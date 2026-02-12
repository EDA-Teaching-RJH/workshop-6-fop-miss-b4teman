#Task 1.1
#Create list
sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

#Print first item (index 0)
print("First sample:", sample_bay[0])

#Print ast item (negative indexing)
print("Last sample:", sample_bay[-1])

#Print total no. samples
print("Total samples:", len(sample_bay))


#Task 1.2: Iteration
for sample in sample_bay:
    print("Transmitting data for:", sample)

#Task 1.3: Appending
new_findings = []

for _ in range(3):
    rock = input("Enter a rock type: ")
    new_findings.append(rock)

print("New findings:", new_findings)

#Task 1.4: Extension
if "Dust" in sample_bay:
    sample_bay.remove("Dust")

print("Cleaned sample bay:", sample_bay)

