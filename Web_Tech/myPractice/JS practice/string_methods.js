// ---EASY LEVEL


// 10 JavaScript String Coding Problems
// Easy
// level


//! 1. Reverse a String
//! Write a function to reverse a given string.


//* solution
// function reverse(s) {
//     rev = ''
//     for (let i = 0; i < s.length; i++) {
//         rev = s.charAt(i) + rev
//     }
//     return rev
// }
// let s1 = 'hello'
// console.log();
// console.log(reverse(s1))

// let s2 = 'hello'
// console.log(s2.split('').reverse().join(''))

// ----------------------------------------

//! 2. Check Palindrome
// Example:
// js
// Input: "madam"
// Output: true

//* solution

// function reverse(s) {
//     rev = ''
//     for (let i = 0; i < s.length; i++) {
//         rev = s.charAt(i) + rev
//     }
//     return rev
// }
// let str = 'madam'
// console.log(str == reverse(str))
// let str = 'madam'
// console.log(str == str.split('').join(''))


// ! 3. Count Vowels in a String
// let s = 'Deepavali'
// let count = 0
// for (let i = 1; i < s.length; i++) {
//     if ('aeiouAEIOU'.includes(s.charAt(i))) {
//         count += 1
//     }
// }
// console.log(count)


//! 4. Find the First Non-Repeating Character
//! Return the first character that appears only once. 
//! Input: "aabbcde" Output: "c"

// let s = "aabbcde"
// for (let i = 0; i <s.length; i++) {
//     if ((s.slice(0,i).includes(s.charAt(i))==false && s.slice(i+1).includes(s.charAt(i))==false)){
//         console.log(s.charAt(i))
//         break
//     }
// }


// let s='aabbcde'
// for (let i = 0; i <s.length; i++) {
//     if (s.indexOf(s.charAt(i),s.indexOf(s.charAt(i))+1)==-1){
//         console.log(s.charAt(i))
//         break
//     }
// }


// let s='aabbcde'
// for (let i = 0; i <s.length; i++) {
//     if (s.indexOf(s.charAt(i))==s.lastIndexOf(s.charAt(i))){
//         console.log(s.charAt(i))
//         break
//     }
// }


//! 5. Remove Duplicate Characters
// Example:


// js
// Input: "programming"
// Output: "progamin"
// Remove duplicate characters while maintaining their original order.
// let s='programming'
// let out=''
// for(let i=0; i<s.length; i++){
//     if ((out.includes(s.charAt(i)))==false){
//         out=out.concat(s.charAt(i));
//     }
// }
// console.log(out);


//! 6. Check Whether Two Strings Are Anagrams
//! Example: Input: "listen", "silent" Output: true
//! Two strings are anagrams if they contain the same characters with the same frequency.
let s1='listen'
let s2='silents'
let flag=true
for(let i=0; i<s1.length; i++){
    if (s1.indexOf(s1.charAt(i))!=s1.lastIndexOf(s1.charAt(i))){
        flag=false
        break;
    }
}
console.log(flag);

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


