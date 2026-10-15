def classify(value):
    if value < 198:
        return "Below range"
    elif value <= 202:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    average_result = total / count
    return average_result


n = int(input("Enter the number of strips: "))
total = 0
below = 0
in_range = 0
above = 0

for i in range(n):
    length = int(input("Enter the strip length: "))
    result = classify(length)
    print(result)
    total += length
    if result == "Below range":
        below += 1
    elif result == "In range":
        in_range += 1
    else:
        above += 1

average = calculate_average(total, n)

print(f"Total length: {total} mm")
print(f"Average length: {average} mm")
print(f"Below range: {below}")
print(f"In range: {in_range}")
print(f"Above range: {above}")