
// let userinfo = {
//     name: null,
//     "is LoggedIn": true,
//     streak: 7,
//     days: 360,
//     subjects: ['js', 'html', 'python', 'sql'],
//     "status%": 'busy',

//     coding: function () {
//         console.log(name, 'is coding now');
//     },
//     resting: (name) => { console.log(name, 'is resting'); },

//     eating: function eat() {
//         return "eating.."
//     },

//     address: {
//         city: 'mysuru',
//         code: 570002,
//         wards: [101,103,201,302]
//     },
//     0:"some metadata first"
// }

// console.log(userinfo);

// //~ Defintion
// /*
// objects are a programmmatical representation of a real world entity whose properties i.e., state and behaviours are represeneted as a key - value pairs
// */


// //~ DOT NOTATION
// //~ 1. accessing using dot notation
// console.log(userinfo.name)
// // console.log(subjects) // ReferenceError: subjects is not defined
// console.log(userinfo.subjects)


// //~ accessing functions that return(log required)
// console.log(userinfo.eating()) // [Function: eat]

// //! dot notation not working on array
// let arr = [10, 20, 30]
// // console.log(arr."0")


// //~ 2. accessing function in objects (no log required)
// userinfo.resting('abc')
// userinfo.resting() //undefined is resting (considered as va?? ) //! var?

// //~ 3. accessing nested object items
// console.log(userinfo.address.code);
// console.log(userinfo.address[1]); // underfined COS what is inside address is an objects not an array

// //~ 3. accessing array tiems
// console.log(userinfo.subjects[2])

// //~ 4. accessng both neste dobject and array at the same time
// console.log(userinfo.address.wards[3]);



// ////////////////////

// //~ Accessing object propertie  using square  brackets

// //~ 1. dynamic access of data
// let key='streak'
// console.log(userinfo.key) //undefined
// console.log(userinfo[key]) //7

// //~ 2. if the key has space in it
// // console.log(userinfo."is LoggedIn") //syntax errr
// console.log(userinfo["is LoggedIn"]) //true

// //~ 3. if the key has some special car init
// // console.log(userinfo(status%)) //syntax error
// console.log(userinfo["status%"]) //busy

// //~ 4. if the key is a number
// console.log(userinfo[0]) //some metadata first //! not referring to index here if the var is an object
// console.log(userinfo["0"]) //some metadata first


//  arr = [10, 20, 30]
// console.log(arr["0"])
// console.log(arr[0])


// //! MODIFYING OBJEVT PROPERTIES - CRUD

// //~ ! CREATING
// let userData = {
//     name:'abc',
//     age:12,
//     flag:true,
//     10:"icse"
// }

// //~ READ
// console.log(userData)
// console.log(userData.age)

// //~ ADDING
// userData.school='Sophia'
// console.log(userData)

// //~ UPDATE
// userData.age=13
// console.log(userData)

// //~ DELETE
// delete userData.flag 
// console.log(userData);




// //////////////////


//! OBJECT METHODS  - method so we need to call on..?
let userData = {
    name:'abc',
    age:12,
    flag:true,
    10:"icse"
}
//~ 1. KEYS()
console.log(Object.keys(userData)) // [ '10', 'name', 'age', 'flag' ]

//~ 2. values()

console.log(Object.values(userData)) //[ 'icse', 'abc', 12, true ] //! note order ws changed

//~ 3. entries()
console.log(Object.entries(userData)) 
/* output
[
  [ '10', 'icse' ],
  [ 'name', 'abc' ],
  [ 'age', 12 ],
  [ 'flag', true ]
]

*/

//~ 4. fromEntries()

let userdata_entries= Object.entries(userData);
console.log(Object.fromEntries(userdata_entries)) // { '10': 'icse', name: 'abc', age: 12, flag: true } 