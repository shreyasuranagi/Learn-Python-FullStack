
//! single item export
// let toys = 'Electric cars'

// export default toys 


//! function export 

// function add(a,b){
//     console.log(a+b)
// }
// export default add

//! export multiple items - using multiple times
// let toys = 'Electric cars'
// function add(a,b){
//     console.log(a+b)
// }

// export default toys
// export default add // SYNTAX error multiple default export statements are not possible

//! exporting mutiple data - usinng object

let toys = 'Electric cars'
function add(a,b){
    console.log(a+b)
}

export default { toys, add }