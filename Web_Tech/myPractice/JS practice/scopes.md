Since you're diving into **Scopes** now, these problems will test how JavaScript looks up variables across **Global Scope**, **Function Scope**, and **Block Scope** (using `let` and `const`), as well as the concept of **Scope Chain** and **Shadowing**!

Here is your new set of **Easy, Medium, and Hard** scope problems:

---

### 🟢 Easy: Global vs. Function Scope

*Focuses on whether variables declared inside a function can be accessed outside of it, and how outer variables are accessed inside.*

```javascript
let globalVar = "I am global";

function showScope() {
  let localVar = "I am local";
  console.log(globalVar);
  console.log(localVar);
}

showScope();
console.log(globalVar);
// What happens if we try to do this?
// console.log(localVar);

```

* **Question:** What gets printed, and what happens at the very end when trying to log `localVar` outside the function?

---

### 🟡 Medium: Scope Chain & Variable Shadowing

*Focuses on what happens when a local variable has the exact same name as a variable in an outer scope (Shadowing), and how the Scope Chain searches for variables.*

```javascript
let color = "blue";

function printColor() {
  let color = "red";
  console.log(color);

  function inner() {
    console.log(color);
  }
  inner();
}

printColor();
console.log(color);

```

* **Question:** What is the sequence of colors printed to the console? Which `color` does `inner()` reach for?

---

### 🔴 Hard: Block Scope (`let`/`const`) vs. Function Scope (`var`) & Temporal Dead Zone (TDZ)

*Focuses on the difference between block scopes created by curly braces `{}` and function scopes, plus a sneak peek at the Temporal Dead Zone.*

```javascript
let count = 10;

function evaluate() {
  // console.log(count); // Uncommenting this throws an error - why?
  let count = 20;

  if (true) {
    let count = 30;
    var flag = true;
    console.log(count);
  }

  console.log(count);
  console.log(flag);
}

evaluate();
console.log(count);

```

* **Question:** What gets printed inside `evaluate()` and at the end? Why does `flag` behave differently than `let count` regarding block boundaries?

---