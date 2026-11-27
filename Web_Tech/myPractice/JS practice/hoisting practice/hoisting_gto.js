//! q1.
// console.log(a);
// console.log(b);

// var a = 10;
// let b = 20;

//* sol1
//undefined
//ReferenceError: cannot access b before initialized


//! q2.
// sayHi();
// sayHello();

// function sayHi() {
//   console.log("Hi!");
// }

// var sayHello = function () {
//   console.log("Hello!");
// };
//* sol
// Hi!
// cannot call undefined - undefined is not a function -> sayHello is not a function


// !q3.
// var x = 1;

// function test() {
//   console.log(x);
//   var x = 2;
//   console.log(x);
// }

// test();
//* sol3
// undefined
// 2


// !q4.
// console.log(typeof foo);

// var foo = "I am a string";

// function foo() {
//   return "I am a function";
// }

// console.log(typeof foo);
//* sol
//function -becuase functions are hoisted before variables, in CP oo-1500 (address) and duplicate name foo is ignored so it takes function
//string - later reinitialsiation to a string overrides from function to string



//! q5.
// console.log(a);
// var a = 10;
// var a = 20;
// console.log(a);
//* sol.5
// undefined
// 20
//-multiple var declarations in the same scope, but only the first declaration is hoisted


//! q6.
// console.log(foo);
// var foo = function() {
//     return "Hello!";
// };
// console.log(foo());
//* sol.6
//undefined
//Hello!
//-function is allocated memory and assigned during EP and in CP only var gets undefined

// //! q7.
// console.log(foo);
// var foo = () => {
//     return "Arrow Function!";
// };
// console.log(foo());
//* sol.7
//undefined
//Arrow Function!

//! q8.
// console.log(foo);
// var foo = () => {
//     return "Arrow Function!";
// };
// console.log(foo());
//* sol8.
//Arrow Function!

// ----------------------------------------

//~ HARD questions

//! q101.
// let x = 10;
// function test(a = x, b = y, y = 20) {
//   console.log(a, b, y);
// }
// test();
//* sol.101
// ReferenceError: Cannot access 'y' before initialization 
//-Default parameters have their own intermediate scope, evaluated left to right ormally in undefined unless a parameter to right refernce it then in TDZ


//! q102.
// function greet(name) {
//   console.log(name); // "Alice" (parameter value is preserved, not undefined)
//   var name = "Bob"; // can redeclare name
//   console.log(name); // "Bob"
// }
// greet("Alice");

//! q103.
// function greet(name) {
//   console.log(name); 
//   let name = "Bob"; // SyntaxError: Identifier 'name' has already been declared; cant redeclare name
//   console.log(name); 
// }
// greet("Alice");

//! q104.
// console.log(typeof foo);
// var foo = 'hello';
// function foo() {
//   return 'world';
// }
// console.log(typeof foo);
//* sol.104
//function
//string

// //! q105.
// function run(value) {
//   if (false) {
//     var value = 'overwritten';
//   }
//   console.log(value);
// }
// run('initial');
//*sol105.


// ! q106.
// var greet = function sayHi() {
//   console.log(typeof sayHi);
//   sayHi = 'changed';
//   console.log(typeof sayHi);
// };
// greet();
// console.log(typeof sayHi);
//* sol106.
//function
//function
//undefined


//Testing
// function fun(data) {
//   data=99
//   console.log(data);
  
// }
// fun(100)
//99


// function fun(data) {
//   var data=99
//   console.log(data);
  
// }
// fun(100)
//99


// function fun(data) {
//   let data=99
//   console.log(data);
// }
// fun(100)
//SyntaxError: Identifier 'data' has already been declared


// function scoped(data) {
//   {
//     let data = 99;
//     console.log('inside block:', data); // 99
//   }
//   console.log('outside block:', data); // 100
// }

// scoped(100);
//99
//100



// function withDefault(data = 10) {
//   var data = 99;
//   console.log(data);
// }
// withDefault(100);
//Throws SyntaxError: Identifier 'data' has already been declared