no_of_elements = int(input("Enter the total number of cards: "))  # Input total number of cards

# input space separated integer values and map them into list
elements = list(map(int, input("Enter the numbers on the card separated by space: ").split()))

elements.sort()  # Sorting the list

required_number = int(input("Enter the number to be found: "))


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo+hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1


def first_position(number_array, required):
    def condition(mid):
        if number_array[mid] == required:
            if mid > 0 and number_array[mid-1] == required:
                return 'left'
            else:
                return 'found'
        elif number_array[mid] < required:
            return 'right'
        else:
            return 'left'
    lo, hi = 0, len(number_array)-1
    return binary_search(lo, hi, condition)


def last_position(number_array, required):
    def condition(mid):
        if number_array[mid] == required:
            if mid < 0  and number_array[mid+1] == required:
                return 'left'
            else:
                return 'found'
        elif number_array[mid] < required:
            return 'right'
        else:
            return 'left'
    lo, hi = 0, len(number_array)-1
    return binary_search(lo, hi, condition)

def first_and_last_position(elements, required_number):
    return first_position(elements, required_number), last_position(elements, required_number)

output = print(first_and_last_position(elements, required_number))