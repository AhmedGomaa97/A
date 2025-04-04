def sort_array():
    array=[]
    print("Enter 5 elememts : ")
    for i in range(5) : 
        num = int(input())
        array.append(num)
    array.sort()
    print(array)
    array.reverse()
    print(array)
sort_array()