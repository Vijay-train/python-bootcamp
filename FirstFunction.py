# create def
# call
# pass parameters
# default values


def MySum (a,b=1000) :
    calcSum = a + b 
    print ("The sum is ",calcSum)
    print(globalSum)
    

globalSum = 500
MySum(10,20)
print ("The sum is ",globalSum)


# global varibale - that is defined in global scope, that is not within a particular function
# are avaioable across the file

# local variable - that is defned in local scope, within that function only
# it cannot be accessed outside the function


