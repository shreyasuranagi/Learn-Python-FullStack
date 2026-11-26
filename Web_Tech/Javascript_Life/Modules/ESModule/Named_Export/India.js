//! import single data password - wrong way- without exact name
// import {p} from './China.js' //SyntaxError: 
// console.log(p);

//! import single data password - correct way
// console.log(password) // 3j234j

//! importing multiple data items as object
// import {obj} from './China.js'
// console.log(obj) //{ password: '3j234j', age: 21 }
// console.log(obj.age) //12

//! importing multiple data items - separately - multiple export, multiple import statements
// import {pass} from './China.js'
// import {flag} from './China.js'
// console.log(pass) //123
// console.log(flag) //true

//! importing multiple data items - as object with destructuring - POSSIBLE
// import {pass,flag} from './China.js'
// console.log(pass) //123
// console.log(flag) //true

//! importing an object - directly WITHOUT object destructuring
// import {emp} from './China.js'
// console.log(emp)  //{ name: 'ramu', age: 21 }
// console.log(emp.name); //21

//! importing an object - WITH object destructuring - NOT POSSIBLE
// import {name} from './China.js' //Syntax error



// ----------------------------------------
// ----------------------------------------
// ----------------------------------------



//! importing again and again - Syntax Error
// import {password,age} from './China.js' //SyntaxError: Identifier 'password' has already been declared
// console.log(password,age)

//! importing non exisitng import
// import {name} from './China.js' // SyntaxError: The requested module './China.js' does not provide an export named 'name'
// console.log(name)

