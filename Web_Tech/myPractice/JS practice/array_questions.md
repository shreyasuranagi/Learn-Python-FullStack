# 🚀 JavaScript Array Methods & Algorithm Practice Guide

Here is your complete guide featuring **26 real-world scenarios** focused exclusively on **JavaScript Array Methods**, followed by **10 medium-level coding questions** that you must solve **WITHOUT using built-in array methods** (using manual loops, pointers, or logic instead)!

---

## 📋 Part 1: 26 Real-World Scenarios (Array Methods Focus)

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

## 🔥 Part 2: 10 Medium-Level Coding Challenges 
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