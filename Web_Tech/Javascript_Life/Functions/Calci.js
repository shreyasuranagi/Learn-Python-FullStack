function Calci(operation,a,b){
    return operation(a,b)
}

function add(a,b){
    return a+b
}
function mul(a,b){
    return a*b
}
function div(a,b){
    return a/b
}
function sub(a,b){
    return a-b
}

console.log(Calci(sub,3,9)) // sub is the callback function, Calci is HOF

console.log()




