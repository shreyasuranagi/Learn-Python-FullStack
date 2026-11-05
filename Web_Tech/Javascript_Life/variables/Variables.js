

        // Var keyword
        //var box; //declaration
        //box="Toys" //initialisation
//


// var name; //only declaration possible
// console.log(name);  //undefined

// var name;  
// name="shreya" // decla and initialization on diff line
// console.log(name) //shreya


// var name='shreya' //declaration and initialization on same line
// console.log(name) //shreya

// var name='abc'
// console.log(name) 
// name = 'shreya'
// console.log(name) // reintialization is possible with var keyword

// var name='abc'
// console.log(name)
// var name='shreya';
// console.log(name) //re-declaration is possible with var keyword

// var name='abc'
// console.log(name) //abc
// var name;
// console.log(name) //abc


//----------------------

//LET keyword

// let name; //only declaration possible

// let name
// name='abc' //declaration and init on diff line is possible
// console.log(name) //abc

// let name = 'abc' //declaration and init on same line is possible
// console.log(name)  //abc


// let name='abc'
// name='shreya' //re-initialization is possible with let keyword
// console.log(name) //shreya

// let name='abc'
// console.log(name) //abc //?doubt- why? it shoudl at least print if js in interpreted?
// let name='shreya'
// console.log(name)

//?interesting
// var name='abc'
// console.log(name) //abc NOT printed
// var name; //no error
// let name='shreya'
// console.log(name) //SyntaxError: Identifier 'name' has already been declared

//---------------------------CONST keyword

// const name; //declaration alone is not possible
// console.log(name)


// const name='abc' // declr and init on same line is possible
// console.log(name) //abc

// const name;
// name='abc' // declar and init on diff line is not possible
// console.log(name)

// const name='abc'
// console.log(name)
// name='shreya' //re init not possible

// const name='abc'
// console.log(name) //abc
// const name='shreya' // redeclaration is not possible