list = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
list.sort()
print(list[len(list)-1], list[len(list)-2], list[len(list)-3])
print(list[0], list[1], list[2])
for i in range(len(list)):
    if list[i]>=10:
        print(list[i])