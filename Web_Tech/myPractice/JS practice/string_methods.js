



// ---EASY LEVEL


// 10 JavaScript String Coding Problems
// Easy
// level
 

//? 1. Reverse a String
//? Write a function to reverse a given string.


//^ solution
function reverse(s){
    rev=''
    for(let i=0; i<s.length; i++){
        rev=s.charAt(i)+rev
    }
    return rev
}
let s1='hello'
console.log();
console.log(reverse(s1))

let s2='hello'
console.log(s2.split('').reverse().join(''))


//? 2. Check Palindrome
// Example:
// js
// Input: "madam"
// Output: true

//^ solution



// 3. Count Vowels in a String
// Example:


// js
// Input: "javascript"
// Output: 3
// Count the number of vowels (a, e, i, o, u) in a given string.

// 4. Find the First Non-Repeating Character
// Example:


// js
// Input: "aabbcde"
// Output: "c"
// Return the first character that appears only once.

// 5. Remove Duplicate Characters
// Example:


// js
// Input: "programming"
// Output: "progamin"
// Remove duplicate characters while maintaining their original order.

// 6. Check Whether Two Strings Are Anagrams
// Example:


// js
// Input: "listen", "silent"
// Output: true
// Two strings are anagrams if they contain the same characters with the same frequency.

// 7. Find the Longest Word in a Sentence
// Example:


// js
// Input: "I love learning JavaScript programming"
// Output: "programming"
// Return the longest word in the given sentence.

// 8. Count Frequency of Each Character
// Example:


// js
// Input: "banana"

// Output:
// {
//   b: 1,
//   a: 3,
//   n: 2
// }
// Count how many times each character appears.

// 9. Capitalize the First Letter of Every Word
// Example:


// js
// Input: "hello world javascript"
// Output: "Hello World Javascript"
// Convert the first letter of every word to uppercase.


//! ----------------------------------------

//! 10. Find the Most Frequent Character
// Example:
// js
// Input: "success"
// Output: "s"


// //