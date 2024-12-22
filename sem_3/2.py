dict = {chr(i): i for i in range(ord('a'), ord('z') + 1)}
dict.update({chr(i): i for i in range(ord('A'), ord('Z') + 1)})
alphabet_order_dict = {letter: index + 1 for index, letter in enumerate(dict.keys())}
print(alphabet_order_dict)
