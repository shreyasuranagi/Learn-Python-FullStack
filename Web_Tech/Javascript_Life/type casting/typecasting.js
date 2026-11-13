//! explcity type casting

//! convert to NUMBER using Number() 
//! 2 ways- Number and parseInt()


//! NUmber() - converts any data type wihtout modifying it to a nUmber and by taking internal representaiont maybe
//~ string to number
var str = "3.4"
console.log(str) //3.4
console.log(typeof str) //string

console.log(Number(str)) //3.4
console.log(typeof Number(str)) //number

console.log(str) //3.4
console.log(typeof str) //string // no modifiction 


//~ try all data types
var x = 1
console.log(Number(x)) //1
var x = 1.3
console.log(Number(x)) //1.3
var x = 3n
console.log(Number(x)) //3
var x = true
console.log(Number(x))  //1
var x = 'abc'
console.log(Number(x)) // NaN
var x = undefined
console.log(Number(x)) //NaN
var x = null
console.log(Number(x)) //0
var x = 3.4
console.log(Number(x)) //3.4
var y = 'a12'
console.log(Number(y)) //NaN


// ----------------------------------------
// strigns to number using Number()
var x = ''
console.log(Number(x)) //0 
var x = ' '
console.log(Number(x)) //0
var x = ' 1'
console.log(Number(x)) //1
var x = ' 1 '
console.log(Number(x)) //1
var x = ' 1 2'
console.log(Number(x)) //NaN 
var x = ' 12    \n'
console.log(Number(x)) //12
var x = ' 1.2    \n'
console.log(Number(x)) //1.2 
var x = ' 1. 2    \n'
console.log(Number(x)) // NaN 
// ----------------------------------------
/*
NOTES for Number() :
it coverts a given data type to Number
rules-
0. string -> Number using Number() works only if stirng has ONLY number(int or float) with or without trailing and ending white space(but NOT space betwen), else NaN
1. null -> 0
2. undefined ->NaN
3. empty string '' or empty space ' ' -> 0
*/


//! parseInt() - parses only STRINGS to a number withotu modification and does NOT take internal representiaon like null or '' or false 

var data = '10'
console.log(parseInt(data)); //10
console.log(typeof parseInt(data)); //number
console.log(data)
console.log(typeof data)

let str = "3.4"
console.log(str) //3.4
console.log(typeof str) //string

console.log(parseInt(str)) //3 //! note
console.log(typeof parseInt(str)) //string //!note

var x = 3.4
console.log(parseInt(x)) //3 //!note
var y = 'a12'
console.log(parseInt(y)) //NaN 
var y = '12a13'
console.log(parseInt(y)) //12

//~ try
var x = 1
console.log(parseInt(x)) //1 
var x = 1.3
console.log(parseInt(x)) //1
var x = 3n
console.log(parseInt(x)) //3
var x = true
console.log(parseInt(x))  // NaN //!note
var x = 'abc'
console.log(parseInt(x)) // NaN
var x = undefined
console.log(parseInt(x)) //NaN
var x = null
console.log(parseInt(x)) //Nan //!note

//strings
var x = ''
console.log(parseInt(x)) //NaN //!note
var x = ' '
console.log(parseInt(x)) //NaN
var x = ' 1'
console.log(parseInt(x)) //1
var x = ' 1 '
console.log(parseInt(x)) //1
var x = ' 1 2'
console.log(parseInt(x)) //1 //! note no error= cos it parses until it doenst find a number - fins leaidng numbers
var x = ' 1.2    \n'
console.log(parseInt(x)) //1 //! note
console.log(parseFloat(x));


//NTOES:
/*
parseInt() baiscally onyl effectively converts onyl strings to a number (int only)

it doesnt take internal representation for null true false '' etc -> NaN
'1.2' -> 1
3.8 ->3
'12a' -> can extract 12 / leading numbers

*/


// ----------------------------------------

//! String() - returns a string but without changing original data


var s = new String("10")
console.log(typeof s); //object
console.log(String(s)); //10
console.log(typeof (String(s))); //string
console.log(s); //[String: '10']
console.log(typeof s);// object // no modification

var s = 10
console.log(typeof s); //nnumber
console.log(String(s)); //10
console.log(typeof (String(s))); //string
console.log(s); //10
console.log(typeof s);// number // no modification

var s = true
console.log(typeof s); //boolean
console.log(String(s)); // true
console.log(typeof (String(s))); // string
console.log(s); // true
console.log(typeof s);// boolean


var s = 3n
console.log(typeof s); //bigint
console.log(String(s)); //3
console.log(typeof (String(s))); //string
console.log(s); //3n //!ntoe
console.log(typeof s);// bigint

