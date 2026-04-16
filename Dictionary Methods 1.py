# This is a dictionary exercise demonstating the use of dictionary methods.

person = {
    "name": "Shivam",
    "age": 25,
    "city": "Kolkata",
    "profession": "Software Engineer",
    "email": "sganguly2096@gmail.com"
}

# 1. Keys method allows us to get a list of all the keys in the dictionary.
print("Keys:", person.keys())

for item in person.keys():
    print(item)

# 2. Values method allows us to get a list of all the values in the dictionary.
print("Values:", person.values())

for item in person.values():
    print(item)

# 3. Items method allows us to get a list of all the key-value pairs in the dictionary.
print("Items:", person.items())
for item in person.items():
    print(item)

for key, value in person.items():
    print("Key: ",key, ", Value: ",value)

# 4. In can be used to check if a key exists in the dictionary.
print("name" in person)  # True
print("address" in person)  # False

if "name" in person:
    print("Name exists in the dictionary.")
else:
    print("Name does not exist in the dictionary.")



# 5. Not In can be used to check if a key does not exist in the dictionary.
print("name" not in person)  # False
print("address" not in person)  # True

# 6. Get method allows us to get the value of a key. If the key does not exist, it returns None or a default value if provided.
print("Name:", person.get("name"))  # Shivam
print("Address:", person.get("address"))  # None
print("Address:", person.get("address", "Not Found"))  # Not Found

# 7. Update method allows us to update the value of a key or add a new key-value pair to the dictionary.
person.update({"age": 26})  # Update existing key
print("Updated Age:", person["age"])  # 26

# Adding new key-value pair
person.update({"phone": "123-456-7890"})
print("Phone:", person["phone"])  # 123-456-7890

# 8. Pop method allows us to remove a key-value pair from the dictionary and return the value of the removed key.
removed_value = person.pop("email")
print("Removed Email:", removed_value)
print("Updated Dictionary:", person)

# 9. Clear method allows us to remove all key-value pairs from the dictionary.
person.clear()
print("Cleared Dictionary:", person)  # {}

# 10. Copy method allows us to create a shallow copy of the dictionary.
person_copy = person.copy()
print("Original Dictionary:", person)
print("Copied Dictionary:", person_copy)

# 11. Fromkeys method allows us to create a new dictionary with specified keys and a common value.
keys = ["name", "age", "city"]
value = "Not Specified"
new_dict = dict.fromkeys(keys, value)
print("New Dictionary:", new_dict)      

# 12. Setdefault method allows us to get the value of a key if it exists, or set it to a default value if it does not exist.
print("Name:", person.setdefault("name", "Unknown"))  # Unknown 
print("Updated Dictionary:", person)  # {'name': 'Unknown'}

# 13. Popitem method allows us to remove and return an arbitrary key-value pair from the dictionary.
removed_item = person.popitem()
print("Removed Item:", removed_item)  # ('name', 'Unknown')
print("Updated Dictionary:", person)  # {}

# 14. Length method allows us to get the number of key-value pairs in the dictionary.
print("Length of Dictionary:", len(person))  # 0

# 15. Update method allows us to update the dictionary with key-value pairs from another dictionary.
person.update({"name": "Shivam", "age": 25, "city": "Kolkata", "profession": "Software Engineer", "email": "sganguly2096@gmail.com", "phone": "123-456-7890"})    
print("Updated Dictionary:", person)

# 16. Del statement allows us to remove a key-value pair from the dictionary.
del person["phone"]
print("Updated Dictionary after deletion:", person)

