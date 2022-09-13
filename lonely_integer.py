arr = [1,2,3,4,3,2,1]
arr_dict = dict()
for a in arr:
    if a in arr_dict:
        # arr_dict[a] = arr_dict[a] +1
        arr_dict[a] +=1
    else:
        arr_dict[a] = 1
# for d in arr_dict:
#     if arr_dict[]
for d in arr_dict:
    if arr_dict[d] == 1:
        print(d)
    # print(d)
# print(arr_dict)