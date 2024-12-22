s = input()
frequency = {}
filtered = ''.join(char for char in s if not char.isdigit() and not char.isspace())
chars = len(filtered)
for char in filtered:
    frequency[char] = frequency.get(char, 0) + 1
for char in frequency:
    frequency[char] /= chars
print(frequency)
