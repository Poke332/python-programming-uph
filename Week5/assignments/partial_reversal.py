def partial_reversal(num_list, ith, jth):
    number_of_reversal = jth - ith
    for _ in range(number_of_reversal):
        if jth <= ith:
            break
        num_list[ith-1], num_list[jth-1] = num_list[jth-1], num_list[ith-1]
        ith+=1
        jth-=1
    return num_list
    
if __name__ == "__main__":
    first_line = list(map(int, input().split()))
    if len(first_line) != 3:
        raise ValueError("First input requires 3 integers split by spaces")
    
    n, i, j = first_line
    if not (0 < n <= 100 and 1 <= i < j<= n):
        raise ValueError("Not in range")
    
    num_list = list(map(int, input().split()))
    if len(num_list) != n:
        raise ValueError(f"Expected {n} numbers of entries, received {len(num_list)}")
    
    result = partial_reversal(num_list, i, j)
    print(" ".join(list(map(str, result))))