dict1 = {
    "Queen" : "Bohemian Rhapsody",
    "Bee Gees" : "Stayin' Alive",
    "U2": "One",
    "Michael Jackson": "Billie Jean",
    "The Beatles": "Hey Jude",
    "Bob Dylan": "Like a Rolling Stone",
}

print(len(dict1))

# List keys using the keys() method

print(dict1.keys())

# List keys using a for loop

for item in dict1:
    print(item)

# List all items using the items() method

print(dict1.items())

# List all items using a for loop

for item in dict1.items():
    print(item)

print(dict1.get("Promise of the Real", "The key does not exist in the dictionary."))