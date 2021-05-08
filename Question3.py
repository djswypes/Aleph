import random

#array = [64, 32, 16, 8, 4, 2, 1]
array = [32, 1, 4, 8, 64, 2, 16]

def random_select(array):
    result = {}

    for n in range(10000000):
        sum = 0
        temp_array = array.copy()

        while sum <= 124:
            choice = random.choice(temp_array)
            temp_array.remove(choice)
            sum += choice

        if sum in result.keys():
            result[sum] += 1
        else:
            result[sum] = 1

    return result

result = random_select(array)
max_value = max(result, key=result.get)

print(max_value)