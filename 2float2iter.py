def float2data(floats, target, countIters=0, upper_bound=None):
    if not floats:
        return (countIters, upper_bound)

    mid = len(floats) // 2
    mid_val = floats[mid]
    countIters += 1

    if mid_val < target:
        return float2data(floats[mid + 1 :], target, countIters, upper_bound)
    else:
        upper_bound = mid_val
        if mid_val == target:
            return (countIters, upper_bound)
        return float2data(floats[:mid], target, countIters, upper_bound)


if __name__ == "__main__":
    data = [1.1, 2.5, 8.7, 10.3, 12.5]
    print(float2data(data, 9))

# Реалізуйте двійковий пошук для відсортованого масиву з дробовими числами.
# Написана функція для двійкового пошуку повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента.
# Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню
