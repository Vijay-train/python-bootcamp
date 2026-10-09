'''
Lists

stops = ["MG Road", "Indiranagar", "Koramangala", "HSR Layout"]

Access
   [0].[1]..[-1]
   list[start:stop] .. can leave either print(cart[0:3])


** Problem **
* Create a list of numbers 1 to 10 
* Print just the middle 4 numbers (positions 3 to 6) using a slice

Modify
* append(item) adds one item to the end of the list
* insert(position, item) adds an item at a specific index, shifting everything after it

** Problem **
* Create a list of 3 tasks
* Use append() to add a 4th task to the end
* Use insert() to add a 5th task at position 0
* Print the final list

Remove
* remove(value) deletes the first item that matches that value
* pop(index) deletes the item at a position, and also returns it
* pop() with no index removes and returns the last item
 Other
* list.sort() sorts the list in place
* list.reverse() flips the order in place
 ** Problem **
* Start with a list of 4 product names
* Append 2 more products
* Remove the 2nd product using pop(1)
* Sort the final list alphabetically and print it
  Tuple
* Written with ( ) instead of [ ]
* Indexing and slicing work exactly the same as lists
* The difference: once created, a tuple cannot be changed — no append, no remove, no sort
 
Why Tuple?


Homework
Create a todo app
Options 
Choose an option
(1) to add an item (2) to delete an item at index (3) to remove the last item (4) to sort the list
 (5) To print the list (6) Exit the app

On (1)
- "Enter a task:"
repeat
- "-1" to go to prev menu

On (2)
- Ask for index,
- Delete that entry and print the list

On (3)
- Remove the last element and print the list

On (4)
- Sort the list and print

On (5) 
- Exit the app

'''

stops = ["d","z","c","a"]

'''
print(stops)

print (stops[0])
print(stops[-1])
print(stops[0:2])
print(stops[:2])
print(stops[2:4])

'''
# modify
stops.append("A1")
print(stops)

#stops.insert(1,"I1")
# print(stops)

stops.insert(-1,"I-1")
print(stops)

stops.insert(-1,"I-2")
print(stops)

# remove items from list

# stops.remove("4")
# print(stops)


stops.pop()
print(stops)

stops.sort()
print(stops)

stops.reverse()
print(stops)

// todo app





