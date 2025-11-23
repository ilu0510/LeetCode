# Sets

## Purpose
A set is an unordered collection of unique, immutable elements. It is implemented as hash tables, and store unique keys only (no values).


## Python Implementation
Python implements sets using a hash-table–based data structure, very similar to dictionaries but storing only keys, not key-value pairs.

### Creation
```
my_set = {1, 2, 3}
empty_set = set() 
```
### Lookup
The element is hashed and its presence in the table is checked.
```
print(2 in my_set)
```
### Insertion
The element is hashed and placed into the hash table if it does not already exist.
```
my_set.add(4)
```
### Deletion
The element is hashed and removed from the set.
```
my_set.remove(2)     # Raises error if 2 not present
my_set.discard(2)    # Does nothing if 2 not present
my_set.clear()       # Removes all elements
```
### Mathematical Operations
```
A = {1, 2, 3}
B = {3, 4, 5}
A.union(B)         # {1, 2, 3, 4, 5}
A.intersection(B)  # {3}
A.difference(B)    # {1, 2}
A.symmetric_difference(B)  # {1, 2, 4, 5}
```

## Time and Space Complexity

### Time Complexity
Insertion: Average: O(1), Worst Case: O(n) 

Lookup: Average: O(1), Worst Case: O(n)   
  
Deletion: Average: O(1), Worst Case: O(n)

### Space Complexity
As each key occupies constant space, complexity is O(n).


