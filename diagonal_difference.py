import math
arr = [[1,2,3],[4,5,6],[9,8,9]]
j = 0
k = len(arr) -1
right_diag = []
left_diag = []
sum_left_diag = 0
sum_right_diag = 0

for i in range(len(arr)):
    left_diag.append(arr[i][j])
    sum_left_diag += arr[i][j]
    right_diag.append(arr[i][k])
    sum_right_diag += arr[i][k]
    j += 1
    k -= 1

print("left diagonal: ",left_diag)
print("right diagonal: ",right_diag)
print(sum_right_diag)
print(sum_left_diag)
print("Absolute value: ",abs(sum_left_diag - sum_right_diag))
# print(math.)
