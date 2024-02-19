s = ""
str = ["hippo", "hills", "hither", "hall", "heathrow"]

i = 0
j = 0
 #Find the prefix for the list and add it to the string s using for loop
while i < len(str[0]):
    while j < len(str):
        if str[0][i] != str[j][i]:
            break
        j += 1
    else:
        s += str[0][i]
    i += 1
    j = 0
print(s)
"""
for i in range(len(str[0])):
    for j in range(1,len(str)):
        if str[0][i] != str[j][i]:
            break
    else:
        s += str[0][i]
print(s)
"""