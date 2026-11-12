//~ easy array method questions

//! 1. Reverse and Join a Phrase
// Given an array of words: ["JavaScript", "is", "awesome"]
// Use methods to transform this into the string "awesome - is - JavaScript
//* solution
let a=["JavaScript", "is", "awesome"]
console.log(a.reverse().join(' - '));


//! 2. Move the First Element to the End
// Given an array ["apple", "banana", "cherry"], mutate it so that the first element is removed and placed at the very end of the array. The final array should be ["banana", "cherry", "apple"].
//* solution
let a= ["apple", "banana", "cherry"]
let p=a.shift()
console.log(p);
a.push(p)
console.log(a);


//! 3. Move the Last Element to the Front
// Given an array [10, 20, 30, 40], mutate it so that the last element is removed and placed at the beginning of the array. The final array should be [40, 10, 20, 30].
//* solution
let a=[10,20,30,40]
let l=a.pop()
a.unshift(l)
console.log(a);

//! 4. Check if All Numbers Are Positive, or if Any Are Zero
// Given an array [3, 7, 0, 12, 5]:
// Check if every number is greater than zero (should return false).
// Check if at least one number equals zero (should return true).
let a=[3, 7, 0, 12, 5]
console.log(a.every( (s)=>s>0 ));
console.log(a.some( (n)=>n==0 ));

//! 5. Find the First and Last Negative Number
// Given an array [5, -2, 9, -7, 3, -1, 4]:
// Find the first negative number.
// Find the index of the last negative number.
//* solution
let a=[5, -2, 9, -7, 3, -1, 4]
console.log(a.find((n)=>n<0))
console.log(a.findLast((n)=>n<0))


//! 6. Extract a Portion and Insert New Items
// Given an array ["red", "green", "blue", "yellow", "purple"]:
// Create a new array containing just ["green", "blue"] without changing the original array.
// In the original array, replace "yellow" with "orange" in-place.
//* solution
log

//NOTE: cant su epslice or pop cos it changes the array and splice does not change original array