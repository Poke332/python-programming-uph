def before_an_exam(d, sumTime):
    time_range = list()
    
    for _ in range(d):
        d_line = input().strip().split(" ")
        min_time, max_time = int(d_line[0]), int(d_line[1])
        time_range.append([min_time, max_time])
        
    sum_min_time = sum(x for x, _ in time_range)
    sum_max_time = sum(y for _, y in time_range)
    
    if sum_min_time <= sumTime <= sum_max_time:
        print("YES")
        result = list()
        for min, max in time_range:
            remainder = sumTime - sum_min_time
            if sumTime > sum_min_time:
                minRem = min+remainder
                if minRem in range(min, max+1):
                    sumTime -= minRem
                    sum_min_time -= min
                    result.append(str(minRem))
                else:
                    sumTime -= max
                    sum_min_time -= min
                    result.append(str(max))
            else:
                result.append(str(min))
        
        print(" ".join(result))
                
    else:
        print("NO")

first_input = input().strip().split(" ")
d, sumTime = first_input
d ,sumTime = int(d), int(sumTime)
before_an_exam(d, sumTime)


    