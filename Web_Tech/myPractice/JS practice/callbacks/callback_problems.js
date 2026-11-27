
// function orderfood(){
//     console.log('ordering food');
// }
// function preparefood(){
//     console.log('preparing food');
// }
// function payment(){
//     console.log('pay for food');   
// }

// orderfood()
// preparefood()
// payment()
//all called immediately



// function orderfood(){
//     setTimeout( ()=>{} , 2000)
//     console.log('ordering food');
// }
// function preparefood(){
//     setTimeout( ()=>{} , 2000)
//     console.log('preparing food');
// }
// function payment(){
//     setTimeout( ()=>{} , 2000)
//     console.log('pay for food');   
// }

// orderfood()
// preparefood()
// payment()
//all called immediately




// function orderfood(){
//     setTimeout( ()=>{} , 2000)
//     console.log('ordering food');
//     preparefood() //~hardcoding is a bad idea, what if i want to call sms() instead of this rifht fater order() at some place? better to use callabck here and based on waht funciton was pased call either sms() or prpaefood()
//     payment()
// }
// function preparefood(){
//     setTimeout( ()=>{} , 2000)
//     console.log('preparing food');
// }
// function payment(){
//     setTimeout( ()=>{} , 2000)
//     console.log('pay for food');   
// }

// orderfood()
//all called immediately






//! 1. Welcome Message (Easy)
// let p= ()=>{
//     console.log("How's your day?");
    
// }

// function greet(name){
//     console.log('Welcome '+name);
//     // prompt()
//     p() //works
// }

// greet('Shreya')
// // p() //workd



function orderfood(){
    console.log('ordering');
    preparefood()
    
}
function  preparefood(){
    console.log(['preparing']);
    
}

// vs

function orderfood(callback){
    console.log('ordering');
    callback()
}
orderfood( ()=>{console.log('preparing'); })

// immeidate call problem still exists? hardcoding is  solved, state problem might still exist , this is stil nnot  anested callback hell probelmm right