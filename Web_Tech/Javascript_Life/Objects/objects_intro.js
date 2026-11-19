
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

// // //~ Defintion
// // /*
// // objects are a programmmatical representation of a real world entity whose properties i.e., state and behaviours are represeneted as a key - value pairs
// // */


// // //~ DOT NOTATION
// // //~ 1. accessing using dot notation
// // console.log(userinfo.name)
// // // console.log(subjects) // ReferenceError: subjects is not defined
// // console.log(userinfo.subjects)


// // //~ accessing functions that return(log required)
// // console.log(userinfo.eating()) // [Function: eat]

// // //! dot notation not working on array
// // let arr = [10, 20, 30]
// // // console.log(arr."0")


// // //~ 2. accessing function in objects (no log required)
// // userinfo.resting('abc')
// // userinfo.resting() //undefined is resting (considered as va?? ) //! var?

// // //~ 3. accessing nested object items
// // console.log(userinfo.address.code);
// // console.log(userinfo.address[1]); // underfined COS what is inside address is an objects not an array

// // //~ 3. accessing array tiems
// // console.log(userinfo.subjects[2])

// // //~ 4. accessng both neste dobject and array at the same time
// // console.log(userinfo.address.wards[3]);



// // ////////////////////

// // //~ Accessing object propertie  using square  brackets

// // //~ 1. dynamic access of data
// // let key='streak'
// // console.log(userinfo.key) //undefined
// // console.log(userinfo[key]) //7

// // //~ 2. if the key has space in it
// // // console.log(userinfo."is LoggedIn") //syntax errr
// // console.log(userinfo["is LoggedIn"]) //true

// // //~ 3. if the key has some special car init
// // // console.log(userinfo(status%)) //syntax error
// // console.log(userinfo["status%"]) //busy

// // //~ 4. if the key is a number
// // console.log(userinfo[0]) //some metadata first //! not referring to index here if the var is an object
// // console.log(userinfo["0"]) //some metadata first


// //  arr = [10, 20, 30]
// // console.log(arr["0"])
// // console.log(arr[0])


// // //! MODIFYING OBJEVT PROPERTIES - CRUD

// // //~ ! CREATING
// // let userData = {
// //     name:'abc',
// //     age:12,
// //     flag:true,
// //     10:"icse"
// // }

// // //~ READ
// // console.log(userData)
// // console.log(userData.age)

// // //~ ADDING
// // userData.school='Sophia'
// // console.log(userData)

// // //~ UPDATE
// // userData.age=13
// // console.log(userData)

// // //~ DELETE
// // delete userData.flag 
// // console.log(userData);




// // //////////////////


// //! OBJECT METHODS  - method so we need to call on..?
// let userData = {
//     name:'abc',
//     age:12,
//     flag:true,
//     10:"icse"
// }
// //~ 1. KEYS()
// console.log(Object.keys(userData)) // [ '10', 'name', 'age', 'flag' ]
// console.log(Object.keys(userinfo))
// //~ 2. values()

// console.log(Object.values(userData)) //[ 'icse', 'abc', 12, true ] //! note order ws changed
// console.log(Object.values(userinfo))
// //~ 3. entries()
// console.log(Object.entries(userData)) 
// console.log(Object.entries(userinfo))
// /* output
// [
//   [ '10', 'icse' ],
//   [ 'name', 'abc' ],
//   [ 'age', 12 ],
//   [ 'flag', true ]
// ]

// */

// //~ 4. fromEntries()

// let userdata_entries= Object.entries(userData);
// console.log(Object.fromEntries(userdata_entries)) // { '10': 'icse', name: 'abc', age: 12, flag: true } 

//~ 5. Object.assign()
// let user_info ={
//     name:'abc'
// }
// let personal_info={
//     age:21,
//     flag:true
// }
// let FinalData = Object.assign({}, personal_info, user_info)
// console.log(FinalData) // { age: 21, flag: true, name: 'abc' }
// console.log(user_info) // { name: 'abc' }
// console.log(personal_info) // { age: 21, flag: true }

