def BinarySearch(arr, l, h, x):

    # check if high index is greater than lower one
    if h >= l:
        # Calculate mid index between them
        mid = (h+l)//2
        # If the finding element is present at middle index
        if arr[mid] == x:
            return mid
        # If the element at middle index is greater than the element to be found
        elif arr[mid] > x:
            # Recursively call the Binary Search function with decrementing the middle index by one and making it the higher index of the array
            return BinarySearch(arr, l, mid-1, x)
        # Other case is definitely that element at middle index is smaller than the element to be found
        else:
            # Recursively call the Binary Search function with incrementing the middle index and making it the starting index of the array
            return BinarySearch(arr, mid+1, h, x)
    else:
        # Element is not present in array
        return -1

arr = [2, 4, 6, 10]
x =6

sol = BinarySearch(arr, 0, len(arr)-1, x)

if sol != -1:
    print("Element is present at index", str(sol))
else:
    print("Element is not present in array")