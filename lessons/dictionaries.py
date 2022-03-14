"""Dictionary capablities"""

# Declaring the type of a dictionary
schools: dict[str, int]

# Intialize to an empty dictionary
schools = dict()

# Set a key value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "Lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key value pair for dictionary
schools.pop("Duke")

# Test for exsistence of key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")


# Update a key value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Reassigning school to be empyty dictionary literal
schools = {} # same as dict()
print(schools)

# Alternatively, intialize key value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"school: {school} -> Value: {schools[school]}")