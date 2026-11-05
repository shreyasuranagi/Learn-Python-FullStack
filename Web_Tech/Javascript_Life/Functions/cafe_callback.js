// function Greeting()
// {
//     console.log('Welcome to the cafe')
//     console.log('Thank you for ordering')

//     console.log()
//     console.log('choose your order')

//     //some conditionals based on the input
//     // Dosa()
//     Pizza()

//     //disad: for 100 items writing 100 calls/conditionals is not scalable
//     //disad: if new item is added changes must be made to this MAIN code again
    
//     //callback adv: based on choice, dynamically calls that function

// }

function Greeting( callback )
{
    console.log('Welcome to the cafe')
    console.log('Thank you for ordering')

    console.log()
    console.log('choose your order')

    callback()
    
    //callback adv: based on choice, dynamically calls that function 

}

function Dosa(){
    console.log('DOsa is being prepared')
    console.log('10min...')
    console.log()
    console.log('your Dosa is ready')
}   

function Pizza(){
    console.log('Pizza is being prepared')
    console.log('10min...')
    console.log()
    console.log('your Pizza is ready')
}

//Greeting() //old code

//suppose: user choice
Greeting(Dosa) //new code with callback function
Greeting(Pizza)