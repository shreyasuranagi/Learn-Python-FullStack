# 🚀 JavaScript Array Methods & Algorithm Practice

# EASY ARRAY METHOD QUESTIONS
Fair enough! That last list leaned heavily into algorithmic problem-solving. If your primary goal right now is to **build muscle memory for how these specific methods work**, the questions should focus on method mechanics rather than tricky algorithms.

Here are 10 questions at a **beginner-to-intermediate** level. They are straightforward enough to help you master the allowed methods, but still require combining 2–3 of them so you aren't just writing a 1-liner `.indexOf()`.

---

### 1. Reverse and Join a Phrase

Given an array of words: `["JavaScript", "is", "awesome"]`

Use methods to transform this into the string `"awesome - is - JavaScript"`.

* **Methods to practice:** `toReversed()` (or `reverse()`), `join()`

---

### 2. Move the First Element to the End

Given an array `["apple", "banana", "cherry"]`, mutate it so that the first element is removed and placed at the very end of the array. The final array should be `["banana", "cherry", "apple"]`.

* **Methods to practice:** `shift()`, `push()`

---

### 3. Move the Last Element to the Front

Given an array `[10, 20, 30, 40]`, mutate it so that the last element is removed and placed at the beginning of the array. The final array should be `[40, 10, 20, 30]`.

* **Methods to practice:** `pop()`, `unshift()`

---

### 4. Check if All Numbers Are Positive, or if Any Are Zero

Given an array `[3, 7, 0, 12, 5]`:

1. Check if **every** number is greater than zero (should return `false`).
2. Check if **at least one** number equals zero (should return `true`).

* **Methods to practice:** `every()`, `some()`

---

### 5. Find the First and Last Negative Number

Given an array `[5, -2, 9, -7, 3, -1, 4]`:

1. Find the **first** negative number.
2. Find the **index of the last** negative number.

* **Methods to practice:** `find()`, `findLastIndex()`

---

### 6. Extract a Portion and Insert New Items

Given an array `["red", "green", "blue", "yellow", "purple"]`:

1. Create a new array containing just `["green", "blue"]` without changing the original array.
2. In the original array, replace `"yellow"` with `"orange"` in-place.

* **Methods to practice:** `slice()`, `splice()`

---

### 7. Flatten and Check for Inclusion

Given a nested array `[1, [2, 3], 4, [5, 6]]`:

1. Flatten it by 1 level.
2. Check if the flattened array contains the number `3`.

* **Methods to practice:** `flat()`, `includes()`

---

### 8. Merge and Sort Numbers

Given two arrays `[40, 10]` and `[30, 20]`:

1. Combine them into a single 4-element array.
2. Sort the combined array in ascending order `[10, 20, 30, 40]`.

* **Methods to practice:** `concat()`, `sort()`

---

### 9. Fill a Grid Placeholder

Create an array of length 5 filled entirely with the number `0`. Then, replace the middle 3 elements (indices 1, 2, 3) with `"X"`.

* **Methods to practice:** `Array(5).fill()`, `fill()` (with start/end indices) or `splice()`

---

### 10. Find Index using Entries Iteration

Given an array `["cat", "dog", "elephant", "fox"]`:
Use `.entries()` with `.find()` to locate the entry whose word has more than 5 letters, and output its index and word as `[2, "elephant"]`.

* **Methods to practice:** `entries()`, `find()`


### 11. Remove an Item by Name In-Place

Given an array `["apple", "banana", "cherry", "date"]` and a target string `"cherry"`:

1. Find the position of `"cherry"`.
2. Remove it from the original array using its index.

* **Methods to practice:** `indexOf()`, `splice()`

---

### 12. Swap the First and Last Elements

Given an array `[10, 20, 30, 40, 50]`:
Without manually typing index numbers like `array[0]` or `array[4]`, swap the first and last elements in-place using array methods.

*(Result should be `[50, 20, 30, 40, 10]`)*.

* **Methods to practice:** `shift()`, `pop()`, `unshift()`, `push()`

---

### 13. Check Order Consistency Across Copies

Given an array `[5, 1, 8, 3]`:

1. Create a reversed copy of the array without modifying the original.
2. Check if **some** elements in the reversed copy are larger than `5`.

* **Methods to practice:** `toReversed()`, `some()`

---

### 14. Find the Last Word Longer Than 4 Letters and Its Index

Given an array `["cat", "elephant", "dog", "giraffe", "fox"]`:

