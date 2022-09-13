# hikes = 'DDUUUUDD'
hikes = 'UDDDUDUU'
print(len(hikes))
total_valleys = 0
sea_level = 0
for h in hikes:
    if h == 'D':
        sea_level -= 1
    else:
        sea_level += 1
    if h == 'U' and sea_level == 0:
        total_valleys += 1
# if hikes[-1] == 'U':
#     print("total valleys: ", total_valleys)
# else:
#     print("total valleys: ", total_valleys -1)
print(total_valleys)
