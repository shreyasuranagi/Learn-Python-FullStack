# Class and object

- Inheritanc emethods cna be thoguht of button/ui on an interface that change the state/perform action of an object. each state has some values that also get changed with state. intiial values are also there
- soo any real world object we have can be basically  divided into 3 parts: 
1. what are the properties it has with values - fixed values (not state) + changeable values (state)
2. what action we can do on it/ how we cna change the state(how to change these values)
3. resulting state(values)based on each action/change of state 
- smartdevice : initial state -off,not connected, 0deg
smartbulb: state = on/off, switchOn(), switchOff() , result=on
smartFridge: temp=25deg, cool(), warm(), result=temp=10
smartTV: channel=0, changeChannel() , result -channl=5

- tip: to model  a class and object tis best ot use or think in terms of what action are to be done first

### how to think of inheritance?

- Iheritance is an IS-A relation
- Inheritance is like a - type of relation. bike isa type of Vehicle, BUsiness accoutn si a type of account
- what if an object is made of another component inside of it? where that coponenet can also be modeled as an object which has aforementioned state and actions that change its state etc? Solution: Compositon, not Inheritance
- what goes to class attr - shared constant values
- what goes to obj attr - unshared dynamic values

