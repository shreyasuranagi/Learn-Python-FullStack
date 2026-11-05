function Greeting(callback, takeway) {
    console.log('Welcome to the cafe')
    console.log('Thank you for ordering')

    console.log()
    console.log('choose your order')

    // callback()
    //takeway() //wrong cos of timer in callback depndency
    callback(takeway)
    //callback adv: based on choice, dynamically calls that function 

}

function Dosa(takeway) {
    setTimeout(() => {
        console.log('DOsa is being prepared')
        console.log('10min...')
        console.log()
        console.log('your Dosa is ready')
        takeway()
    },5000)

}

function Pizza() {
    console.log('Pizza is being prepared')
    console.log('10min...')
    console.log()
    console.log('your Pizza is ready')
}


function takeaway() {
    console.log('Your order is ready to Takeaway. Pls visit again')
}
//Greeting() //old code

//suppose: user choice
Greeting(Pizza, takeaway) //new code with callback function

