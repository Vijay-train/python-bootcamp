'''
print("this is a set")

roll_no = {123,345,567}
print(roll_no)

# list of items.. there could be duplicates
# Unique items from this list

cities_visited = ["Mumbai","Delhi","Chennai","Kolkata","Hyd","Pune","Mumbai","Delhi"]

unique_visited = set(cities_visited)

print(cities_visited)
print(unique_visited)

# check if an item exists in a set
does_it_exist = "Pune123" in unique_visited # true or false
print(does_it_exist)

# add more to set
unique_visited.add("DW")
print(unique_visited)

unique_visited.discard("DW")
print(unique_visited)

# Set of 4 students
# check whether some student exists in that set, print the result
# if they dont exist, add them, print the result

# 11:15

# Comparing two sets
set1 = {"Vivek","Dilip","Gungun"}
set2 = {"Vivek","Divya","Sanjay"}

print("in both", set1 & set2)
print("in either", set1 | set2)
print("only set1", set1 - set2)
'''
# dictionaries
student =  { "name":"Vikky",
         "age":5,
          "roll_no":120 }
print(student)

student["Location"] = "Dantewada" # add
print(student)

student["Location"] = "Hyderabad" #update
print(student)

# check if a key dic in dict or not
check_location = "Location" in student # key exists in the dict called Student\
print(check_location)

# in is used checking key
check_location_value = "Hyderabad" in student.values()
print(check_location_value)

print(student.get("name"))


'''
1. Create a dictionary of inventory of 4 items ( Rice 10, Soap 20) Key - name of the item, 
value - count, print
2. Reduce the count of one of the items by 2 , print

3. Check if a key exists, if it exists then increment the value by 1
3.1 else, create a new key with value = 10

'''


''' 
Home (or class) work
Manage store order and inventory

1) You have a  Prices dictionary with 5 items and their prices
2) You have an out_of_stock set with 2 of the items (from the Prices dictionary)
3) You have an Order list, that has list of orders (list of items)
4) Loop through the Order list
4.1) for each order, if it is out of stock, print unavailable
4.2) else, keep a running total ( get the price from the Prices dictionary)
5) Print the final order value

'''


items = {
 "Apple": 10,
"Banana": 20,
"orange": 15,
"Kiwi": 5
}

print("Original items:", items)

items["Apple"] -= 2
print("After reducing Apple:", items)

exist_item = "Apple"
if exist_item in items:
    items[exist_item] += 1
else:
    items[exist_item] = 10
    
print("Final items:", items)












