//! Array Destructing - process of extracting individual items or elements from an array withotu slicing by the use of aliases/ variable names to the elements

let a=[10,20,30,40,50]

//~ normal way of accessing array elemnts using indexing
console.log(a[0])
console.log(a[1])


for(let i=0; i<a.length; i++){
    console.log(a[i])
}

//~ accessing using array destructing / aliases
let [ten,twenty,thirty,forty,fifty] = a 

console.log(thirty)
console.log(fifty)

let colors=['green','red','rosa','blue']
//let [g,r,r,b] = colors //Cannot redeclare block-scoped variable 'r'
var [g,r,r,b] = colors //order matters
console.log(r) // rosa

let [gr,,ro,,] = colors
console.log(ro)
