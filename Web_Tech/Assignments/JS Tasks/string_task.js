//1. reverse a string
let s ='abc'
let out=''

for(let j=-s.length; j<=-1; j++){
    
    out=s.at(j).concat(out)
    
}
console.log(out)

//2. validate email address
let email = 'suggi@gmail.com'
console.log(email.endsWith('gmail.com'))

//3. extract and format user input
let ip = '  prefix for random 123 text'
let i=ip.trimStart()
if( i.startsWith('prefix')){
    console.log(i.toUpperCase())
}
console.log(ip)

//4. mask sensitive information
let card='1234567891233456'
console.log( '*'.repeat(card.length-4)+(card.slice(-4)) )

//5. check if palindrome or not
let ss = 'lalal'
let o=''
for(let j=-ss.length; j<=-1; j++){ 
    o=ss.at(j).concat(o) 
}
console.log(o === ss)

//6. extract file extentsion
let file = 'notes.md'
console.log(file.slice(file.lastIndexOf('.')))