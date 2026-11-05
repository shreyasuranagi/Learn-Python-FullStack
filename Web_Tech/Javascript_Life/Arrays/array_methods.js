// Array.from()
var data = 'Shreya'
var arr = Array.from(data)
console.log(data)
console.log(arr)

var data = 2
console.log(Array.from(data)) // []

var data = true
console.log(Array.from(data)) // []

var data = function () { console.log(hi) }
console.log(Array.from(data)) // []

var data = [10, 20]
console.log(Array.from(data)) // [ 10, 20 ]

var data = { name: 'abc' }
console.log(Array.from(data)) // []

//
var data = [1, 2, 3, 4, 5]
console.log(Array.from(data)) // [ 1, 2, 3, 4, 5 ]
console.log(data) // [ 1, 2, 3, 4, 5 ]

console.log(Array.from(data, (i) => i ** 2)) //[ 1, 4, 9, 16, 25 ]

//convert str to array and add 0 after each character
var str = 'Javascript'
// console.log(  Array.from(Array.from(str,(ch)=>ch+'0'), function(i){ var out=''; out=out+i}))
console.log(Array.from(str, (ch) => ch + '0'))
console.log(Array.from(str, (ch) => ch + '0')[0].concat(Array.from(str.slice(1), (ch) => ch + '0')).toString().replaceAll(',', ''))
console.log(Array.from(str, (ch) => ch + '0').toString())
console.log(Array.from(str, (ch) => ch + '0').toString().replaceAll(',', ''))

//Array.isArray
var arr = '[1,2,3]'
if (Array.isArray(arr)) {
    console.log('data received is array')
}
else {
    console.log('data received is NOT array')
}


//! Arrray.of()
var a = Array.of(1, 2, 3, 4, 5, 6, 7, 8, 9) // similar to Array constructor diff- single arg->single item in array instead of length
console.log(a)
var b = Array.of(10)
console.log(b)


// passing array
var a = [1, 2, 3]
var b = new Array(a) //
console.log(b)
var c = Array.of(a)
console.log(c)




