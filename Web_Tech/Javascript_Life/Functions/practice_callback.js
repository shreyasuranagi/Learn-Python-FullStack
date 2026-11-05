// callback functions

// with reference/ funciton name

function greet(greet_time) {
    greet_time()
}
function gm() {
    console.log('gm')
}
function ga() {
    console.log('ga')

}


//callback wiith named reference function
function hello(time) {
    console.log('Welcome')
    // if (9<=time<12){
    //     greet(gm)
    // }
    if (time >= 9 && time < 12) {
        console.log(gm)
    }
    else {
        greet(ga)
    }
}


//callback wiith  function definition
function hello(time) {
    console.log('Welcome')
    // if (9<=time<12){
    //     greet(gm)
    // }
    if (time >= 9 && time < 12) {
        greet(function gm() {
            console.log('gm')
        })
    }
    else {
        greet(function ga() {
            console.log('ga')
        })
    }
}



//callback wiith anonymous function 
function hello(time) {
    console.log('Welcome')
    // if (9<=time<12){
    //     greet(gm)
    // }
    if (time >= 9 && time < 12) {
        greet(function ()  {
            console.log('gm')
        })
    }
    else {
        greet(function () {
            console.log('ga')
        })
    }
}


//callback wiith  anonymous arrow function
function hello(time) {
    console.log('Welcome')
    // if (9<=time<12){
    //     greet(gm)
    // }
    if (time >= 9 && time < 12) {
        greet( () => console.log('gm') )
    }
    else {
        greet( () => console.log('ga') )
    }
}



hello(17)