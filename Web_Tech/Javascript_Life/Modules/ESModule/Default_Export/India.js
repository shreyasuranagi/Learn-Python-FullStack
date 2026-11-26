//! single itme export
// import toys from './China.js'

// console.log(toys) // Electric cars

//! function import

// import add from './China.js'
// add(2,3) //5


//! importing from multiple export statements - NOT possibel

// import toys, add from './China.js'

// console.log(toys)


//! importing multiple items from an object - using inside of import -destructuring is not possible

// import {toys,add} from './China.js'
// console.log(toys) //  The requested module './China.js' does not provide an export named 'add'


//! import using a signle object and THEN destructuring it -

// import object from './China.js'
// console.log(object) // { toys: 'Electric cars', add: [Function: add] }
// console.log(object.toys) // Electric cars
// console.log(object.add) //[Function: add]
// object.add(1,2)


// //OR
// let {toys,add}=object 
// console.log(toys); //Electric cars
// console.log(add); // [Function: add]
// add(10,20)


//! importing object

// import object from './China.js'

// console.log(object)
// console.log(object.name);

// let {name,age} = object 
// console.log(name);
// console.log(age);

// let {name:n, age:a} = object 
// console.log(n);
// console.log(a);





