
# n = 9
# binary = bin(n)
# compliment = ~n
# print(binary)
# print(bin(compliment))
# print('{:032b}'.format(~9))
# previous_compliment = '{:032b}'.format(~9)
# # print(type(previous_compliment))
# new_val = int(previous_compliment) + 2**32
# print(new_val)


def flipping_bits(n):
    thirty_two_bit = '{:032b}'.format(n)
    converted_bits = ''
    for i in thirty_two_bit:
        if i=='0':
            converted_bits += '1'
        else:
            converted_bits += '0'
    int_val = int(converted_bits,2)
    return int_val

print(flipping_bits(9)) #! Expected: 4294967286
print(flipping_bits(2147483647)) #! Expected: 2147483648
print(flipping_bits(1)) #! Expected: 4294967294
print(flipping_bits(0))#! Expected: 4294967295
