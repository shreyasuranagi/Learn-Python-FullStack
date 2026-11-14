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

// ----------------------------------------


// ! 3. Count Vowels in a String
//* solution
// let s = 'Deepavali'
// let count = 0
// for (let i = 1; i < s.length; i++) {
//     if ('aeiouAEIOU'.includes(s.charAt(i))) {
//         count += 1
//     }
// }
// console.log(count)

// ----------------------------------------


//! 4. Find the First Non-Repeating Character
//! Return the first character that appears only once. 
//! Input: "aabbcde" Output: "c"
//* solution
// let s = "aabbcde"
// for (let i = 0; i <s.length; i++) {
//     if ((s.slice(0,i).includes(s.charAt(i))==false && s.slice(i+1).includes(s.charAt(i))==false)){
//         console.log(s.charAt(i))
//         break
//     }
// }

// OR
// let s='aabbcde'
// for (let i = 0; i <s.length; i++) {
//     if (s.indexOf(s.charAt(i),s.indexOf(s.charAt(i))+1)==-1){
//         console.log(s.charAt(i))
//         break
//     }
// }

// OR
// let s='aabbcde'
// for (let i = 0; i <s.length; i++) {
//     if (s.indexOf(s.charAt(i))==s.lastIndexOf(s.charAt(i))){
//         console.log(s.charAt(i))
//         break
//     }
// }

// ----------------------------------------

//! 5. Remove Duplicate Characters
// Example:
// js
// Input: "programming"
// Output: "progamin"
// Remove duplicate characters while maintaining their original order.
//* solution
// let s='programming'
// let out=''
// for(let i=0; i<s.length; i++){
//     if ((out.includes(s.charAt(i)))==false){
//         out=out.concat(s.charAt(i));
//     }
// }
// console.log(out);

// ----------------------------------------


//! 6. Check Whether Two Strings Are Anagrams
//! Example: Input: "listen", "silent" Output: true
//! Two strings are anagrams if they contain the same characters with the same frequency.
//* solution
// let s1='listen'
// let s2='silents'
// let flag=true
// for(let i=0; i<s1.length; i++){
//     if (s1.indexOf(s1.charAt(i))!=s1.lastIndexOf(s1.charAt(i))){
//         flag=false
//         break;
//     }
// }
// console.log(flag);

// ----------------------------------------


//! 7. Find the Longest Word in a Sentence
// Example:
// js
// Input: "I love learning JavaScript programming"
// Output: "programming"
// Return the longest word in the given sentence.
//* solution
// let s='I love learning JavaScript programming'
// sa=s.split(' ')
// console.log(sa);

// let l=''
// let i=0;
// while (i<sa.length){
//     if (sa[i].length>l.length){
//         l=sa[i]
//     }
//     i++
// }
// console.log(l);


// ----------------------------------------


// 8. Count Frequency of Each Character
// Input: "banana"
// Output:
// {
//   b: 1,
//   a: 3,
//   n: 2
// }
// Count how many times each character appears.


// ----------------------------------------


//! 9. Capitalize the First Letter of Every Word
//best solution
// let s = 'hello welcome to javascript'
// sa = s.split(' ')
// console.log(sa);

// out = ''
// for (let i = 0; i < sa.length; i++) {
//     out = out + sa[i][0].toUpperCase() + sa[i].slice(1) + ' '
// }
// console.log(out);


// OR
// let s2 = 'hello welcome to javascript'

// out = s2[0].toUpperCase()
// for (let i = 1; i < s2.length; i++) {
//     if (s2[i] == ' ') {
//         out = out + s2[i]
//         i++
//         out = out + s2[i].toUpperCase()

//     }
//     else {
//         out = out + s2[i]
//     }

// }
// console.log(out);

//OR
// let s = 'hello welcome to javascript'
// sa = s.split(' ')
// console.log(sa);

// for (let i = 0; i < sa.length; i++) {
//     sa[i] = sa[i][0].toUpperCase() + sa[i].slice(1)
// }
// console.log(sa)
// console.log(sa.toString().replaceAll(',', ' '));




//! ----------------------------------------

//! 10. Find the Most Frequent Character
// Example:
// js
// Input: "success"
// Output: "s"
//pending
// let s='success'

// for(let i=0; i<s.length; i++){
//     let c=s[i]
//     let cc=0
//     for(let j=0; j<s.length; j++)   {

//     } 
// }



// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------


