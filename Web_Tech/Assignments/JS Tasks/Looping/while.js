// let i=1;
// while (i<=5){
//     console.log('tick tock '+i+' second');
//     i++;
// }

//table
console.log("nultiplication tables of 12")
var i=1
while(i<=10)
{
    console.log(`12 x ${i} = ${12*i}`)
    i++
}

//get sum from 1 to 10
let s=0
var i=0
console.log("sum from 1 to 10")
while(i<=10)
{
   s=s+i
   i++
}
console.log('Sum='+s)


//odd nos from 1 to 50
var i=1
while(i<=50)
{
    if(i%2!==0)
    {
        console.log(i)
    }
    i++
}

//odd nos fromm 1 to 50 with count
let c=0
var i=1
while(i<=50){
    console.log(i)
    c++
    i+=2
}
console.log('count odd:'+c)


//even nos from 50 to 100
var i=50
while(i<=100){
    if(i%2==0){
        console.log(i)
    }
    i++
}

//even nos from 50 to 100 with count
let co=0
var i=50
while(i<=100){
    console.log(i)
    i+=2
    co++
}
console.log('count of even:'+co)