def greater_than_average(num_list):
    average = sum(num_list)/len(num_list)
    result = list()
    for num in num_list:
        if num > average:
            result.append(num)
    return result

numbers = list(map(int, input().split()))
print(greater_than_average(numbers))