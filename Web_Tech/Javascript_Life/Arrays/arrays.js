//arrays

//creation using string literal
let arr = [1,2,3,6,7,8,8,6,2,7,2,1,2,1,4,3]
console.log(arr)

let arr2=[1.2,3n,'hello',true,false,90,2,'o']
console.log(arr2)

//show mutable nature of array
arr3=[0,1] //wrong
console.log(arr)

let s='abc'
console.log(s)
s='def'
console.log(s)
s[1]='z' 
console.log(s) // shows mutable nature
console.log(arr3)
arr3[1]=2
console.log(arr3)

//length
console.log(arr2.length)


// array literal - []
var a=10
let data = [10,true,3.4,function (){console.log('im array item inside')}, {name:'shreya'},`there are ${a} apples`]
console.log(data)
console.log(data[3])
console.log(data[3]())
data[3]()
console.log(data[4])
console.log(typeof data)

//using Array constructor
let arr5=new Array(1,3.4,6,-12,'a')
console.log(arr5)
console.log(typeof arr5) //object

let array = new Array(10)
console.log(array) // [ <10 empty items> ]
console.log(typeof array)
console.log(array.length) //10
console.log(array[2]) // undefined
array[2]=3
console.log(array) // [ <2 empty items>, 3, <7 empty items> ] 

