num_list = list(map(int, input().split()))
diviser = int(input())
new_list = [num for num in num_list if not num % diviser == 0]
print(sum(new_list))