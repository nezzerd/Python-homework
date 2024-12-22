squares = {i: i**2 for i in range(1, 1001)}
sum_even_keys = sum(value for key, value in squares.items() if key % 2 == 0)
print(sum_even_keys)