//! q1.
// function changeNum(x) {
//   x = 50;
// }

// let a = 10;
// changeNum(a);
// console.log(a);
//* sol.1
//10
// -Numbers are primitives passed by value


//! q2.
// let greeting = 'hi';
// let copy = greeting;
// copy = 'hello';

// console.log(greeting);
// console.log(copy);
//* sol.3
//hi
//hello


//! q3.
// function renameUser(user) {
//   user.name = 'Maya';
// }

// const person = { name: 'Leo' };
// renameUser(person);
// console.log(person.name);
//* sol.3
//Maya

//! q4.
function replaceObj(obj) {
  let obj = { count: 99 };
}

function mutateObj(obj) {
  obj.count = 99;
}

const data = { count: 1 };
replaceObj(data);
console.log(data.count);

mutateObj(data);
console.log(data.count);
//* sol.4
//99
//99



// ----------------------------------------

//! q5.
function updateArr(arr) {
  arr.push(4);
  arr = [10, 20];
  arr.push(30);
}

const nums = [1, 2, 3];
updateArr(nums);
console.log(nums);


//! q6.
const list = [{ id: 1 }, { id: 2 }];
const shallowCopy = [...list];

shallowCopy[0].id = 100;
shallowCopy[1] = { id: 200 };

console.log(list[0].id);
console.log(list[1].id);


//! q7.
const config = { theme: 'dark', meta: { retries: 2 } };
const clone = { ...config };

clone.theme = 'light';
clone.meta.retries = 5;

console.log(config.theme);
console.log(config.meta.retries);


//! q8.
function bump(val) {
  val += 1;
}

const state = { score: 10 };
bump(state.score);
console.log(state.score);


//!q9.
function swap(a, b) {
  const temp = a;
  a = b;
  b = temp;
}

let first = { label: 'A' };
let second = { label: 'B' };

swap(first, second);
console.log(first.label, second.label);

//! q10.
function tricky(a, b) {
  a.value = 2;
  b = a;
  b.value = 3;
  a = { value: 4 };
  return a.value + b.value;
}

const x = { value: 1 };
const y = x;

const result = tricky(x, y);
console.log(result);
console.log(x.value);
console.log(y.value);