// let user_info_complete={
//     isloggedin: true
// }

// let final2 = Object.assign(user_info_complete,user_info,personal_info)
// console.log(FinalData) // { age: 21, flag: true, name: 'abc' }
// console.log(user_info_complete)

// let f2=user_info_complete
// console.log(f2)
// console.log(f2==user_info_complete) //! try later


//~ 6. Object.seal()
// let empInfo ={
//     full_name: 'dr jay shankar',
//     age:30,
//     pan_no: 'P2345'
// }

// console.log('original data before seal:',empInfo)

// Object.seal(empInfo) // -> returns object itself after sealing
// console.log('After sealing the data:',empInfo)

// delete empInfo.pan_no //not possibel bcos of seal
// console.log('Deleting after sealing no change:',empInfo)
// empInfo.reff='rani' //not possible bcos of seal
// console.log('Adding key after seal no change:',empInfo) 
// empInfo.age=31 // modification possible in seal
// console.log('Modifying key after seal yes change:',empInfo) 



//~ 7. OBject.isSealed()
// let userinfo={
//     name:'abc',
//     age:22,
//     credit_card:2345678765432
// }
// Object.seal(userinfo) 
// console.log(Object.seal(userinfo))
// if (Object.isSealed(userinfo)){
//     console.log('data is safe and secure')
// }
// else{
//     console.log('data NOT secure!!!')
// }


//~ 8. Object.freeze()
// let userinfo={
//     name:'abc',
//     age:22,
//     credit_card:2345678765432
// }

// Object.freeze(userinfo)

// delete userinfo.name //no change
// console.log(userinfo)
// userinfo.role='admin' //no change
// console.log(userinfo)
// userinfo.age += 1 //no change
// console.log(userinfo) 

// //doubt- security? what if they copy, can they, how mcuh of ourdat ais permanetn


//~ 9. Object.isFrozen(objref)
// let userinfo={
//     name:'abc',
//     age:22,
//     credit_card:2345678765432
// }
// Object.freeze(userinfo)
// if (Object.isFrozen(userinfo)){
//     console.log('FUlly restricted no crud possible')
// }
// else{
//     console.log('object not frozen')
// }

// // let copy=userinfo //! copy is aslo frozen
// // let copy=Object.assign({},userinfo) //! copy is aslo frozen

// Object.freeze(copy) 
// if (Object.isFrozen(userinfo)){
//     console.log('FUlly restricted no crud possible')
// }
// else{
//     console.log('object not frozen')
// }


//~ 10. Object.hasOwn()

// let userinfo={
//     name:'abc',
//     age:22,
//     credit_card:2345678765432
// }
// console.log(Object.hasOwn(userinfo,"name")) //true
// console.log(Object.hasOwn(userinfo,'hello')) //false


//~ 11. Object.is(value,object)
// let userinfo={
//     name:'abc',
//     age:22,
//     credit_card:2345678765432
// }
// console.log(Object.is(2,3)) //false
// console.log(Object.is(2,2)) //true
// console.log(Object.is(userinfo.age,22)) //true 
// console.log(Object.is('abc',userinfo.name)) //true
// console.log(Object.is(userinfo,{name:'xyz',age:22})) //false
// let rani={name:'xyz',age:22}
// console.log(Object.is(userinfo,rani))//false
// console.log(Object.is(userinfo,{name:'abc',age:22,credit_card:2345678765432})) //false //! NOTEEE here

// let copy=Object.assign({},userinfo)
// console.log(Object.is(userinfo,{name:'xyz',age:22})) //false //! NOTEEE here - .assign creates obj in new memory prolly

// let copy2=Object.assign(userinfo)
// console.log(Object.is(copy2,userinfo)) //true  //! NOTEEE here - using = operators holds same ref proll in memory