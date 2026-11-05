var str='JavaScript'
// at(), charAt()

console.log(str[0])
console.log(str.at(0))
console.log(str.charAt(0))

console.log('negative indices\n')
//negative indices 

console.log(str[-1]) //undefined
console.log(str.at(-1)) //t
console.log(str.charAt(-1)) // ->nothing

console.log('non existing indices')
// non existing positive indices
console.log(str.at(15)) //undefined
console.log(str.charAt(15)) // -> nothing


// charCodeAt()

let j ='JavaScript'
console.log(j.charCodeAt(4)) //83
console.log(j.charCodeAt(-1)) //NaN

//concat
let s1='Java'
let s2='Script'
let newstr1 = s1.concat(' ',s2,'is a great lang')
let newstr2 = s1.concat(' ',s2,6*12.5,'is a great lang') //Java Script75is a great lang
console.log(newstr1)
console.log(newstr2)


//includes()

var s='JS is Java Script'
console.log(s.includes('is'))
console.log(s.includes('pt'))
console.log(s.includes('z'))
console.log(s.includes('s',4))
console.log(s.includes('S',11))

//indexOf()
var s ='javascript'
console.log(s.indexOf('a'))
console.log(s.indexOf('a',s.indexOf('a')+1)) // a after the first a
console.log(s.indexOf('z'))



//string interpolation
//7. lastIndexOf
var s ='java script java'
console.log(s.lastIndexOf('i')) //8
console.log(s.lastIndexOf('va'))
console.log(s.lastIndexOf('va',0))
// console.log()
// console.log()

//split - converta string to an array
var str='Javascript      is a \n wonderful language'
console.log(str.split()) // will conside the entire string as a single item in an array 
console.log(str.split(' '))
console.log(str.split('i'))
console.log(str.split(''))
console.log(str.split('a'))
console.log(str.split('a',3))

//toUpperCase
var s = 'TodaY is 2nd MoNdAY'
console.log(s.toUpperCase())
console.log(s)
console.log(s.toLowerCase())

//trim
var s = 'JavaSript is a wonderful language'
var s3= '   JavaSript is a wonderful language'
console.log(s.length) //33
console.log(s3.length) //36
console.log(s3) //   JavaSript is a wonderful language
console.log(s3.trim()) //JavaSript is a wonderful language
console.log(s3) //   JavaSript is a wonderful language
console.log(s3.length) //36
console.log(s3.trim().length) //33

//trimStart()
//trimEnd()


console.log()
console.log('TRIMSTART AND TRIMEND')
var s ='   Javascript     ' //3 spaces fornt 5 space at end
console.log(s)
console.log(s.length) //18
console.log(s.trimStart()) 
console.log(s.trimStart().length) //15
console.log(s.trimEnd())
console.log(s.trimEnd().length) //13

//doesnt work for without white space
// var str='**java**'
// console.log(str.trim('*'))


//15. startsWith()

var link = "https://www.url.com"
console.log(link.startsWith("https"))
console.log(link.startsWith("www",8))

//endswith
var data="images.jpg"
console.log(data.endsWith('.jpg'))

//repeat()
var data ='hello..'
var n =data.repeat(11)
console.log(n)

//padStart()
var data='type'
console.log(data.padStart(2,'.'))

//padStart
var data='typing'
console.log(data.padEnd(10,'.'))

//padEnd
var heading = 'analysis'
h1=(heading.padStart(20,'-'))
console.log(h1.padEnd(30,'-'))

//replace
var data = 'ramu ramu'
console.log(data.replace('ra','so'))
console.log(data)
console.log(data.replaceAll('ra','so'))

//toString()

var n=3n
//try  with object
console.log(n)
console.log(typeof(n))
var s=n.toString()
console.log(s)
console.log(typeof s)

var s=new String('test')
console.log(typeof s) //object
console.log(s)  // [String: 'test']
var snew=s.toString() 
console.log(typeof snew) //string
console.log(snew) //test

//slice
//substr

var s= 'Java Script is Wonderful Language'

//slice
console.log(s.slice())
console.log(s.slice(4))
console.log(s.slice(-19))
console.log()
console.log(s.slice(11,22)) // 22 is exlusive
console.log(s.slice(-15,-7)) // 
console.log(s.slice(22,11)) // ''
console.log(s.slice(-7,-15)) // ''
console.log(s.slice(10,-3)) // goes from 10 till the -3 index


//substr
console.log('subtr--')

console.log(s.substring()) //0
console.log(s.substring(4)) //0th
console.log(s.substring(-19)) //0th
console.log()
console.log(s.substring(11,22)) // 22 is exlusive
console.log(s.substring(-15,-7)) //(0,0) ''
console.log(s.substring(22,11)) // swaps - (11,22)
console.log(s.substring(-7,-15)) // (0,0) ''

console.log(s.substring(10,-16)) // actually goes from 0 to 9 , -16->0th index - so no ending index

