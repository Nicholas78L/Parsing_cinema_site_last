# count = []
# count =[
#     '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25',
#     '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25'
# ]
agl_cl = ['1', '2', '6', '7', '21']
data = [['1'], ['2, 3, 4, 5'], ['6, 7, 8, 9, 10', '11, 12, 13, 14, 15', '16, 17, 18, 19, 20', '21, 22, 23, 24, 25']]
print('len(data)', len(data))
# print('len(count)', len(count))


for g in range(0, len(agl_cl)):
    count = 0
    for f in range(0, len(data)):
        if agl_cl[g] in data[f][1]:
            print('Ok')
        count += 1


        # print('count[g][f]', count[g][f])
        # print('len(count)', len(count))


