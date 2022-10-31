# stock_prices =[]
# with open("prices.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_prices.append([day,price])
# print(stock_prices)

# stock_prices = {}
# with open("prices.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_prices[day] = price
# print(stock_prices)
# print(stock_prices['march 9'])

class Hash_Table:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)] # list comprehension done and assigning each value None

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    # def add(self,key,val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

t = Hash_Table()
t['march 6'] = 130
t['march 4'] = 128
t['march 5'] = 129
t['march 17'] = 459
print(t.arr)
print(t['march 6'])
print(t['march 17'])
del t['march 6']
print(t.arr)