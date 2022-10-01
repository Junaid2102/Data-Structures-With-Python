number = list(map(int, input("Enter the numbers separated by space: ").split()))
print(number)
def min_rotation(num):
    lo, hi = 0, len(num)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if num[mid] < num[mid - 1]:
            return mid
        elif num[mid] < num[lo]:
            hi = mid - 1
        elif num[mid] > num[hi]:
            lo = mid + 1
    return -1

print(min_rotation(number))