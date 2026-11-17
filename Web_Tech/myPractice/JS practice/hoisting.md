```
console.log(name);
var name = "JavaScript";

sayHello();

function sayHello() {
  console.log("Hello world!");
}
```
>
output-\
undefined\
Hello world!




```
console.log(score);
var score = 50;
score = 100;
console.log(score);

function getScore() {
  console.log(score);
}
getScore();
```
>
output-
undefined
100
100



### Medium: Function Execution Context (FEC) & Arguments
Focuses on what happens when an FEC is created and how parameters interact with local variables.
```
var x = 10;

function test(x) {
  console.log(x);
  var x = 20;
  console.log(x);
}

test(5);
console.log(x);
```
>
output-\
5\
20\
10



```
var fruit = "apple";

function eatFruit(fruit) {
  console.log(fruit);
  var fruit = "banana";
  console.log(fruit);
}

eatFruit("orange");
console.log(fruit);
```
output-
orange
banana
apple



### Hard: Hoisting Precedence (Function vs. Variable)
Focuses on the Creation Phase rules: Who wins when a variable and a function share the same name during hoisting?
```
var a = 100;

function foo() {
  console.log(a);
  var a = 200;
  function a() {}
  console.log(a);
}

foo();
console.log(a);
```
>
output-\
[Function: a]\
200\
100


```
var num = 10;

function check() {
  console.log(num);
  var num = 20;
  
  function num() {
    return 50;
  }
  
  console.log(num);
  console.log(num());
}

check();
```
output-\
undefined
[Function: num]
50

### CONCLUSION
- when there are parameters and fucntion variabels with the same name we get function variabels taking the paramter values
- when function and variables declaration with same name are accesswe dpriority goes to function variable 
