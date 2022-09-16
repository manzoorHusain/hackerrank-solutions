def plusMinus(arr):
    # Write your code here
    size = len(arr)
    count_zero = count_p = count_n = 0
    for i in arr:
        if i<0: count_n += 1
        if i>0: count_p += 1
        if i==0: count_zero += 1
    # print("%.6f" %(size/count_p),"\n","%.6f" %(size/count_n),"\n","%.6f" % (size/count_zero))
    print("{0:.6f}".format(count_p/size))
    print("{0:.6f}".format(count_n/size))
    print("{0:.6f}".format(count_zero/size))