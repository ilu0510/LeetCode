# Hashmaps

## Purpose
Hashing is the process of transforming any given key or a string of characters into another value. Hashmaps store key-value pairs in a list that is accessible through its index. 

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

## Dictionary Methods
```
.keys()                   #Returns iterable list of keys
.values()                 #Returns iterable list of values
.get(keyname, value)      #Returns value of item with the specified key (even if the key does not exist)
.items()                  #Returns a view object that contains all the key-value pairs as tuples
```


## Time and Space Complexity

### Time Complexity
Insertion: Average: O(1), Worst Case: O(n)

Lookup: Average: O(1), Worst Case: O(n)  
  
Deletion: Average: O(1), Worst Case: O(n)

### Space Complexity
As each key-value pair occupies constant space, complexity is O(n).
