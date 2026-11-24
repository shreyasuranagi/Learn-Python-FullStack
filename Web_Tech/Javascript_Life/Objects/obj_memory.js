// // console.log(userData)cls

// let userData={
//     name:'abc',
//     age:32,
//     status:false,
//     working:function() { console.log('working currently'); }
// }

// console.log(userData)
// console.log(userData.name)
// console.log(userData.length)

// //! pass by value
// let data1=100
// let data2=data1
// console.log(data1) //100
// console.log(data2); //100
// data1=200
// console.log(data1) //200
// console.log(data2); //100
// data2=300
// console.log(data1) //200
// console.log(data2) //300 


// //! pass by referncce






// //! function executon in memory block
// function add(a,b,c){
//     console.log(a+b)
// }
// add(10,20)
// console.log(add.name); //add
// console.log(add.length) //3



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

function outerfunction() {

    console.log("outerfunction execution started");

    let impData = 10
    function innerFunction() {
        console.log("innerFunction exe started");
        console.log("accesing outerfunction value:" + impData);
        console.log("innerFunction exe ended");
    }


    console.log("outererfunction exec ended");
    return innerFunction
}
let result = outerfunction()
result()
