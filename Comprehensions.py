
'''
prices = [100, 250, 80] 
doubled = []
for p in prices: 
    doubled.append(p * 2)


print(doubled)
prices1 = [100, 250, 80]
doubled1 = [p * 2 for p in prices1 if p >200] # List comprehension
print(doubled1)

ages = [12, 25, 17, 30] 
adults = [a for a in ages if a >= 18]

ages1 = [12, 25, 17]
tags = ["adult" if a >= 18 else "minor" for a in ages1] # ['minor', 'adult', 'minor']

# dictionary comprehension
prices = {"tea": 10, "samosa": 15, "vada pav": 20}

costly = {k: v for k, v in prices.items() if v > 10}
print(costly)

doubled = {k: v * 2 for k, v in prices.items()}
print(doubled)

# class work
print ()
print("### Dictionary comprehension ###")
report = {"asha": 72, "kabir": 35, "meera": 88}
print ("Original", report)
passed = {n: m for n, m in report.items() if m >= 40}
print("Passed ", passed)

bonus = {n: m + 5 for n, m in report.items()}
print("With bonus ", bonus)

swapped = {m: n for n, m in report.items()}
print("Swapper ",swapped)


# set comprehension

cities = ["pune", "patna", "delhi", "goa", "dehradun"]
# set comprehension
# p,p,d,g,d
letters = {c[0] for c in cities}
print("First letters of the cities", sorted(letters))

grid = [[1, 2], [1, 4]]
print("Original Grid ",grid)
flat = [x for row in grid for x in row]
print("Flattened ",flat)

'''

# lazy generators
def evens(limit):
    n = 0
    while n <= limit:
        yield n
        n += 2

gen = evens(6)

'''
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
'''

print(list(evens(6)))