// MEIDUM LEVEL QUESTIONS WITH JS  STRING METHODS


//! 1. **Reverse the Order of Words**
// Input: "I love JavaScript"
// Output: "JavaScript love I"
//* Solution
s = "I love JavaScript"
console.log(s.split(' ').reverse().join(' '))


//! 2. **Find the Longest Word in a Sentence**
// Input: "I love learning programming"
// Output: "programming"
//* solution
// s='I love programming learn'
// a=s.split(' ')
// console.log(a);
// let longest=''
// for(let i=0; i<a.length; i++){
//     if (a[i].length>longest.length){
//         longest=a[i]
//     }
// }
// console.log(longest)


//! 3. **Remove Duplicate Words**
// Input: "java is easy and java is powerful"
// Output: "java is easy and powerful"
//* solution
// let s = 'java is easy and java is powerful'
// sa = s.split(' ')
// console.log(sa);
// out=''
// for (let i = 0; i < sa.length; i++) {
//     // console.log(s.indexOf(sa[i]))
//     // console.log(s.indexOf(sa[i],s.indexOf(sa[i])+1));

//     if (s.indexOf(sa[i], s.indexOf(sa[i]) + 1) != -1) {
//         out=out+sa[i]+' '
//         // console.log('out:',out);
//         s=s.replaceAll(sa[i],'')
//         // console.log('s:',s);
//         sa=s.split(' ')
//         s=sa.join(' ')
//         // console.log(s)


//     }
//     else{
//         out=out+sa[i]+' '

//     }
// }
// console.log(out.trimEnd());


//! 4. **Find All Words Starting With a Vowel**
// Input: "Apple is not an amazing orange"
// Output: ["Apple", "is", "an", "amazing", "orange"]
//* solution
let s = 'Apple is an amazing orange'
let sa = s.split(' ')
out = []
for (let i = 0; i < s.split(' ').length; i++) {
    if ('aeiouAEIOU'.includes(sa[i][0].split())) {
        out.push(sa[i])
    }
}
console.log(out);

//! Convert a String to Title Case
// Capitalize the first letter of every word and convert the remaining letters to lowercase.
// js Input: "hELLO wORLD javascript" Output: "Hello World Javascript"
let s= "hELLO wORLD javascript"
// wl=s.split(' ')
// out=''
// for(let i=0; i<wl.length; i++){
//     w=wl[i]
//     nw=w[0].toUpperCase().concat(w.slice(1).toLowerCase())
//     out=out.concat(nw,' ')
// }
// console.log(out)



//! 6. **Find the Most Repeated Word**
// Find the word that appears most frequently in a sentence.
// Input: "apple banana apple orange banana apple"
// Output: "apple"
//* solution
s='apple banana apple orange banana apple'
a=s.split(' ')
console.log(a)
console.log(a)



//! 7. **Remove a Specific Character From a String**
// Remove all occurrences of a given character from a string.
// Input: "programming"
// Character: "g"
// Output: "prorammin"
//* solution
let s='programming'
console.log(s.replaceAll('g',''))


//! 9. **Find the Second Longest Word**
// Input: "I love JavaScript programming"
// Output: "JavaScript"
let s = "I love  programming JavaScript"
sa = s.split(' ')

let ll = 0
let lw = ''
let sl = 0
let slw = ''

for (let i = 0; i < sa.length; i++) {

    if (sa[i].length > ll) {
        sl = ll
        slw = lw
        ll = sa[i].length
        lw = sa[i]

    }
    else if (sa[i].length > sl) {
        sl = sa[i].length
        slw = sa[i]
    }

}
console.log(slw);



// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------


// REAL WORLD SCENARIO QUESTIONS interview level
//! 2. **The High-Performance Autocomplete Substring Matcher:**
// Your team is reviewing a high-traffic search bar where users type rapidly. You notice memory spikes and unnecessary allocations when validating whether a product list contains a search term. Aside from basic inclusion checks, how would you search a string while ignoring case sensitivity without creating expensive temporary lowercase copies of large catalog strings?
//* solution
let catalog=`shoes
Shampoo
Dresses
CLEAN and CLEAR
Jeans
Fruits and Vegetables
Vegetables`
let search='clear'
let search2='sh'

let a=catalog.toLowerCase().split('\n')
// console.log(a);

for(let i=0; i<a.length; i++){
    
    
    if (a[i].includes(search2.toLowerCase())) {
        console.log(a[i]);
        
    }
}