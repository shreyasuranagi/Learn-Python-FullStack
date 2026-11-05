// //--------normal named function--------
// function TotalMarks(h,c,j,p){
//     console.log(h+c+j+p)
// }
// TotalMarks(90,80,70,60)
// console.log(TotalMarks(90,80,70,60))

// //----named function with return stmt---------
// function TotalMarks(h,c,j,p){
//     return h+c+j+p
// }
// console.log(TotalMarks(90,80,70,60)+10) 


// //-------anonymous function---------

// let bhoot =
// function() {
//     console.log('this is anonymous function')
// }
// bhoot() //actual function call stmt
// console.log(bhoot)
// console.log(typeof bhoot)
// console.log()
// console.log(bhoot())
// console.log(typeof bhoot())


// //------Arrow function -shorter way to write functions-----
// //normal function-
// function addition(a,b)
// {
//     console.log(a+b);
// }
// addition(10,20);


// //----arrow function---
// //syntax- ()=>{}
// (a,b)=>{ console.log(a+b) } //cannot call it tho


// use function expression to store the function in a variable and then call it
// var add = (a,b) => { console.log(a+b) }
// add(10,20)

// // 1. single line - with return and curly braces
// var add = (a,b) => {return a+b} //explicit return
// console.log(add(10,20))

// // wrong type 1
// var add=(a,b) => {a+b} //worng-undefined must ahve return keyword when using {}
// console.log(add(10,40)) 

// //wrong type 2
// var add=(a,b) => return a+b //wrong-undefined must ahve {}  when using return
// console.log(add(10,40)) 

// // 2. single line - without return and without curly braces
// var add=(a,b) => a+b //implicit return
// console.log(add(10,40))

// // 3. single parameter - without return and without curly braces
// var add = a => a+20
// console.log(add(10))



// //function expression
// var adds = function printAdd(){
//     console.log(10+100);
// }
// // printAdd() //ReferenceError: printAdd is not defined 
// // once function is assigned to a variable, the function name cannot be used to call, we use func expression variable name
// adds()


// //=========CALLBACK FUNCTION=======

// //--- CASE 1---
// // passing a function as an argument to another function is called callback function
// //by using function reference inside as callback

// function add()
// {
//     console.log(10+200)
// }

// function Task(fun_add)
// {
//     fun_add()
// }

// Task(add) // add is the callback function
// //function defintion inside callback


// //--- CASE 2---

// function Task(fun_add)
// {
//     fun_add()
// }

// Task(
//     function add() //CALLBACK FUNCTION
// {
//     console.log(10+200)
// }
// )


// //--- CASE 3---
// //using anoymous functions as callback function
// function Task(fun_add)
// {
//     fun_add()
// }

// Task(
//     function ()  //CALLBACK FUNCTION - anonymous function
// {
//     console.log(10+200)
// }
// )


// HOF Function
//type 1 - acccepts another function as parameter

function Task(func_add){
    func_add()
}
function add()
{
    console.log(10+20)
}
Task(add) //Task is HOF function


//type 2 - returns another function 

function Task() //is HOF as it returns another function
{
    return function(){
        console.log('hi')
    }
}

let result = Task()
result()

//doubt- where best to log things and where best to return?





// console.log(add())  //210 undefined(grey)
// console.log(typeof add()) //210 undefined(printed)
// console.log(add) //[Function: add]
// console.log(typeof add) //function
// Task(add)