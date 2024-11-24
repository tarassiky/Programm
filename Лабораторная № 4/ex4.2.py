def two_sum_hashed(lst, target):
    seen = {}
    for i, num in enumerate(lst):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Пример использования
lst = [10, 20, 30, 40, 50]
target = 60
print(two_sum_hashed(lst, target))