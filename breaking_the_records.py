
#! Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
def break_records(arr):
    min_count= max_count = 0
    max_num = min_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num= i
            max_count += 1
        if i < min_num:
            min_num = i
            min_count += 1
    
    return [min_count,max_count]
arr = [12,24,10,24]
print(break_records(arr))