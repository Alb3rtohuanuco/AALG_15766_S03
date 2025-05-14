a = [2*x for x in range(1,10+1)]
print(a)

i = [2*n +1 for n in range (0,5)]
print(i)

b=[(2*x)+1 for x in range(1,10+1)]
print(b)

print([n for n in range(1,10,2)])

print([0 if x % 3 == 0 else x for x in range(1,10,2)])