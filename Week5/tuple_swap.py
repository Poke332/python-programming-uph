num = list(map(int, input().split()))
num[0] , num[len(num)-1] = num[len(num)-1], num[0]
num = tuple(num)
print(num)