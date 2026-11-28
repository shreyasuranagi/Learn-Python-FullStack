
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




// ----------------------------------------
// ----------------------------------------
// ----------------------------------------



//~ MODERN APPROACH 

// let myPromise = new Promise(  (resolve, reject) => {
//     console.log('i am inside executor function');
//     // resolve('SUCESS: Data received');
//     reject('FAIL: data NOT received')

// })



// async function handleMyPromise(){


//     console.log(myPromise);

// }



//! MODERn - async and await - success /resolve

// async function handleMyPromise(){
//     let result = await myPromise
//     console.log(result);
// }
// handleMyPromise()
//out-
// i am inside executor function
// SUCESS: Data received



//! modern approach - async and await  - rejected / reject() - without try and catch()

// async function handleMyPromise(){

//     let result = await myPromise
//     console.log(result);
// }
// handleMyPromise()
//i am inside executor function
// node:internal/process/promises:392
//       new UnhandledPromiseRejection(reason);



// //! modern approach - async and await  - rejected / reject() - with try and catch()

// async function handleMyPromise(){
//     try{
//         let result = await myPromise
//     console.log(result);
//     }catch(err){
//         console.log(err);

//     }

// }
// handleMyPromise()

//! create a promise that with data bool true- emp logged succes, else thumb=true

// let thumb = false
// let p = new Promise((resolve, reject) => {
//     if (thumb == true) {
//         resolve('Employee logged in Successfully')
//     }
//     else {
//         reject('Employee NOT logged in!!')
//     }
// })

// async function handleLogin() {
//     try {
//         let log_status = await p
//         // console.log(log_status); // wont be executed if reject is called, it goes to catch(err)
//     }
//     catch (err) {
//         console.log(err); 
//     }
// }
// handleLogin()

// output-
// true-> Employee logged in Successfully
// false -> Employee NOT logged in!!

//explanation-

// 1. thumb is scanned and it is an async operation - we cant predict time it is completed - depneds on human and the operation performing the scanning

// 2. so the result of this operation can be either true-scanned succesffuly correct person or false- scanned wrongly wrong person

// 3. and this result can come at any time , so we have to wait for the result - await keyoword and amking the handling function asynchronous - async keyword

// 4. if the async operation gives true, that means i need to call resolve to put my promise/result in fulfilled state 

// 5. if the async operation gives false, that means i need to call reject to put it into rejected state 

// 6. now the result of the promise - result val / error - is stored 

// 7. handleLogin will wait for the result of the promise (val/error) and logs it



//!CAFE - tradidional approach then and catch

function orderfood() {

    //what if we did this and then returned new promise?
    // setTimeout(() => {
    //     console.log('your fav food is ordered!!');
    // }, 2000)


    return new Promise((resolve) => {
        setTimeout(() => {
            console.log('your fav food is ordered!!');
            resolve('--ordering done successfully--')
        }, 2000)
        
    })
}


function preparefood() {

    return new Promise((resolve) => {
        setTimeout(() => {
            console.log('done preparng the food!!');
             resolve()
        }, 5000) 
    })
}


function payment() {

    return new Promise((resolve) => {
        setTimeout(() => {
            console.log('payment is dont');
            resolve()
        }, 2000);
        
    })
}


function takeaway() {
    setTimeout(() => {
        console.log('ready for takeaway!');
        resolve()
    }, 2000)

}

//~ traditional appraoch
orderfood().then(() => { return preparefood() }).then(() => { return takeaway() }).then(() => { return payment; console.log('enjoy oyour food!') });


//! callback hell

// orderfood(() => {
//     preparefood(() => {
//         payment(() => {
//             takeaway(() => {
//                 console.log('Enjoy your food!');
//             });
//         });
//     });
// });


// ----------------------------------------
// ----------------------------------------
// ----------------------------------------

//~ MODERN APPROACH

// function orderfood() {

//     return new Promise((resolve) => {
//         setTimeout(() => {
//             console.log('your fav food is ordered!!');
//             resolve()
//         }, 2000)
//         // resolve('--ordering done successfully--')?
//     })
// }


// function preparefood() {

//     return new Promise((resolve) => {

//         setTimeout(() => {
//             console.log('done preparng the food!!');
//             resolve()
//         }, 5000)
        
//     })


// }


// function payment() {

//     return new Promise((resolve) => {
//         setTimeout(() => {
//             console.log('payment is dont');
//             resolve()
//         }, 2000);
//         // resolve()
//     })
// }


// function takeaway() {
//     return new Promise((resolve) => {
//         setTimeout(() => {
//             console.log('takeaway is called');
//             resolve()
//         }, 2000);
//         // resolve()
//     })

// }

// async function handledata() {
//     await orderfood()
//     await preparefood()
//     await takeaway()
//     await payment()
//     console.log('enjoy food');
// }
// handledata()