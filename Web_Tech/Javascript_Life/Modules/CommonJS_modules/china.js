//! single data is exported
// let toys='bags'
// module.exports = toys


//! exporting funcitons
// function add(a,b){
//     console.log(a+b)
// }
// module.exports = add // onyl this is considdered


//! exporting multiple in the form of an object
// module.exports = {add, toys}


//! exporting multiple objects
// let userInfo={
//     name:'maya',
//     userid:'u123',
//     status:true
// }

// let empInfo ={
//     name:'kiran',
//     eid: 'e123',
//     age:22
// }

// module.exports = { userInfo, empInfo }

//! exporting single objects - destructuring
// let userInfo={
//     name:'maya',
//     userid:'u123',
//     status:true
// }
// module.exports = userInfo


//! exporting multiple objects - destructuring -??
let userInfo={
    name:'maya',
    userid:'u123',
    status:true
}
module.exports = {userInfo, empInfo}