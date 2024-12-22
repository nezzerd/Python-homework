word = input()
dict = {chr(i): i for i in range(ord('a'), ord('z') + 1)}
dict.update({chr(i): i for i in range(ord('A'), ord('Z') + 1)})
alphabet_order_dict = {letter: index + 1 for index, letter in enumerate(dict.keys())}
unique_letters = set(word.lower())
sum_of_numbers = sum(alphabet_order_dict[letter] for letter in unique_letters if letter in alphabet_order_dict)
print(sum_of_numbers)