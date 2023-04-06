# Strings

### Q1 Print frequencies of characters in sorted order in a string of lower case alphabets
### Q2 Check Palindrome
### Q3 Check if a string is subsequence of other
### Q4 Check if anagram
### Q5 leftmost repeating character
### Q6 leftmost non repeating character
### Q7 reverse order of words in string using O(1) aux space *
### Q8 



## Pattern Matching algorithm 
### Q8 Naive pattern searching (sliding window based)
### Q9 Improved pattern searching when elements are distinct
### Q10 Rabin Karp algorithm 
- Used when there are multiple patterns to be found in text.
- Precomutes a hash function for given patterns
- Computes hash function in rolling window fashion (update based on removing first element of window and adding new element)
- If hash function matches then iteratively checks for all the characters
- Use modulus with prime number (largest prime number possible to avoid spurious hits) to calculate hash function.

### Q11 KMP Algorithm*
- Q.11_a Constructing LPS array in linear time
- Q.11_b Using LPS array to match pattern using sliding window method
If all characters in pattern are distinct than naive algorithm also takes linear time,
but KMP algorithm takes linear time even in worst case when there are redundancies in pattern since it preprocess the redundancies.

### Q12 Check if strings are rotation



