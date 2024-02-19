
s = "abc"
print(s[0:2])
#string are immutable
s += "def"
print(s)

#valid numeric strings can be converted
print(int("123") + int("456"))
#And numbers can be converted to string
print(str(123) + str(123))

#ord gets the ascii value of a string
print(ord("a"))
print(ord("b"))

#string can also be added like this
string = ["ab", 'cd', "ef"]
print("".join(string))
