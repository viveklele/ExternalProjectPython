def binay_search(list1, num):
    
    list1.sort()
    low = 0
    high = len(list1)
    found = False
    while low <= high and not found: #low=0, high= 8
        mid = (low + high)//2          # mid = 4
        if num == list1[mid]:           #
            found = True
        elif num > list1[mid]:
            low = mid+1    #low = 5
        else:
            high = mid -1
    if found == True:
        print(num)
    else:
        print('num not found')
        
list1 = [12, 54, 64, 23, 754, 423, 123, 1213]
print(list1)    
num = int(input("Enter number= "))
binay_search(list1, num)