// let a = [1, 2, 3, 4, 5]

// console.log(a)

// for (let i = 0; i < a.length; i++) {
//     console.log(a[i] * 5)
// }


// //~ using map()

// let newarr = a.map(multiply)

// function multiply(x) {
//     //console.log(x*5) // new array: [ undefined, undefined, undefined, undefined, undefined ]
//     return x * 5   // orgi ar: [ 1, 2, 3, 4, 5 ]
// }

// console.log('new array:', newarr)
// console.log('orgi ar:', a)

// //~ shorter code using anonoymoous functions and arrow functions

// var newa = a.map(function multiply(x) {
//     return x * 5
// })

// console.log(newa)

// //~ using annoymou s function

// var newa = a.map(function (x) { return x * 5 })
// console.log(newa)

// //~ using arrow functions

// var newa = a.map( x => x*5 )
// console.log(newa)

// //~ SYNTAX

// // arr.map((item,index,orgarrary)=>
// // console.log(item,index,orgarray);
// // })

// //!task cube of array items

// var na = a.map( x => x**3)
// console.log(na)


// //orr

// var na = a.map( (item, index, a) => {
//     return item**3
    
// })
// console.log(na)

// //orr


//! FILTER


// let a =[1,2,3,4,5]

// // var na = a.map( item => item%2 && item) // short circuit operator
// // console.log(na) //[ 1, 0, 3, 0, 5 ]

// // var na = a.map( item =>{
// //     if (item%2==0) return item
// // })
// // console.log(na) // [ undefined, 2, undefined, 4, undefined ]

// var na = a.filter( (item,index,org) => item%2 )
// console.log(na)

// var na = a.filter( (item,index,org) => item%2===0 )
// console.log(na)

// //! task -  length greater than 5

// names=['anya','tanyas','anil','kannaika','praya']
// var newnames = names.filter( (item,index,org)=> item.length>5 )
// console.log(newnames)

// //! task - filter the names starting with r

// names=['ramya','tanyas','rani','kannaika','praya']
// var newnames = names.filter ( (item,index,org) => item[0]==='r')
// console.log(newnames)

// //! filter out empty strings form the array

// names = names=['ramya','\n','rani','','','   ']

// var newnames = names.filter( (item,index,org) => (item))
// console.log(newnames)

// //! task - names that consist of 'a'

// names = ['ramya','\n','chintu','','','   ']
// // var newnames = names.filter( (item,index,org) => item.indexOf('a')!=-1 )
// var newnames = names.filter( (item,index,org) => item.includes('a') )

// console.log(newnames)

// //! task - filter the number whcihc consist of 5 in their value
// nums = [1,43,5,25,656,7,293]
// var newnums = nums.filter( (item,index,org) => item.toString().includes('5') )
// console.log(newnums)




//! REDUCE - single output

// let data =[1,2,3,4,5,6,7,8,9,10]
// console.log(data)

// let sum=0
// for(let i=0; i<data.length; i++){
//     sum = sum+data[i]
// }
// console.log(sum)


// let newdata = data.reduce( (acc, currv) => acc * currv, 1) // default acc value is 0
// console.log(newdata) 

// //OR

// let newdata = data.reduce( (acc,curvv) => { return acc+curvv },1)


//! Find the sum of all the even nos in the array

// let a = [1,2,3,4,5,6,7,8,9,10,11,12]

// let newa = a.filter( (item,index,org) => item%2==0 ).reduce( (acc,currv) => acc + currv)
// console.log(newa)

// task
//1. ocunt of odd numbers in the gvien array
//2. find the sum of squares of given elemnts
//3. count how many numbers are divisible by 2 and 3 both
//4. find total no of chars in all the strings of array
