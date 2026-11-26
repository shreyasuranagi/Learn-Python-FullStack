// import {password} from './China.js'

// console.log(password) // 3j234j

// import {age} from './China.js'

// console.log(age); //21


// import {password,age} from './China.js' //SyntaxError: Identifier 'password' has already been declared

// console.log(password,age)

// import {password,age,emp} from './China.js'
// console.log(password,age,emp) // 3j234j 21 { name: 'ramu' }


// import {password:p,age:a,emp:e} from './China.js' // alias not allowed
// console.log(p,e,a) // 3j234j 21 { name: 'ramu' }

// import {name} from './China.js' // SyntaxError: The requested module './China.js' does not provide an export named 'name'
// console.log(name)