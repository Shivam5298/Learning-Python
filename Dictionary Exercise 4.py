# This is a sample exercise for dictionary in python

internet_celebrities = {
    "DrDisrespect": "YouTube", 
    "ZLaner": "Facebook", 
    "Ninja": "Mixer"
    }

another_one = {
    "shroud": "Twitch"
    }

internet_celebrities.update(another_one)

copy_dict = internet_celebrities.copy()

internet_celebrities.clear()

print(internet_celebrities)

print(copy_dict)