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

