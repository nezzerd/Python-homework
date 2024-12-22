import re

phone_numbers = input().split()
pattern = r'^[89]\d{9}$'
valid_numbers = [number for number in phone_numbers if re.match(pattern, number)]
print(*valid_numbers)
