costs = {
    1: "AЕIOULNSTRАВЕИНОРСТ",
    2: "DGДКЛМПУ",
    3: "BCMPБГЁЬЯ",
    4: "FHVWYЙЫ",
    5: "KЖЗХЦЧ",
    8: "JXШЭЮ",
    10: "QZФЩЪ"
}
costs_dict = {}
for cost, letters in costs.items():
    for letter in letters:
        costs_dict[letter] = cost
word = input().upper()
cost = sum(costs_dict[letter] for letter in word if letter in costs_dict)
print(cost)
