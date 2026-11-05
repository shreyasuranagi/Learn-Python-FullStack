// console.log("JS is  awonderful lang");
// let i=0;
// for(; ; )
// {
//     i<3
//     i++
//     console.log("JRE punishment assignment "+i)
    
// }


// for(i=1; i<=10; i++)
// {
//     console.log(5*i)
// }

// for(let i=1; i<=10; i++)
// {
//     console.log(10+'X'+i+'='+10*i)
// }

//sum from 1 to 10
// let s=0
// for(let i=1 ;  i<=10;  i++)
// {
    
//     s=s+i;
// }

//get odd numbers from 1 to 50
console.log('odd nos from 1 to 50:')
for(let i=1; i<=50; i+=2)
{
    console.log(i)
}

//get  odd numbers from 1 to 50 get the count
let count=0
console.log('odd nos from 1 to 50 with count')
for(let i=1; i<=50; i+=2)
{
    console.log(i)
    ++count;
}
console.log('count='+count)

//get even nos from 50 to 100
let c=0;
console.log('even nos from 50 to 100 with count')
for (let i=50; i<=100; i++)
{
    if(i%2==0)
    {
        console.log(i)
        c++
    }
    
}
console.log(`count:${c}`)


//while