1. Find the **last word** in the array that has more than 4 letters (`"giraffe"`).
2. Find the **index** of that exact word.

* **Methods to practice:** `findLast()`, `findLastIndex()`

---

### 15. Merge, Clean, and Slice

Given two arrays `[1, 2, 3]` and `[4, 5, 6]`:

1. Combine them into one array.
2. Extract only the middle 4 elements into a new array `[2, 3, 4, 5]` without changing the combined array.

* **Methods to practice:** `concat()`, `slice()`

---

### 16. Replace Every Negative Number with Zero

Given an array `[4, -2, 7, -9, 5]`:
Find the index of the first negative number, replace it with `0` in-place, and repeat until **every** element passes the check of being greater than or equal to `0`.

* **Methods to practice:** `findIndex()`, `splice()`, `every()`

---

### 17. Rotate Array Right by 1 Step

Given an array `["A", "B", "C", "D"]`:
Take the last element off the end and place it right at the front of the array so it becomes `["D", "A", "B", "C"]`.

* **Methods to practice:** `pop()`, `unshift()`

---

### 18. Find First Element After Index 2 That Matches a Condition

Given an array `[2, 12, 4, 18, 5, 22]`:
Find the **first number greater than 10** that appears *after* index 2 in the array.

*(Hint: slice first or use the index argument in the callback).*

* **Methods to practice:** `slice()`, `find()` (or `findIndex()`)

---

### 19. Create a Masked Array

Given an array of 6 elements `[1, 2, 3, 4, 5, 6]`:

1. Use a method to overwrite elements from index 2 up to (but not including) index 5 with `"X"`.
2. Verify if the array **includes** `"X"`.

* **Methods to practice:** `fill()`, `includes()`

---

### 20. Check Index Alignment using Entries

Given an array `["a", "b", "c", "d"]`:
Use `.entries()` with `.find()` to locate the entry where the **index matches the element's position** in an custom condition (e.g., find the entry where `index === 2`).

* **Methods to practice:** `entries()`, `find()`

---
---


# MEDIUM LEVEL ARRAY METHOD QUESTIONS


Here are 12 problem statements designed to test your JavaScript array skills using **only** the allowed method set:

> **Allowed Methods:**
> `push`, `pop`, `shift`, `unshift`, `slice`, `splice`, `concat`, `join`, `indexOf`, `includes`, `entries`, `keys`, `values`, `every`, `some`, `fill`, `find`, `findLast`, `findIndex`, `findLastIndex`, `flat`, `reverse`, `sort`, `toReversed()`

---

### 1. In-Place Duplicate Removal without Extra Memory

Given a sorted array of numbers (e.g., `[1, 1, 2, 2, 2, 3, 4, 4]`), modify the array **in place** so that each element appears only once, maintaining order.

* **Rules:** You cannot use `map`, `filter`, or `Set`.
* **Hint:** Combine `indexOf`, `lastIndexOf` (or index-checking with `findIndex`), and `splice`.

---

### 2. Find the Subarray Peak Index

Given an array of numbers that first increases and then decreases (e.g., `[1, 3, 8, 12, 9, 4, 2]`), find the index of the peak element (highest number).

* **Rules:** Solve it using `findIndex` or `find` by comparing adjacent elements within the method callback.

---

### 3. Check for Palindromic Array Structure

Write a function that returns `true` if an array reads the same forward and backward (e.g., `[1, "a", "b", "a", 1]`), and `false` otherwise.

* **Rules:** Use `toReversed()` and `every` (or `slice` + `reverse`).

---

### 4. Custom In-Place Array Rotation

Rotate an array to the right by `k` steps in-place. For example, rotating `[1, 2, 3, 4, 5]` by `k = 2` steps gives `[4, 5, 1, 2, 3]`.

* **Rules:** Do it using only `pop` and `unshift`, or `splice` combined with `unshift` and spread/`push`.

---

### 5. Find the First Pair That Sums to Target

Given an array of integers and a `target` sum (e.g., `nums = [2, 7, 11, 15]`, `target = 9`), return the indices of the first two numbers that add up to `target`.

* **Rules:** Solve this using `findIndex` combined with `slice` and `indexOf` (no loops or `map`).

---

### 6. Remove All Occurrences of an Element In-Place

Given an array and a value `val` (e.g., `[0, 1, 2, 2, 3, 0, 4, 2]`, `val = 2`), mutate the original array to remove all instances of `val`.

