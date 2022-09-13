


def sum_pairs(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i] + arr[j]) % 5 == 0:
                print(arr[i],arr[j])
    # return



arr = [1,2,3,4,5,6]
sum_pairs(arr)

class Demo:
    """
    this works fine for me
    """
    def info(self):
        """ Self method"""
        print("this is info() ")
d = Demo()
print(d.__doc__)
print(d.info.__doc__)
import random as rd 
int_list = [i for i in range(1,10)]
print(int_list)