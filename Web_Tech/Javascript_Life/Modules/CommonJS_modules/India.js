
//~ accessing data in CHina without improting in India- ReferncError
// console.log(toys) #ReferenceError: toys is not defined

//~ importing data in India without export in china - {}
// let t=require('./china')
// console.log(t) // {}

//~ export data to China without importing in India - 

// //! with single data export in china and import in India
// let toy = require('./china')
// console.log(toy) //bags


//! with multiple exports in both , improting functions
// let a=require('./china')
// a(10,2) //12


// //! importing multiple items as objects - data, functions
// let items = require('./china')
// console.log(items) // { add: [Function: add], toys: 'bags' }

// console.log(items.toys); //bags
// items.add(10,30) //40


//! improting multiple objects - using dot notation - not effiecient

// let infos = require('./china')
// console.log(infos.userInfo) // { name: 'maya', userid: 'u123', status: true }
// console.log(infos.empInfo) // { name: 'kiran', eid: 'e123', age: 22 }
// console.log(infos.empInfo.name) // kiran
// console.log(infos.userInfo.userid); // u123


//! importing objects by destructuring objects - with same KEY name!

// let {name,userid,status} = require('./china')
// console.log(name,userid,status); // maya u123 true
