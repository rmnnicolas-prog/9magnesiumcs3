# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](q1/classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| itemName| string| Public| The item's name must  be seen by the program|
| isUsable| boolean| Public| The program needs to check if the item can be used|
| quantity| int| Private| Should only be changed by the item's methods|
| price| double| Private| Prevents the price from being changed directly|
## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
I the quantity attribute private because it should only be changed by the methods like useItem() or addItem().
### Which method changes the state of your object?
The useItem() method changes the state of my object. It changes the quantity by decreasing the item by one when it is used.
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
