import re

input_string = input()
no_punctuation = re.sub(r'[^\w\s]', '', input_string)
result = no_punctuation[::2]
print(result)
