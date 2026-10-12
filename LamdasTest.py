# functions
def square(x):
    return x*x

cube = lambda y: y*y*y

add_gst = lambda price: price > 0

# <name> = lambda xx: 
#print(square(2))
#print(cube(3))
# print(add_gst(-5000))

# small function, that basically less # of line

# write a lambda call is_passing that wiill return true if marks >40

#mark = lambda is_pass: marks>40
#print(mark(60))


# how to sorted with lambda
items = [("zuchini",40),("Banana",100),("Apple",25)]
sortedItems = sorted(items,key=lambda item:item[0])

print(sortedItems)

'''
# map()

def myFunc(n):
    return len(n)

# call this function for 5 diff strings
#print(myFunc("Himanshu"))

x = list(map(myFunc,('apple','banana','orange')))

numbers=[1,2,3,4,5]
doubled= list(map(lambda x:x*2,numbers))

print(doubled)
'''