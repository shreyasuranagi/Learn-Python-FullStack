// // #########################

// // ARRAY INSTANCE METHODS

// let arr = [1,5.3,6,'hi']
// console.log('array:'+arr) //5

// // end of array - push() pop()

// //push()
// console.log(arr.push(7)) //5 - length after pushing
// console.log(arr) // [ 1, 5.3, 6, 'hi', 7 ]

// // pop()
// console.log(arr.pop()) // 7 - retunrs removed element
// console.log(arr) // [ 1, 5.3, 6, 'hi' ]

// //beginning of array - shift() and unshift()
// // shift()
// console.log(arr.shift())
// console.log(arr)

// //  unshift()

// arr.unshift(7)
// console.log(arr)

// //experiment
// console.log(arr.unshift(8))
// console.log(arr)
// console.log(arr.push(100,function(){console.log('hi')},102,[-1,-2]))
// console.log(arr)


// // slice()

// let arr = [10,20,30,40,50,60]
// console.log(arr)

// console.log(arr.slice())
// console.log(arr.slice(2))
// console.log(arr.slice(-3))
// console.log(arr.slice(2,4))
// console.log(arr.slice(-4))
// console.log(arr.slice(4,2)) //?

// let arr1=[]
// console.log(arr1.slice()) //[]
// console.log(arr1.slice(1)) //[]


// // splice(SI,dC, item1,item2,item3,...)

// let a = [10,20,30,40,50,60]
// console.log(a)

// var d = a.splice(2,2,90)
// console.log(d) // 30 40
// console.log(a)

// var d = a.splice()
// console.log(d) // []
// console.log(a)

// var d = a.splice(-3,1,-100) //-ve index supported
// console.log(d) 
// console.log(a)

// var d = a.splice(10,1,-100) // SI exceeds limit -[]
// console.log(d) // []
// console.log(a)

// var d=a.splice(4,0,'rani')
// console.log(d)
// console.log(a)

//concat
// let a1=[1,3,5]
// let b1=[5,2.4,1,2]
// console.log(a1.concat(b1)) // new array
// console.log(a1)


// //reverse()
// let a=[10,20,30,40,50]
// console.log(a)
// console.log(a.reverse())
// console.log(a)

// //join()
// let a = [1,4,24,6,2]
// console.log(a)
// console.log(a.join()) //default with the commas ,
// console.log(typeof a.join())
// console.log(a.join(''))
// console.log(a.join('---%---'))



// //lastIndexOf() -L to R
// let a1=[1,2,3,4,5,6,7,5,6,9]
// console.log(a1)
// console.log(a1.indexOf(5)) //4
// console.log(a1.indexOf(100)) //-1
// console.log( a1.indexOf()) //-1

// //lastIndexOf() - R to L
// let a2=[1,2,3,4,5,6,7,5,6,9]
// console.log(a2)
// console.log(a2.lastIndexOf(5)) //7

// //includes()
// let a=[1,2,3,4,3]
// console.log(a.includes(5)) //false
// console.log(a.includes(2)) //true
// console.log(a.includes(2,1)) //true
// console.log(a.includes(3,1,3)) //true


// // array.entries()

// let arr = [10,20,30,40,50]
// console.log(arr.entries());
// for(let x of arr.entries()){
//     console.log(x);
// }
// console.log(arr.entries[2]) //undefined
// console.log()

// for(let x of arr.keys()){
//     console.log(x);
// }
// console.log(arr.keys())

// for(let x of arr.values()){
//     console.log(x);
// }

// every()
let data=['pink','red','yellow','','undefined',undefined]
console.log(data.every( (col) => col!== undefined)) //true // checks value and data type is undefined or not
