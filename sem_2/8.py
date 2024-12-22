import re


def cube_numbers_in_text(text):
    def cube_match(match):
        number = int(match.group())
        return str(number ** 3)

    result = re.sub(r'\b\d+\b', cube_match, text)
    return result


input_text = "Было закуплено 12 единиц техники по 410.37 рублей."
output_text = cube_numbers_in_text(input_text)
print(output_text)
