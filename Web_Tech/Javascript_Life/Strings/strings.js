var s1='a$2.'
console.log(s1)

//var s2='it is the dog's fault' //error
console.log(s1)
console.log(typeof s1)



var s3=`"it is the dog's fault"`
console.log(s3)


//multiline string not possible sing '' and ""
// var s4=" abc
// SVGFEDropShadowElements
// sf"

//multiline 
var s5=` hello
world
today is
Thursday `
console.log(s5)


//string concatenation without built in methods - using + concatenation operator
let first_name='Shreya'
let last_name="Suranagi"
let dob=7
console.log(typeof first_name)

console.log('My first name is '+ first_name +' and my last name is '+last_name+dob)
console.log('My full name is '+(first_name+last_name))


//String INterpolation - dynamic access of data inside string using
// ${}  - string interpolation symbol
console.log(`My first name is ${first_name} and my last name is ${last_name}`)
console.log(`My 'full name' is ${first_name+' S ' +last_name}`)

//using String constructor

let str = new String("JavaScript")
console.log(str) //[String: 'JavaScript']
console.log(typeof str) //object

console.log(2+str+' and Web tech')


// length property
// .length
let data='abcd@5 324 21'
console.log(data.length)
console.log(typeof length)

//indexing
console.log(data[0])
console.log(data[4])
console.log(data[data.length - 1])
console.log(data[-2])

for(let i=0; i<data.length; i++)
{
    console.log(data[i])
}