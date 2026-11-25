//! closure

// function outer(){
//     let impdata=200
//     function inner(){
//         console.log(impdata)

//     }
//     return inner
// }
// let result=outer()
// result() //200


// //! example 2
// function outerfunction() {

//     console.log("outerfunction execution started");

//     let impData = 10
//     function innerFunction() {
//         console.log("innerFunction exe started");
//         console.log("accesing outerfunction value:" + impData);
//         console.log("innerFunction exe ended");
//     }


//     console.log("outererfunction exec ended");
//     return innerFunction
// }
// let result = outerfunction()
// result()



// //! example 3

// function counter() {
//     let count=0;
//     return function(){
//         count++;
//         return count;
//     }

// }
// const increment = counter();

// console.log(increment());
// console.log(increment());
// console.log(increment());