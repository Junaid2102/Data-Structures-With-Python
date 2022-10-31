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
        self.max = 100
        self.arr = [None for i in range(self.max)] # list comprehension done and assigning each value None

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
        self.arr[h] = val

    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
t = Hash_Table()
t['march 6'] = 130
t['march 4'] = 128
t['march 5'] = 129
print(t.arr)
print(t['march 6'])
del t['march 6']
print(t.arr)