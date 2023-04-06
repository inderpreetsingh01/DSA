# Hashing

- Mostly useful when dealing with **Search, Insert and Delete** only.
- Search, Insert, Delete are all O(1) operations.
- All keys are unique.
- Deleting means deleting the key and its value from hash table.


Not used for:
- Finding closest value
- Sorted data
- Prefix searching

## Applications of Hashing
Hash table is popular data structure in Computer Science
1. Dictionaires
2. Database Indexing
3. Cryptography
4. Caches
5. Symbol tables in Computers/Interpreters
6. Routers
7. Caches
8. Getting data from databases


### Direct Access Table:
- An array with boolean value based on if index is present in data or not.
- Only suitable for small range of integers, cannot handle string, float, large integers.

### Hash Function
- Should always map a large key to same small key.
- Should generate values from 0 to m-1.
- be fast, O(1) for integers/float and O(len) for string of length len.
- Uniformly distribute arge keys to hash table slots.


### Hash tables: 
- C++ => unordered_set and unordered_map.
- Python => set and dictionary


___

### Q1 Count distinct elements in array
### Q2 Intersection, Union, subtraction of sets
### Q3 Is subarray with zero sum present?
### Q4 Is Subarray with given sum present?
### Q5 Find the longest subarray with given sum.
### Q6 Longest subarray with equal zero and one
### Q7 Longest common span with same sum in two binary 
arrays
### Q8 Longest consecutive subsequence
### Q9 Count of distinct element in every sliding window
### Q10 More than n/k Occurences
### Q11 More than n/k Occurrences (O(nk) solution)*

