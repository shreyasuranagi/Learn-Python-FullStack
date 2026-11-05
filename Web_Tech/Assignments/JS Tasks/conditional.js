//if 
//if-else

// var age=3
// if (age>=60)
// {
//     console.log('u can vot for xyz')
// }


// var age=3
// if (age>=18)
// {
//     console.log('u can vot for xyz')
// }
// else{
//     console.log('not eligible')
// }


//else if ladder

// let marks=3
// if (marks>90){
//     console.log("Grade A+")
// }
// else if (marks>=80){
//     console.log("Grade A")

// }
// else if (marks>=70){
//     console.log("Grade B+")

// }
// else if (marks>=60){
//     console.log("Grade B")

// }
// else if (marks>=50){
//     console.log("Grade C+")

// }
// else if (marks>=40){
//     console.log("Grade C")

// }
// else if (marks>=30){
//     console.log("Just pass")

// }
// else{
//     console.log("fail")
// }


// let num=-1
// if (num>0){
//     console.log("positive")
// }
// else if(num<0){
//     console.log("negative")
// }
// else{
//     console.log("zero")
// }


//********* */
//greatest among 2 numbers
// let a=13
// let b=13
// if (a>b){
//     console.log(`${a} is greater`)
// }
// else if(a<b){
//     console.log(`${a} is greater`)
// }
// else{
//     console.log(`both are equal - ${a}`)
// }


//greatest among 3 numbers

// let a=12
// let b=12
// let c=11

// if (a>=b && a>=c){
//     console.log(a)
// }
// else if(b>=c){
//     console.log(b)

// }
// else{
//     console.log(c)
// }





// let days = 3.0
// switch (days) {
//     case 1 + 0: console.log("Monday");
//         break;
//     case 2: console.log("Tuesday");
//         break;
//     case 3: console.log("Wednesday");
//         break;
//     case 4: console.log("Thursday");
//         break;
//     case 5: console.log("Friday");
//         break;
//     case 6: console.log("Saturday");
//         break;
//     case 7: console.log("Sunday");
//         break;

//     default:
//         console.log("invalid");

// }

//Ternary operator
// let flag=false
// let result = flag?"logged in":"logged out"
// console.log(result)

// let cond=3>2
// console.log(cond)

// let age=22
// console.log(age>21?"welcome to party":"Get lost")

// let marks=85
// console.log((marks>90)?"Grade A":(marks>80)?"Grade B":(marks>70)?"Grade C":"None")


//5 example of ternary operator
//example 1
var weather='rainy'
//var weather='sunny'
console.log(weather=='sunny'?'play':'assignment')

//example 2
let size=36
console.log(size>=36?'XL':size>=34?'L':size>=30?'M':'S')

//example 3
let num=5
console.log(num%2==0?'even':'odd')

//example 4
let temp=35
console.log(temp>35 && temp<25?'ac':'fan')

//example 5
let button='clicked'
console.log(button=='clicked'?'submit':'not submit')