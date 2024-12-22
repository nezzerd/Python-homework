dict = {chr(i): i for i in range(ord('a'), ord('z') + 1)}
print(dict)
dict.update({chr(i): i for i in range(ord('A'), ord('Z') + 1)})
print(dict)
