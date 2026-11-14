var s = new String("10")
console.log(typeof s); //object
console.log(String(s)); //string
console.log(typeof (String(s)));
console.log(s); //[String: '10']
console.log(typeof s);// object // no modification