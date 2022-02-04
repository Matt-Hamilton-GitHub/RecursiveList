def sum(lis):
    if len(lis) == 0:
        return 0
    else:
        return lis[0] + sum(lis[1:])
    

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('The Given list:',myList)
print('Sum:',sum(myList))
