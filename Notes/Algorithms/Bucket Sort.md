# Bucket Sort

## What is it?

Bucket Sort (BS) is a distribution-based algorithm that:
 - Divides the input range into a fixed number of buckets.
 - Places each element into a bucket based on some function (usually proportional to value)
 - Sorts each bucket individually 
 - Concatenates the buckets

Works best when you know something about the distribution of the input.

## When & Why is it useful?

Can achieve O(n) time when input is uniformly distributed. 

Ideal when you don't need full comparison-based sorting, but rather want quick grouping. 

Great for problems where you need to cluster values, not just sort them.

## Implementation

We generally mplement the algorithm in the following way:
  1. Set up a list of empty buckets. A bucket is in itialised for each element in the array. 
  2. Iterate through the bucket list and insert elements from the array. 
  3. Sort each non-empty bucket. (If only a few elements in each bucket, use Insertion Sort)
  4. Visit the bukcets in order. Once the contents of each bucket are sorted, when concatenated, they will yield a list in which the elements are arranged based on your criteria. 

## Example 

Problem 347 - Top K Frequent Elements
```
def topKFrequent(nums, k):
    #Create a dictionary to store frequencies of each number
    h = {}

    #Count occurences of each number in nums
    for n in nums:
        h[n] = h.get(n,0)+1
    
    #Create a dictionary where key = frequency, value = list of numbers with that frequency
    bucket = {}

    #Fill the bucket with numbers grouped by their frequency
    for num, freq in h.items():
        if freq not in bucket: 
            bucket[freq] = [] 
        bucket[freq].append(num) 
        #If this frequency bucket does not exist yet create a new list for this frequency then add number to its frequency bucket.
    
    #This will store the final k most frequent numbers
    res = []

    #Find the max frequency present (upper bound for looping downwards)
    max_freq = max(bucket.keys())

    #Loop from the higheat frequency down to 1
    for i in range(max_freq, 0, -1):
        if i in bucket:
            for num in bucket[i]:
                res.append(num)
        #If any numbers have frequency i, append all numbers with this frequency
            #If we have collected k numbers, return them
            if len(res)==k:
                return res
    return res
```

## Space & Time Complexity

Average / Best Case Scenario:
 - Time: O(n + k log k) if buckets sort small lists, approx O(n) when distribution is uniform
 - Space: O(n + k)

Worst Case
 - Time: O(n log n)
 - Space: O(n + k)

 Rule of Thumb: Bucket Sort is only optimal when data is well-spread!
