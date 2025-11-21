# Hashmaps

## Purpose
Hashing is the process of transforming any given key or a string of characters into another value. Hashmaps store key-value pairs 
in a list that is accessible through its index. 

## Python Implementation
Python implements hashmaps through the dictionary data-type. These dictionaries are mutable, meaning that the items can be changed, 
added or removed after the dictionary is created. The keys are immutable and unique. 

### Creation
```
dict = {key1:value1, key2:value2, key3:value3}
```
### Lookup
The key is hashed to find the index, and the value at that index is returned. 
```
print(dict[key1])
#Expected output: value1
```
### Insertion
The key-value pair is hashed, and the resulting index is used to store the value in the corresponding slot.
```
dict[key4] = value4
```
### Deletion
The key is hashed to find the index, and the item at that index is removed. 
```
del dict[key1] #Deleting specific key-value pair
dict.clear()   #Deleting all
```

## Time and Space Complexity

### Time Complexity
Insertion (average): O(1) --> Worst Case: O(n) 
Lookup (average): O(1) --> Worst Case: O(n)     
Deletion (average): O(1) --> Worst Case: O(n)  

### Space Complexity
As each key-value pair occupies constant space, complexity is O(n).

