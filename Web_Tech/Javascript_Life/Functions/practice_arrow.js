// ARROW FUNCTIONS
//---signle line of code---

//if return -> log the fucntion call
//if no return -> log it insicde function

//original type 1 - multiple params - implicit 
var s = (a,b) => a+b 
s(10,30) //wont be printed only receives value
console.log(s(10,30))

//original type 2 - single param - implicit
var s = a => a+15
s(10)  //wont be printed only receives value
console.log(s(10))

//original type 2 - no param - implicit
var s = _ => console.log('hi')
s() // 'hi' since console log already there in function only
console.log(s()) // 'hi' and then undefined

//with return and  {} - explicit
var s = (a,b) => { return a+b }
s(10,20) //wont be printed only receives value
console.log( s(10,20))  


//---multiple line of code---
//type 1a
var s = (a,b) =>{
    console.log()
    console.log(a)
    console.log(b)
    console.log(a+b)
}
s(10,20)

//type 1b
var s = _ =>{
    console.log('gm')
    console.log('hi')
}
s()

//type 2
var s = (a,b) =>{
    console.log('hi again')
    return a+b
}
console.log(s(20,20))

