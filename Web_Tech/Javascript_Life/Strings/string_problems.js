//count the characters in  string

let data = "javaScript is Wonderful Language"
console.log('length using .length : '+data.length)

// q1. count of chars without length
// let i=0
// let count=0
// while  (data.charAt(i)!=''){
//     count+=1
//     i+=1
// }
// console.log(count)

// q2. count of chars without length using for
// let c=0
// for(let i=0; data.charAt(i); i++){
//     c+=1
// }
// console.log('count using for'+c)


// let c=0
// for(let i=0; data.charAt(i); i++){
//     if ( (data.charCodeAt(i)>=65 && data.charCodeAt(i)<=90) || (data.charCodeAt(i)>=97 && data.charCodeAt(i) <=122) ){
//         c++
//     }
// }
// console.log('count of only letters :'+c)

// q3. count of vowels

// let c=0
// for(let i=0; data.charAt(i); i++){
//     let ch=data.charAt(i)
//     switch(ch){
//         case 'a':
//         case 'e':
//         case 'i':
//         case 'o':
//         case 'u':
//         case 'A':
//         case 'E':
//         case 'I':
//         case 'O':
//         case 'U': c++
//         break;
//     }
// }
// console.log('count of only vowels :'+c)


// let co=0
// for(let i=0; i<data.length; i++){
//     let ch=data.charAt(i)
//     if ('AEIOUaeiou'.includes(ch)==true)  co++ //single line stmt
    
// }
// console.log('count of only vowels :'+co)



// let data = "javaScript is Wonderful Language"
data=data[0].toUpperCase()+data.slice(1)

console.log(data)

// console.log(data.replace(data[0],  data[0].toUpperCase()))

// console.log(data)

//q remove spaces in a string
s= '    he;llo world \tthis is js   ' //exception 
console.log(s)
console.log(s.trim(' '))
console.log(s.trim(' ').replaceAll(' ',''))