var s = [1, 3.4]
console.log(typeof s); //object
console.log(String(s)); //1,3.4
console.log(typeof (String(s))); //string
console.log(s); // [1,3.4]
console.log(typeof s);// object

var s = null 
console.log(typeof s); //object
console.log(String(s)); //null
console.log(typeof (String(s))); //string
console.log(s); // null
console.log(typeof s);// object

var s = undefined 
console.log(typeof s); //undefined
console.log(String(s)); //undefined
console.log(typeof (String(s))); //string 
console.log(s); // udnefined
console.log(typeof s);// undefined

var s = new String("10")
console.log(typeof s); //object
console.log(s.toString()); //10
console.log(typeof (s.toString())); //string
console.log(s); //[String: '10']
console.log(typeof s);// object // no modification

//NOTES
/*
String() converts aany DATA TYPE TO STIRNG reliably wihtout an y eroor including null and undefined! including Stirng objects
*/

//! toString() - 
//! converts any d.t to a String and returns string withtou modifying it
//! converts a string object to a string without modifying it
//!  converts an array to a string by seprating the items by commas
var s = new String("10")
console.log(typeof s); //object
console.log(s.toString()); //string
console.log(typeof (s.toString()));
console.log(s); //[String: '10']
console.log(typeof s);// object // no modification

var s = 10
console.log(typeof s); //nnumber
console.log(s.toString()); //10
console.log(typeof (s.toString())); //string
console.log(s); //10
console.log(typeof s);// number // no modification

var s = true
console.log(typeof s); //boolean
console.log(s.toString()); // true
console.log(typeof (s.toString())); // string
console.log(s); // true
console.log(typeof s);// boolean


var s = 3n
console.log(typeof s); //bigint
console.log(s.toString()); //3
console.log(typeof (s.toString())); //string
console.log(s); //3n
console.log(typeof s);// bigint

var s = [1, 3.4]
console.log(typeof s); //object
console.log(s.toString()); //1,3.4
console.log(typeof (s.toString())); //string
console.log(s); // [1,3.4]
console.log(typeof s);// object

var s = null 
console.log(typeof s); //object
console.log(s.toString()); //! TypeError: Cannot read properties of null (reading 'toString')
console.log(typeof (s.toString())); //string
console.log(s); // [1,3.4]
console.log(typeof s);// object

var s = undefined 
console.log(typeof s); //object
console.log(s.toString()); //1,3.4
console.log(typeof (s.toString())); //string //! TypeError: Cannot read properties of undefined (reading 'toString')
console.log(s); // [1,3.4]
console.log(typeof s);// object


//NOTES
/*
toString mainly converts any data type to a String type
esepcially usefutl to convert stirng object to string so operations/metdods have smooth behaviour
can be used often in arary to string conversions as well

note- any data type menas any type EXCEPT null and undefined

*/

// ----------------------------------------
// ----------------------------------------


//! BOOLEAN using 

//! truthy and falsy values

/*
false
0
-0
0n
""
null
undefined
NaN
*/
//FALSY VALUES
console.log(Boolean(false))
console.log(Boolean(''))
console.log(Boolean(null))
console.log(Boolean(undefined))
console.log(Boolean(NaN))
console.log(Boolean(0))
console.log(Boolean(-0))
console.log(Boolean(NaN))

console.log(Boolean('0'))
console.log(Boolean(-0))
console.log(Boolean([]))
console.log(Boolean([]))
console.log(Boolean("false"))


// ----------------------------------------
// ----------------------------------------
//! LOGICAL OPERATORS


//! &&
console.log(true && false); //false
console.log(true && 3); //false
console.log(true && "false");// "false"
console.log(true && null); //null
console.log(true && false);

console.log(false && true); //false
console.log(false && 3); //false
console.log(null && "false");// null
console.log('' && null); //''
console.log(true && false); //false


console.log(true && false); //false
console.log(true && 'somu'); //somu
console.log(false && "somu");// false
console.log('rani' && "somu"); //somu

// ! || operator

console.log(true || false); //true
console.log(true || 3); //true
console.log(true || "false");// ture
console.log(true || null); //true
console.log(true || false);  // true

console.log(3 || false); //3
console.log(2.6 || 3); //2.6
console.log('hi' || false);// hi
console.log(null || true); //true
console.log(false || 1);  // 1

//! ! operator
console.log((!!'helo'));


// NOTES-
/*

logical && - if both true -> true, else false
logical || - if any one true-> true, else false
logical ~ - if true-> false, else true

logical && - if op1 truethsy check if op2 truthsy then RETURN op2, else false
loigical || - if op1 truethsy, RETURN op1;   if not, check op2 -> if op2 is truethsy ,RETURN op2 , else RETURN false
logical ~ - if op1 is truethsy RETURN false; else RETURN true
*/
