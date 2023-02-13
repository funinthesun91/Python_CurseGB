def max_berries(berries):
    n = len(berries)
    max_sum = 0
    for i in range(n):
        current_sum = berries[i] + berries[(i-1) % n] + berries[(i+1) % n]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


berries = [10, 20, 30, 40, 50]
print("Максимальное количество ягод, которые можно собрать:", max_berries(berries))
