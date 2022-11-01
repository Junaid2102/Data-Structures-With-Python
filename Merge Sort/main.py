def MergeSort(unsort):
    if len(unsort)>1:
        mid = len(unsort) // 2
        lhalf = unsort[:mid]
        rhalf = unsort[mid:]
    lhalf.sort()
    rhalf.sort()
    solution = []
    i, j =0, 0
    while i<len(lhalf) and j<len(rhalf):
        if lhalf[i] < rhalf[j]:
            solution.append(lhalf[i])
            i+=1
        else:
            solution.append(rhalf[j])
            j+=1
    print(solution)

    # print(lhalf)
    # print(rhalf)


unsort = list(map(int, input("Enter unsorted array: ").split(' ')))
MergeSort(unsort)