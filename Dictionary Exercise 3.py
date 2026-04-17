# This is a sample program for dictionaries in python

keys = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

value = "consonant"

dict1 = dict.fromkeys(keys, value)

for key, value in dict1.items():
    print(key , value)

fast_food_items = {
    "McDonald's": "Big Mac", 
    "Burger King": "Whopper", 
    "Chick-fil-A": "Original Chicken Sandwich"
    }

print(fast_food_items.pop("McDonald's"))
removedItem = fast_food_items.popitem()

print(fast_food_items)
print(removedItem)