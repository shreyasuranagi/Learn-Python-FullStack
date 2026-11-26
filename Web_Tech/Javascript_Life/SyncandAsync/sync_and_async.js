//~ synchronous
//! SYnchronous
// console.log('starting execution');

// console.log('mid of execution');

// console.log('end of execution');

// output-
// starting execution
// mid of execution
// end of execution

//! also synchronous

// console.log('starting execution');
// for (let i = 0; i < 12345; i++) { console.log('loading...') } // takes up execution time in call stack
// console.log('important data here');
// console.log('end of execution');


//ooutput-
// start execution
// loading... 
// loading...
// loading... ...
// ....(long time)
// important data here
// end of execution


//! this is still synchronous -

// console.log('starting execution')
// function handlingData() {
//     for(let i=0; i<1234534523; i++) {}
//     console.log('done dealing with data');
// }
// handlingData()   // sync funciton makes the following function wait
// console.log('imp data');
// console.log('ending execution');
// console.log('done with program');

// output -
// start execution
// (...long wwait time)
// done dealing with Data 
// imp Data 
// ending execution
// done with program 

//~ asynchronous
//~ ----------------------------------------

//! ASYNCHRONOUS 
// ! async - error - worng way to call callbackfunction that have parameters

// console.log('starting execution')
// function handlingData(n) {
//     for(let i=0; i<102; i++){

//     }
//     console.log(n);
//     console.log('done dealing with data');
// }

// setTimeout(handlingData(1), 0.5) //*TypeError [ERR_INVALID_ARG_TYPE]: The "callback" argument must be of type function. Received undefined
// setTimeout(handlingData(2),0.4)
// console.log('ending execution');
// console.log('done with program');



// ! async - callback function s that have PARAMETERS - use anonmoyus or arrow functions
// console.log('starting execution')
// function handlingData(n) {
//     for(let i=0; i<1029876543; i++){

//     }
//     console.log(n);
//     console.log('done dealing with data');
// }

// setTimeout(() => handlingData(1), 0.7) 
// setTimeout(function(){ handlingData(2)},0.4)
// console.log('ending execution');
// console.log('done with program');

//* output-
// starting execution
// ending execution
// done with program
// 1
// done dealing with data
// 2
// done dealing with data



// console.log('starting execution')
// function handlingData(n) {
//     for(let i=0; i<1029876543; i++){

//     }
//     console.log(n);
//     console.log('done dealing with data');
// }

// setTimeout(() => handlingData(1), 5) 
// setTimeout(function(){ handlingData(2)},2)
// console.log('ending execution');
// console.log('done with program');


//* output-
// starting execution
// ending execution
// done with program
// 2
// done dealing with data
// 1
// done dealing with data



// ! async - callback function WITHOUT parameters
// console.log('starting execution')
// function handlingData() {
//     for(let i=0; i<102; i++){

//     }
//     console.log('done dealing with data');
// }

// setTimeout(handlingData, 0)
// setTimeout(handlingData, 1)
// console.log('ending execution');
// console.log('done with program');


//* output-
// starting execution
// ending execution
// done with program
// done dealing with data
// done dealing with data



// ----------------------------------------


//! clearTimeout() - 1 - worng method/syntax
// console.log('starting execution')
// function handlingData() {
//     for(let i=0; i<1234534523; i++){
//     }
//     console.log('done dealing with data');  
// }
// clearTimeout(handlingData)
// setTimeout(handlingData, 5000)
// console.log('ending execution');
// console.log('done with program');

//* output -
// starting execution
// ending execution
// done with program 
// --(waits for about a second---for loop only+5s)
// done dealing with data



// //! clearTimeout() - correct method
// 1.starting execution logs synchronously.

// 2.setTimeout(handlingData, 5000) schedules the timer and returns a timer ID, stored in timerId.

// 3.clearTimeout(timerId) runs immediately on the next synchronous line, canceling that timer before its 5000 ms delay finishes.

// 4.ending execution and done with program log synchronously, and the program finishes with no pending timer callback left to run.


// console.log('starting execution');
// // clearTimeout(timerId); // cannot be placed here, ReferenceError
// function handlingData() {
//   for (let i = 0; i < 1234534523; i++) {}
//   console.log('done dealing with data');
// }

// const timerId = setTimeout(handlingData, 5000);
// clearTimeout(timerId); // Cancels this specific scheduled timer immediately and its callback function is also not called
// console.log('ending execution');
// // clearTimeout(timerId); // can be placedanywehre after setimeout, cancels after .log('end exec')
// console.log('done with program');

//* output-
// starting execution
// ending execution
// done with program



//! without cleartimeout()
// clearTimeout(handlingData) // it matters where it is written in the program, put it before setTimeout
// console.log('starting execution')
// function handlingData() {
//     for(let i=0; i<1234534523; i++){
//     }
//     console.log('done dealing with data');  
// }
// // let tid=setTimeout(handlingData,5000)
// setTimeout(handlingData,5000)
// // clearTimeout(tid)
// console.log('ending execution');
// console.log('done with program');


//* output -
// starting execution
// ending execution
// done with program
// done dealing with data



// ----------------------------------------



//! setInterval()  -?
// console.log('starting execution')
// function handlingData() {
//     for(let i=0; i<12; i++){
//     }  
//     console.log('done dealing with data');
// }
// setInterval(handlingData, 3000)
// console.log('ending execution');
// console.log('done with program');

//* output-
// starting execution
// ending execution
// done with program
// done dealing with data
// done dealing with data
// done dealing with data
// ....





//! clearInterval() - class way
//!wrong
// console.log('starting execution')
// function handlingData() {
//     for(let i=0; i<102; i++){
//     }  
//     console.log('done dealing with data');
// }
// setInterval(handlingData,6000)
// setTimeout( ()=> clearInterval(handlingData),2000)
// console.log('ending execution');
// console.log('done with program');


//////////////////

//! setTimeout - corrected class way
// let interval= setInterval( () => { console.log('program...')} , 800)

// setTimeout( ()=> { clearInterval(interval)}, 5000 )

// console.log('Dealing with imp data');



//! clearInterval()  - correct way
// console.log('starting execution')
// function handlingData() {
//     for(let i=0; i<102; i++){
//     }  
//     console.log('done dealing with data');
// }
// let tid = setInterval(handlingData,3000)
// clearInterval(tid)
// console.log('ending execution');
// console.log('done with program');

// starting execution
// ending execution
// done with program


//~ USE CASE VERSIONS

//~ clearInterval() - lets say we show ads every 6s and we want to stop showing ads
console.log('starting execution')
function handlingData() {
    for(let i=0; i<102; i++){
    }  
    console.log('AD: buy santoor soap!');
}
setInterval(handlingData,6000)
setTimeout( ()=> clearInterval(handlingData),4000)
console.log('ending execution');
console.log('done with program');