* **Rules:** Use a combination of `indexOf`, `includes`, and `splice`.

---

### 7. Interleave Two Arrays

Given two arrays of equal length (e.g., `["a", "b", "c"]` and `[1, 2, 3]`), merge them into a single interleaved array: `["a", 1, "b", 2, "c", 3]`.

* **Rules:** Do not use `map`. Use `keys()`, `concat()`, `push()`, or `splice()`.

---

### 8. Find the Single Outlier by Parity

Given an array of at least 3 integers, the array is either entirely comprised of odd integers or entirely comprised of even integers, except for a single outlier integer `N`. Find `N`.

Example: `[2, 4, 0, 100, 4, 11, 2602, 36]` $\rightarrow$ `11`

* **Rules:** Use `some`, `every`, `find`, or `findIndex`.

---

### 9. Check if Array is Monotonic

An array is monotonic if it is entirely non-increasing or entirely non-decreasing. Given `[1, 2, 2, 3]` return `true`. Given `[1, 3, 2]` return `false`.

* **Rules:** Use `every` or `some` together with `slice` or index matching via `keys()`.

---

### 10. Split Array into Chunk Batches of Size N

Given an array `[1, 2, 3, 4, 5, 6, 7]` and batch size `n = 3`, return `[[1, 2, 3], [4, 5, 6], [7]]`.

* **Rules:** Do not use loops (`for`/`while`). Use `splice` or `slice` in combination with array iteration methods like `keys()`.

---

### 11. Find First and Last Position of an Element

Given a sorted array `[5, 7, 7, 8, 8, 10]` and a target `8`, return `[3, 4]` (the start and end indices of `8`). If target is not found, return `[-1, -1]`.

* **Rules:** Use `indexOf`, `findIndex`, `findLastIndex`, and `includes`.

---

### 12. Flatten Nested Array up to Level 1 manually

Flattens an array containing elements or 1-level sub-arrays (e.g., `[1, [2, 3], 4, [5]]` $\rightarrow$ `[1, 2, 3, 4, 5]`) without using `.flat()`.

* **Rules:** Do not use `.flat()`, `.map()`, or `.reduce()`. Solve it using `concat`, `splice`, or `push` with spread syntax.

---

# ARRAY QUESTIONS WITHOUT USING BUILT IN METHODS


#### 🔥 : 10 Medium-Level Coding Challenges 
*(Constraint: Solve these **WITHOUT** using any built-in array methods like `map`, `filter`, `reduce`, `find`, `indexOf`, `slice`, `splice`, `sort`, `reverse`, `join`, `split`, etc. Use raw loops, pointers, and manual logic!)*

