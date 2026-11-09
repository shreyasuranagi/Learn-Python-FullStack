# PYthon notes - 08-11-2026

### namespaces
- Namespaces in Python is the way / container where entities are stored like
variable name - value
function name - function
class name - class objects

- types of namespaces - local, global, enclosing, built-in, module

- other types of namespace - global, local, class, instace

- suppose self(init or apssed to any othe method), and some new variable/existing defined inside a FUNCTION becomes local namespace

```

college_name = "ABC University" #global ns

class Student: # global ns

    college = "IIT" #class ns

    def __init__(self, name, age): #class ns
        self.name = name #instance ns
        self.age = age #instance ns

    def display(self): #class ns
        message = "Student Details" #local ns
        print(message)
        print(self.name)
        print(self.age)
        print(self.college)


s1 = Student("Rahul", 21) # global ns
s2 = Student("Priya", 22) #global ns
print(vars(s1))
print(s1.__dict__)
```

### accessing attributes
- s1.college - if attr not found in s1 instance namespac, it checks in its class namespace first 
- also a class namespace cant access its instance namespace but vice versa is possible cos of the above point on hierarchy of checking


### modifying attributes
- now for modification exceptoin case is -> s1.college ='mit' changes onyl s1 instance namespace value of college wihtotu affecting colllege of other obj (affecting others would be bad, if you want overall change call it with classname.attr)
another exception si that: suppose s1.college ='mit', AND collelg attr not in s1 namespace but it is ther in class namespae, -> then it is created in s1 anemspace instead of modifying class attr -> (attritbute shadowing so it doesnt affect other objects, however again if you did Student.college='mit' it would change for all objects obvisously)

- to remove the natural override of instance attr over the class attr u must remvoe th instace attr for that instace by del s1.college

- s1.display() -> is actually Student.display(s1) IF display is defined actually in the class and not in the object. again it searches in instnace if not it searches in class namespace

### mutable attr vs instance attr

Lookup & Shadowing work the exact same way for everything (Python always checks the instance namespace first, then falls back to the class).

The Catch: Assignment (=) always creates/updates an instance attribute and shadows the class attribute. In-place mutation (.append(), .remove()) on a class attribute modifies the shared object directly **UNLESS** that instance has already shadowed it with its own separate object.

- chanding lets say Student.subjectsList =[..] will change it only for those objects taht dont have their own SubjectsList

### Object creation and memory

- only when we ahve some **requried** essential information from an Object then we need to take it sproperties at time of object creation only, so use  __init__
- custom object without __init__ is possible but with __new__
- so s1=Student() is basicalyl working by callin __new__ then calling __init__ if tehre are some importnat  initial requried proeprties whose valeus need to be intiialized
- so the global namespace s1 is now referrign toe the instance namespace attr like name and age
- return self allows method chaining and fluent APIs

### Scope and name resolution

If you write print(college) inside display(), Python checks:Local scope (display variables) $\rightarrow$ Not found.Enclosing scope (none) $\rightarrow$ Skipped.Global scope (module level) $\rightarrow$ Looks for a global variable named college. If it's not there, it crashes with a NameError.It completely skips the class namespace (college = "IIT").  thats why we need that self.college or Student.college to tell PYthon we are referring to somehting in class or instanc enamespace and not somethign in lexical textual scope

### getter and setter


### static instance and class methods

- normall we call calss emthod htrought class and instace method throught object
- bUT we can call a class emthdo thrught instance however it takes onyl the cls as argument anyway - s1.class_method()
- we can instanc emethdo throgh class IF we pass object as sargumetn fo r the self : Student.display(s1)
- the decorator tell pyhton that it belogns to class method, and automaticall pass addres of cls
- suppose our data to create objects come form a file/webAPI/json?SQL now we cant send directly to init thoses tring.
so we can create an alternative constructor that splits based on',' and then call the constructor:
```
# Alternative constructor example using a class method:
    @classmethod
    def from_string(cls, data_str):
        """Parses a comma-separated string like 'Rahul,21' to create a Student object."""
        name, age = data_str.split(",")
        return cls(name, int(age))
```



