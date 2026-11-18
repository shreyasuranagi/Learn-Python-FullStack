//! global scope
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


//~ example -  name is not defined

console.log(data); //undefined
function print(){
    console.log((data));

}
print() // undefined
console.log(name); // ReferenceError: name is not defined
var data='somu'
console.log(data)



//~ example of function scope

// let x=10
// function print(){
//     let x =20
//     console.log(x) //20
// }
// print()
// console.log(x) //10


//~ example of global getting changed in function when accessed without declaration cos declaration creates the var/data in creation phase

let x = 10
function print() {
     x = 20
    console.log(x) //20
}
print()
console.log(x) //20



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

//! BLOCK SCOPE

//~ let example

let flag=true
if (flag) {
    var data=100
    console.log('in block:',data) //100
}
else{
    var data=100
    console.log('in block:',data)
}
console.log(data) //100

//~ modified

let flag=true
if (flag) {
    let data=100
    console.log('in block:',data) //100
}
else{
    var data=100
    console.log('in block:',data)
}
console.log(data) // undefined

//!

let flag=true
if (flag) {
    let data=100
    console.log('in block:',data) //100
}
else{
    let data=100
    console.log('in block:',data)
}
console.log(data) // data is not defined

//~ scope chaining

let d1='somu'
function outer(){
    let d2='rani'
    function inner(){
        let d3='raja'
        console.log(d1);
        console.log(d2); //scope chaining
        console.log(d3);
        
    }
    inner()
    console.log(d2)
    console.log(d3) // d3 not defined, scope concept here
}
outer()

// dif in lexical and scope chaning and scopes