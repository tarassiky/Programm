def two_sum(numbers, desired_sum):
    indices = []
    for x in range(len(numbers)):
        for y in range(x + 1, len(numbers)):
            if numbers[x] + numbers[y] == desired_sum:
                indices = [x, y]
                return indices
    return indices

# Пример использования
lst = [10, 20, 30, 40, 50]
target = 60
print(two_sum(lst, target))



