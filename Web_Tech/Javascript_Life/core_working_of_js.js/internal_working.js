// var data='somu' // decclaratin and initialization on the same line

// var data; // declaration
// data ='somu' // initialization

// ----------------------------------------
// var data
// console.log(data) //undefined cos acessing  variable before it is init always-> undefined
// ----------------------------------------

// //~ exmaple 1
// console.log(data); ////undefined cos acessing  variable before it is init always-> undefined
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



// //BUTTT-
// console.log(data); //ReferenceError: Cannot access 'data' before initialization 
// // it means data was alllocated memory('defined') but it cannot be accessed
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

// console.log(data)
// function print(){
//     console.log('print')
// }
// var data = 'somu'
// console.log(data);
// print()

// ----------------------------------------
// ----------------------------------------

//~ example 4

console.log(data)
function print(){
    let name='rani'
    console.log(data);
    console.log(name)
}
var data = 'somu'
console.log(data);
print()