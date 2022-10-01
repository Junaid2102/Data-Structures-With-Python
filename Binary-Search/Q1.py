no_of_cards = int(input("Enter the total number of cards: "))  # Input total number of cards

# input space separated integer values and map them into list
no_on_cards = list(map(int, input("Enter the numbers on the card separated by space: ").split()))

no_on_cards.sort(reverse=True)  # Reverse the list
#print(no_on_cards)

to_found_number = int(input("Enter the number to be found: "))

# Using simple Algorithm
'''def locate_card(cards, number):
    position = 0
    while position < len(cards):
        if cards[position] == number:
            print(position)
        position += 1
        if position == len(cards) - 1:
            print("Not Found")
locate_card(no_on_cards, to_found_number)'''

# Using Binary search

def check_location(cards, number, mid):
    mid_num = cards[mid]
    if mid_num == number:
        if mid-1 >= 0 and cards[mid-1] == number:
            return 'left'
        else:
            return 'found'
    elif mid_num < number:
        return 'left'
    else:
        return 'right'


def locate_card(cards, number):
    lo, hi = 0, len(cards)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        result = check_location(cards, number, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1


output = locate_card(no_on_cards, to_found_number)
print(output)