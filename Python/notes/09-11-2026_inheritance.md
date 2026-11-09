### INHERITANCE (Finally)

- Child class is jsut a more specfiic form of super class. it holds the parent classes in Child.__bases__
- Parent class attr are NOT simply copied to chidl class namespace BUT rather child class can access parent class attr ebcause of the search throguht its hierarchy
- thats why child.__dict__ doesnt show the paretn class attr inside it!

- No Namespace Copying: Inheritance is a lookup path (__mro__), not a duplication process. Child.__dict__ stays lean.
- Parent class can actually acces Child class attr! - with the help of self
- lets say Parent ahs familyname attr. but if i careate CHild.familyname attr it will eb created in instance space and overrides by MRO/ willbe accesed first

- super().__init__(name) clals the NEXT  __init__ in the MRO

- be careful with-
 1.instance assignemtn
2. class assignment
3. super class assignment

- isinstance(obj, cls): Returns True if the object is of the specified type. It is preferred over type(obj) == cls because it accounts for inheritance. It is used to verify the type of an object. 
- hasattr(obj, name): Returns True if the object has an attribute with the given string name. It works by calling getattr() and catching AttributeError. It is used to verify the existence of an attribute

# single level

consider:
```
class Animal:
	def __init__(self, name):
		self.name = name


class Dog(Animal):
	def __init__(self, name, breed):
		super().__init__(name)
		self.breed = breed


d1 = Dog("Tommy", "Labrador")
```

- we could have written this basically as self.name and result world be same but writing ti this way what changes is that you dont repeat all that intialization - DRY principle

- here name is a pparent class isntance attribute
-  jsut follow the MRO and anmespaces

# multi level 
- just the MRO chain is extended
- best to keep levels up to 3 max industry standard
- super() to go up the hierarchy
- at each level super()._init__ cos we ened to init
- debuggn is hard, if yu change aparametrers of one inti class youll ahve to change it on all classes
 thats why go with *args, **kwargs for any additional parameters that are liekly to change or receive
 ```
 class Animal:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)  # Keeps the super chain alive safely
```

- note: still Puppy.__dict__ contains only its class attr not inheritred class attr
 
# multiple

- in single leve, super() goes to parent, and in multiple, super() goes to the next class in MRO
- MRO search for first mentioned Parent calss, if nto found then the next and so on in the order mentioned in the class declaration
- to stop this and calle explicity use: SecondClass.method(c1)

- inti will ALSO need to change cos now you ahve to do intialize for both class so we do this-
```
def __init__(self, surname, language, age):
        
        self.age = age
        # Cooperative call: triggers MRO sequence across BOTH parents
        super().__init__(surname=surname, language=language)
        
```

### important : diamond problem


You might wonder: *“Why can’t I just write two explicit constructor calls inside `Child.__init__`, like this?”*

```python
class Child(Father, Mother):
    def __init__(self, surname, language, age):
        Father.__init__(self, surname)  # Call 1
        Mother.__init__(self, language)  # Call 2
        self.age = age

```

The short answer is: **Yes, you *can* do that, but it introduces a massive trap known as the "Diamond Problem" and duplicate initialization.**
- if those lasses have further initn methods, then that suepr init methdos will eb called twice once by Fathre andonce b Mother
- If `Human` initializes a database connection, resets a counter, or allocates expensive resources, running it twice can corrupt your object's state or cause silent bugs.
---


- You might wonder: What about writing two `super()` calls?


```python
class Child(Father, Mother):
    def __init__(self):
        super().__init__()  # Calls Father
        super().__init__()  # Calls Father AGAIN (restarts MRO lookup)

```

This fails because `super()` does not mean *"call the next parent in the list.".  Calling it twice just triggers the exact same first parent twice.

---

#### Why Cooperative `super()` Solves This

When *every* class in the hierarchy uses cooperative `super()` (passing arguments up the MRO chain), Python ensures that **each class in the diamond graph is visited exactly once**, in the exact order specified by the MRO (`Child` $\rightarrow$ `Father` $\rightarrow$ `Mother` $\rightarrow$ `Human`).

```python
class Human:
    def __init__(self, **kwargs):
        print("-> Human.__init__ running")
        super().__init__(**kwargs)

class Father(Human):
    def __init__(self, surname, **kwargs):
        print("-> Father.__init__ running")
        self.surname = surname
        super().__init__(**kwargs)  # Seamlessly steps up to Mother/Human

class Mother(Human):
    def __init__(self, language, **kwargs):
        print("-> Mother.__init__ running")
        self.language = language
        super().__init__(**kwargs)

class Child(Father, Mother):
    def __init__(self, surname, language, age):
        print("-> Child.__init__ START")
        self.age = age
        super().__init__(surname=surname, language=language) # Triggers the entire chain cleanly once!
        print("-> Child.__init__ END")

```

#### Summary Rule of Thumb:

* **Explicit calls (`Parent.__init__(self)`)**: Fine *only* if the parents are 100% independent and will never share a common base class.
* **Cooperative `super()**`: Mandatory if your multiple inheritance hierarchy forms a diamond or needs predictable, single-execution initialization chains.


# HIERARCHICAL INHERITANCE

- the diff objects are indepenedent cnanot mdoify or access each others properties, except by itself
- if in n child classes one child class overrides parent class method OR changes parent class attr. that parent class attr gets changed for all object of that child class onyl and NOT for the sibling classes 

- error scenarios:
1. if parent class attr is mutable it will affect sibling child classes when modified - same address shared


# Hybrid inheritance
- MRO is important to find the order


# QUESTIONS for interview
### define
### whys
### scaenarios
### real world examples
### code