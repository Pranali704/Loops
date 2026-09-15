numbers = [10, 20, 30, 40, 50]

sum = 0
i = 0

while i < len(numbers):
    sum = sum + numbers[i]
    i = i + 1

average = sum / len(numbers)

print("Average =", average)