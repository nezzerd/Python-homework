import re

input_string = input()
vowels = r'\b[аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU]\w*'
words = re.findall(vowels, input_string)
print(*words)
