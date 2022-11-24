# Make sure that numbers length is even and same
def karatsuba(a, b):
    if(a<10 or b<10):
        return a*b
    else:
        astring = str(a)
        bstring = str(b)

        k = max(len(astring), len(bstring))
        mid = int(k/2)
            # Finding Higher bits for each no.
        i = int(astring[:-mid])
        j = int(bstring[:-mid])
            # Finding Lower bits for each no.
        k = int(astring[-mid:])
        l = int(bstring[-mid:])

        ij = karatsuba(i, j)
        kl = karatsuba(k, l)

        il_plus_kj = karatsuba(i + k, j + l) - ij - kl
        return ij*10**(2*mid) + il_plus_kj*10**(mid) + kl


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Answer is: ")
# print(karatsuba(3425, 2486))
print(karatsuba(a,b))