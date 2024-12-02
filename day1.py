with open('input') as file:
    list1, list2 = [], []
    while True:
        a = file.readline()
        if not a:
            break
        num1, num2 = a.split()
        list1.append(int(num1))
        list2.append(int(num2))
    list1.sort()
    list2.sort()

    diff = 0
    for i in range(len(list1)):
        diff += abs(list1[i] - list2[i])
    print(diff)


