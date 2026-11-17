// var data='somu' // decclaratin and initialization on the same line

// var data; // declaration
// data ='somu' // initialization

// ----------------------------------------
// var data
// console.log(data) //undefined cos acessing  variable before it is init always-> undefined(definition of undefined)
// ----------------------------------------

// //~ exmaple 1
// console.log(data); //undefined cos acessing  variable before it is init always-> undefined
// var data='somu'
// console.log(data); // somu

//* internal
// var data ;// = undefined //(by default)
// console.log(data); 
// data='somu'
// console.log(data); 

// ----------------------------------------
// ----------------------------------------
 
//~ example 2

// console.log(data); // ReferenceError: data is not defined (memory has not even been allocated)

// BUTTT-
// console.log(data); //ReferenceError: Cannot access 'data' before initialization 
        //  it means data was alllocated memory('defined') but it cannot be accessed(because of hoisting and creation phase)
// let data='somu'
// console.log(data);  // ownt be executed

//* internal
// let data //-> // actully let data='undefined'
// console.log(data);  //TDZ - data is not accesisble here
// data='somu'
// console.log(data);  //somu


// ----------------------------------------
// ----------------------------------------

//~ example 3

// console.log(data) // undefined
// function print(){
//     console.log('print')
// }
// var data = 'somu'
// console.log(data); // somu
// print() // print

// ----------------------------------------
// ----------------------------------------

//~ example 4

// console.log(data) //error
//     let name='rani'
//     console.log(data);
//     console.log(name);
// let data = 'somu'
// console.log(data); 
// print()

// ----------------------------------------
// ----------------------------------------

//~ example 5

// print() 
//                 // op- 
//                 // undefined
//                 // rani
// console.log(data) //undefined
// function print(){
//     let name='rani'
//     console.log(data);
//     console.log(name)
// }
// var data = 'somu'
// console.log(data); //somu


// ----------------------------------------
// ----------------------------------------

//~ example 6

console.log(data)
let print = function printFunction(){
        let name='rani'
        console.log(data)
        console.log(name)
}
var data='somu'
console.log(data)
print() 

// //op
// undefined
// somu 
// somu 
// rani

//~ example 8
// console.log(data)
// var print = function printFunction(){
//         let name='rani'
//         console.log(data)
//         console.log(name)
// }
// var data='somu'
// console.log(data)
// print() 

// //op
// undefined 
// somu 
// somu 
// rani

//~ example 9
// console.log(data)
// print()  //! ReferenceError: Cannot access 'print' before initialization
// let print = function printFunction(){
//         let name='rani'
//         console.log(data)
//         console.log(name)
// }
// var data='somu'
// console.log(data)


//~ example 10
// console.log(data)
// print()  //! TypeError: print is not a function
// var print = function printFunction(){
//         let name='rani'
//         console.log(data)
//         console.log(name)
// }
// var data='somu'
// console.log(data)
