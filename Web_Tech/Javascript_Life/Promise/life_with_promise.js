
//~ CREATING A PROMIS - BACKEND JOB

//! creating a promise automatically calls the executor function
// let myPromise = new Promise( (resolve,reject) => {
//     console.log('I am inside executor function'); //I am inside executor function 
// })


//! without storing in variable calling resolve - no effect - needs to be stored
// let myPromise = new Promise( (resolve,reject) => {
//     console.log('I am inside executor function'); 
//     resolve('hi')
// })
// //out - I am inside executor function 


//! resolve- success state without argument
// let myPromise = new Promise( (resolve,reject) => {
//     resolve() //nothing
// })
// console.log(myPromise);
// //out- Promise { undefined }


// //! resolve- success state with argument
// let myPromise = new Promise( (resolve,reject) => {
//     resolve('SUCCESS: data received') //nothing
// })
// console.log(myPromise);
// //out - Promise { 'SUCCESS: data received' }


// //! reject- failed state with argument
// let myPromise = new Promise( (resolve,reject) => {
//     reject('FAIL: data NOT received') //nothing
// })
// console.log(myPromise);
// out - 
// Promise { <rejected> 'FAIL: data NOT received' }
// node:internal/process/promises:392
//       new UnhandledPromiseRejection(reason);
// UnhandledPromiseRejection:


//! ERROR situation - 

// ----------------------------------------


//~ HANDLING OF PROMISE - FRONTEND JOB - TRADITIONAL WAY

//! Handling promises -TRADITIONAL WAY - then and catch

//! then
// let myPromise = new Promise( (resolve,reject) =>{
//     console.log('I am in executor');
    
//     resolve('SUCESS')
//     reject('FAIL')
// });
// myPromise.then( (data) => {
//     console.log(data);
    
// });
// out - 
// I am in executor
// SUCESS


//! CATCH
// let myPromise = new Promise( (resolve,reject) =>{
//     console.log('I am in executor');
//     reject('FAIL')
// });
// myPromise.catch( (err) => {
//     console.log(err);  
// });
//out -
// I am in executor
// FAIL



//! BOTH then and catch - NO USE
// let myPromise = new Promise( (resolve,reject) =>{
//     console.log('I am in executor');
    
//     // reject('FAIL')

//     resolve('SUCESS')
// });
// myPromise.then( (data) => {
//     console.log(data);  
// }).catch( (err) => {
//     console.log(err);
    
// })
