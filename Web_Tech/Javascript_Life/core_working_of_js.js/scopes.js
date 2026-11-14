// global scope
// here data is global scope

// console.log(data);
// function print(){
//     let name='rani'
//     console.log(data);
//     console.log(name);
// }
// var data='somu' // global scope
// console.log(data) 
// print()


//~ local scope

// console.log(data);
// function print(){
//     console.log((data));

// }
// print()
// console.log(name); # ReferenceError: name is not defined
// var data='somu'
// console.log(data)



//~ example of function scope

// let x=10
// function print(){
//     let x =20
//     console.log(x) //20
// }
// print()
// console.log(x) //10


//~ example of global getting changed in function when accessed without declaration cos declaration creates the var/data in creation phase

// let x = 10
// function print() {
//     x = 20
//     console.log(x) //20
// }
// print()
// console.log(x) //20



// ----------------------------------------
//! whats going on ehre
// it works as global only, weakly typed language

// x = 10
// function print() {
//     x = 20
//     console.log(x) //20
// }
// print()
// console.log(x) //20