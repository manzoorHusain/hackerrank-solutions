
#! Problem link: https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    # Write your code heremar
    mars_str = s
    changed_char = 0
    for i in range(0,len(mars_str),3):
        # print(mars_str[i],mars_str[i+1],mars_str[i+2])
        if mars_str[i] != 'S': changed_char += 1
        if mars_str[i+1] != 'O':  changed_char += 1
        if  mars_str[i+2] != 'S': changed_char += 1
    return changed_char
print(marsExploration('SOSTOT'))