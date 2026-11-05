// function Print(a,b){
//     console.log(a)
//     console.log('this is JS class')
// }
// Print(10);


// function Print(){
//     console.log('lets go')
//     console.log('this is JS class')
// }
// Print();

// function GoodMorning(){
//     console.log('Good Morning!!!')
// }

// function GoodAfternoon(){
//     console.log('good afternoon~~')
// }

// function GoodEvening(){
//     console.log('good evening ^^')
// }

// GoodMorning()
// GoodAfternoon()
// GoodEvening()

// function greet()
// {
//     console.log('Good morning shreya')
// }
// greet("abc")

// function greet(names)
// {
//     console.log('Good morning '+names)
// }
// greet("abc")

// function greet_time(time){
//     if (time<12 && time>=9){
//         console.log('Good morning ')
//     }
//     else if (time>=12 && time<17){
//         console.log("Good afternoon")
//     }
//     else if(time>=17 && time<20){
//         console.log("good evening")
//     }
//     else{
//         console.log('invalid input')
//     }
    
// }
// greet_time(18)


// function greet_time(time){
//     if (9<=time<12){
//         console.log('Good morning ')
//     }
//     else if (1<=time<5 || time==12 || time<12){
//         console.log("Good afternoon")
//     }
//     else if(5<=time<8){
//         console.log("good evening")
//     }
//     else{
//         console.log('invalid input')
//     }
    
// }
// greet_time(12)

function update_cart(counter,button)
{
    if (button=='+'){
        counter+=1
    }
    else{
        counter-=1
    }
    return counter;
}
console.log(update_cart(3,'+'))
console.log(update_cart(10,'-'))