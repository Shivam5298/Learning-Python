# This is a sample code to demonstrate the use of dictionaries in Python
# A dictionary is a collection of key-value pairs, where each key is unique and maps to a value 
# Creating a dictionary
person = {
    "name": "Shivam Ganguly",
    "age": 29,
    "city": "kolkata",
    "email": "sganguly2096@gmail.com",
    "UUID": "123e4567-e89b-12d3-a456-426614174000"

}

# nested dictionary
personDatabase = [
    {
        "UUID": "123e4567-e89b-12d3-a456-426614174000",
        "name": "Shivam Ganguly",
        "age": 29,
        "city": "kolkata",
        "fullAddress": {
            "street": "123 Main St",
            "state": "WB",
            "zip": 700032,
            "country": "India"
        },
        "email": "sganguly2096@gmail.com"
    },
    {
        "UUID": "123e4567-e89b-12d3-a456-426614174001",
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "fullAddress": {
            "street": "456 Oak Ave",
            "state": "NY",
            "zip": 10001,
            "country": "USA"
        },
        "email": "johndoe@example.com"
    }
]

print(person["name"])  # Output: Shivam Ganguly
print(person["age"])   # Output: 29
print("Details of the first person in the database:" )
print(personDatabase[0])  # Output: {'name': 'Shivam Ganguly', 'age': 29, 'city': 'kolkata', 'fullAddress': {'street': '123 Main St', 'state': 'WB', 'zip': 700032, 'country': 'India'}, 'email': 'sganguly2096@gmail.com'} 


# Anoteher way to access the values in a dictionary is to use the get() method, which returns None if the key is not found instead of raising an error
print("Database details of Shivam in the database:" )

for item in personDatabase:
    if item["name"] == "Shivam Ganguly":
        UUID = item["UUID"]

for item in personDatabase:
    if item["UUID"] == UUID:
        details = item

print(details)  # Output: {'UUID': '123e4567-e89b-12d3-a456-426614174000', 'name': 'Shivam Ganguly', 'age': 29, 'city': 'kolkata', 'fullAddress': {'street': '123 Main St', 'state': 'WB', 'zip': 700032, 'country': 'India'}, 'email': '