//! Object destructuring - process of extracting individual properties from n object directly without the reglar syntax of obj reference

let data ={
    name:'abc',
    age:21,
    status:true,
    sleeping: () => console.log('dnd')
}

let {n,a,st,sl} = data
console.log(n) //undefined
console.log(data.name);
console.log(data.n) //undefined
console.log(data.sleeping())


let {name,status,age, sleeping} = data // order does not matter
console.log(data.age) //21
console.log(age) //21