### 1. **Reverse an Array Manually**
Reverse the elements of an array in-place without using `.reverse()`.
```javascript
// Input: [1, 2, 3, 4, 5]
// Output: [5, 4, 3, 2, 1]


# Part 2: JavaScript Arrays – Medium Level

## Important Rules

Solve these questions WITHOUT using built-in array methods.

### Allowed:
- `for` loops
- `while` loops
- `if-else` conditions
- Variables and temporary variables
- Array indexing (`arr[i]`)
- Array length (`arr.length`)

### Not Allowed:
- `map()`
- `filter()`
- `reduce()`
- `forEach()`
- `sort()`
- `splice()`
- `slice()`
- `includes()`
- `indexOf()`
- `find()`
- `some()`
- `every()`
- `push()`

You can create new arrays using indexed assignments.

## 1. Find the Second Largest Element

Find the second-largest unique number without sorting the array.

Input: `[10, 50, 30, 80, 60]`  
Output: `60`

## 2. Move All Zeros to the End

Move all zeros to the end while maintaining the relative order of non-zero elements.

Input: `[0, 1, 0, 3, 12]`  
Output: `[1, 3, 12, 0, 0]`

## 3. Find Duplicate Elements

Find all elements that appear more than once.

Input: `[1, 2, 3, 2, 4, 5, 1]`  
Output: `[1, 2]`

## 4. Find the Missing Number

An array contains numbers from 1 to N, but one number is missing. Find it.

Input: `[1, 2, 4, 5, 6]`  
Output: `3`

## 5. Rotate an Array to the Right

Rotate an array to the right by K positions.

Input: `[1, 2, 3, 4, 5]`  
K: `2`  
Output: `[4, 5, 1, 2, 3]`

## 6. Find the Pair With a Given Sum

Find two elements whose sum equals the target.

Input: `[2, 7, 11, 15]`  
Target: `9`  
Output: `[2, 7]`

## 7. Separate Even and Odd Numbers

Separate even and odd numbers into two different arrays while maintaining their original order.

Input: `[1, 2, 3, 4, 5, 6]`

Output:
```js
Even: [2, 4, 6]
Odd: [1, 3, 5]
```

## 8. Find the Maximum Consecutive Sum

Find the maximum sum of any two consecutive elements.

Input: `[2, 1, 5, 1, 3, 2]`  
Output: `6`

## 9. Merge Two Sorted Arrays

Merge two already sorted arrays into a single sorted array without using sorting methods.

Input:
```js
[1, 3, 5, 7]
[2, 4, 6, 8]
```

Output:
```js
[1, 2, 3, 4, 5, 6, 7, 8]
```

## 10. Find the Frequency of Each Element

Count how many times each number appears without using built-in array-processing methods.

Input: `[1, 2, 2, 3, 1, 4, 2]`

Output:
```text
1 -> 2
2 -> 3
3 -> 1
4 -> 1
```


---

---
# REAL WORLD SCENARIO ARRAY METHOD QUESTIONS

1. **The Team Roster Initialization:** How would you quickly create an array of 5 default placeholder seats initialized with the string `"empty"`?
2. **The New Member Onboarding:** A new user joins your platform, and you need to append their username to the very end of your active users array.
3. **The Session Logout Cleaner:** A user logs out, and you need to remove the very last session token from your active session stack.
4. **The Priority Notification Queue:** A high-priority system alert arrives and needs to be placed at the immediate front (beginning) of your notification queue.
5. **The Shift Handover:** You are processing a print queue where the first print job must be removed and processed. How do you pull it from the front?
6. **The User Profile Splicing:** A user deletes their account located right in the middle of your active user array. How do you remove 1 item at a specific index without leaving an empty slot?
7. **The Sub-Playlist Extractor:** You need to slice out a specific range of songs from a playlist array (from index 2 to 5) to create a temporary preview queue.
8. **The Playlist Merger:** You have a guest playlist and a main playlist, and you need to combine them into a single continuous playback array.
9. **The Tag Serializer:** You need to convert an array of category tags into a single comma-separated string to display in a meta description tag.
10. **The Array Reverser:** You are displaying a chat history feed and need to reverse the order of messages so the newest ones appear at the top.
11. **The Alphabetical Leaderboard Sort:** You need to sort a list of player usernames alphabetically in ascending order.
12. **The Numerical Score Sorting:** You have an array of player scores (e.g., `[45, 12, 100, 3]`), and you need to sort them numerically from highest to lowest.
13. **The User ID Search:** You need to find the exact index position of a specific user ID string inside a tracking array.
14. **The Item Existence Check:** You want to check with a simple boolean (`true`/`false`) whether a specific product ID exists in your shopping cart array.
15. **The First Flagged User Locator:** You need to find the *first* user object in an array whose status property is marked as `"suspended"`.
16. **The Suspended User Index Locator:** You need to find the index of that *first* suspended user so you can target them for moderation.
17. **The Active Users Filter:** You have a mixed array of user accounts, and you need to filter out only the ones where `isActive` is `true`.
18. **The Price Discount Mapper:** You have an array of product prices and need to apply a 20% discount to generate a brand-new array of reduced prices.
19. **The Cart Total Accumulator:** You need to sum up all the item prices in a shopping cart array to calculate the final checkout total.
20. **The All-Items In-Stock Validator:** You want to check if *every* item in a user's order array has a `stock > 0` before allowing payment.
21. **The Any-Item On-Sale Checker:** You want to check if *at least one* item in a product catalog array has a `discount` flag set to `true`.
22. **The Nested Comments Flattener:** A blog post returns nested replies arrays inside comments, and you need to flatten them into a single linear array.
23. **The Department Employee Grouping & Mapping:** You need to extract user names and map/flatten them in a single step when processing department records.
24. **The Iterator Entry Extractor:** You need to loop through an array of configuration settings while getting both the numeric index and the value for each item.
25. **The Dynamic Array Filler:** You need to dynamically generate an array containing sequential numbers from 1 to 10 for a pagination bar.
26. **The Immutable Array Modification:** You want to update an item at index 2 in an array without mutating the original state (using modern copying methods).

---




# SOLUTION NOTES

### HEADING -
#### QUESTION NO.- 
- TRIED:
- MISTAKE-
- FINAL