# This is a sample code to demonstrate the use of dictionaries in Python
# A dictionary is a collection of key-value pairs, where each key is unique and maps to a value 
# Creating a dictionary
person = {
    "name": "Shivam Ganguly",
    "age": 29,
    "city": "kolkata",
    "email": "sganguly2096@gmail.com"

}

# nested dictionary
personDatabase = [
    {
        "name": "Shivam Ganguly",
        "age": 29,
        "city": "kolkata",
        "fullAddress": {
            "street": "123 Main St",
            "state": "WB",
            "zip": "700001",
            "country": "India"
        },
        "email": "sganguly2096@gmail.com"
    },
    {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "fullAddress": {
            "street": "456 Oak Ave",
            "state": "NY",
            "zip": "10001",
            "country": "USA"
        },
        "email": "johndoe@example.com"
    }
]