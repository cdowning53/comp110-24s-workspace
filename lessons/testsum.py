vals: list[bool] = [1.1, 0.9, 1.0]

def w_sum(vals):
    total = 0.0
    index = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total

print(w_sum([1.1, 0.9, 1.0]))

