def two_sum_hashed_all(lst, target):
    seen = {}
    result = []

    for i, num in enumerate(lst):
        complement = target - num

        if complement in seen:
            result.append([seen[complement], i])

        seen[num] = i

    return result


# Пример использования
lst = [10, 20, 30, 40, 50, 15, 45]
target = 60
print(two_sum_hashed_all(lst, target))