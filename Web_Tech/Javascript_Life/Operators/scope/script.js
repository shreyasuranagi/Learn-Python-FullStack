var a = 10
let b = 20
const c = 30

console.log(b) //20
console.log(a) //10

{
    console.log(a) //10
    var a = 20
    console.log(a) //20
    let b = "hii"
    console.log(b) //hii

}

console.log(a) //10
console.log(b) //20



//
// console.log("lets learn scopes")

// var a =" a is var global"
// let b ="b is let script"
// const c="c is const script "

// {

// var a = "a is var global inside"
// let b= "b is let block inside"
// console.log(b)
// const c="c is const block inside"
// console.log(c)

// }



// console.log(a)
// var a =10
// let b;
// console.log(b)
// const b=20;
// console.log(b)