string = "North Dakota"

print(string.rjust(17))

print(string.ljust(17), "**")

centerPlus = string.center(16, "+")
print(centerPlus)

print(string.lstrip("North"))

print(centerPlus.rstrip("+"))

print(centerPlus.strip("+"))

print(string.replace("North","South"))


