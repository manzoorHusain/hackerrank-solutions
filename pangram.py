
#! Problem link: https://www.hackerrank.com/challenges/pangrams/problem
def pangram_naive_approach(s):
    import string
    lower_case_letters = string.ascii_lowercase
    pangram_str = s
    pangram_str = ''.join(pangram_str.split()).lower()
    pangram_dict = {}

    for p in pangram_str:
        if p in pangram_dict :
            pangram_dict[p] += 1
        else:
            pangram_dict[p] = 1
    # print(pangram_dict)
    flag = True
    for p in lower_case_letters:
        if p in pangram_dict:
            continue
            # print(p)    
        else:
            # print(p)
            flag = False
            break
    return "pangram" if flag else "not pangram"
def pangram_better_approch(s):
    # Write your code here
    s= ''.join(s.split()).lower()
    s = set(s)
    return 'pangram' if len(s) == 26 else 'not pangram'

s = 'We promptly judged antique ivory buckles for the next prize'
print("Apprach 1: ",pangram_naive_approach(s))
print("Appraoch 2: ",pangram_better_approch(s))