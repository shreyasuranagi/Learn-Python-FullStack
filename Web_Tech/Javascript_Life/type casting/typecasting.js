//! explcity type casting

//! convert to NUMBER using Number() 
//! 2 ways- Number and parseInt()


//! NUmber() - converts wihtout modifying
//~ string to number
var str = "3.4"
console.log(str) //3.4
console.log(typeof str) //string

console.log(Number(str)) //3.4
console.log(typeof Number(str)) //number

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

// ----------------------------------------
/*
NOTES :
string to Number works only if stirng has ONLY number(int or float) , else NaN

*/

//! parseInt()

var data = 10
console.log(parseInt(data)); //10
console.log(typeof parseInt(data)); //number


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
console.log(parseInt(x)) //1 
var x = ' 12    \n'
console.log(parseInt(x)) //12 //!note
var x = 1.2
console.log(parseFloat(x));

// ----------------------------------------

//! String() - returns a string but without changing original data
let data = 109
console.log(String(data)); //109 
console.log(typeof data); //string
console.log(typeof String(data)); //number
data = String(data)
console.log(typeof data); //string


var x = true
console.log(String(x));
console.log(String(x));
console.log(typeof x);
console.log(typeof String(x));

//! toString() - converts any d.t  and returns string withtou modifying it
var s = new String("10")
console.log(typeof s); //object
console.log(s.toString()); //string
console.log(typeof (s.toString()));
console.log(s); //[String: '10']
console.log(typeof s);// object

var s = 10
console.log(typeof s); //nnumber
console.log(s.toString()); //10
console.log(typeof (s.toString())); //string
console.log(s); //10
console.log(typeof s);// number

var s = true
console.log(typeof s); //nnumber
console.log(s.toString()); //10
console.log(typeof (s.toString())); //string
console.log(s); //10
console.log(typeof s);// number


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

var s = null //! TypeError: Cannot read properties of null (reading 'toString')
console.log(typeof s); //object
console.log(s.toString()); //1,3.4
console.log(typeof (s.toString())); //string
console.log(s); // [1,3.4]
console.log(typeof s);// object

var s = undefined //! TypeError: Cannot read properties of undefined (reading 'toString')
console.log(typeof s); //object
console.log(s.toString()); //1,3.4
console.log(typeof (s.toString())); //string
console.log(s); // [1,3.4]
console.log(typeof s);// object

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
