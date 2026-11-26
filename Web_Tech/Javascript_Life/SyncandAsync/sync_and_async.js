//! SYnchronous
// console.log('starting execution');

// console.log('mid of execution');

// console.log('end of execution');

// starting execution
// mid of execution
// end of execution

//! also synchronous

// console.log('starting execution');

// for (let i = 0; i < 12345; i++) { console.log('loading...') } // takes up execution time in call stack

// console.log('important data here');

// console.log('end of execution');


//! this is still synchronous -

// console.log('starting execution')

// function handlingData() {
//     for(let i=0; i<1234534523; i++){
        
        

//     }
//     console.log('done dealing with data');
    
// }
// handlingData() // sync funciton makes the following function wait
// console.log('imp data');

// console.log('ending execution');
// console.log('done with program');

//! ASYNCHRONOUS 
// ! async -?

console.log('starting execution')

function handlingData(n) {
    for(let i=0; i<102; i++){

    }
    console.log(n);
    console.log('done dealing with data');
}
setTimeout(handlingData(1), 0.5)
setTimeout(handlingData(2),0.4)

console.log('ending execution');
console.log('done with program');


//! setInterval()  -?

// console.log('starting execution')

// function handlingData(n) {
//     for(let i=0; i<1234534523; i++){

//     }
//     console.log(n);
    
//     console.log('done dealing with data');
// }
// setInterval(handlingData, 0.5)
// // setInterval(handlingData, 0.4)

// console.log('ending execution');
// console.log('done with program');

//! clearTimeout()

// console.log('starting execution')

// function handlingData(n) {
//     for(let i=0; i<1234534523; i++){

//     }
//     console.log(n);
    
//     console.log('done dealing with data');
    
// }
// clearTimeout(handlingData)
// setTimeout(handlingData, 5)

// console.log('ending execution');
// console.log('done with program');

//! clearInterval()
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
// let interval= setInterval( () => { console.log('program...')} , 800)

// setTimeout( ()=> { clearInterval(interval)}, 5000 )

// console.log('Dealing with imp data');


