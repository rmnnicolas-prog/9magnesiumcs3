# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
A game inventory system that manages different items. The inventoryItem stores information about each item while the Inventory stores them.
## Inheritance Relationship
Parent: inventoryItem
Child: Iron Sword
Explanation: An iron sword is an inventoryItem. It can reuse the attributes and methods of InventoryItem, but will also have its own damage attribute.
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation
Explanation: The Inventory stores inventoryItems but items can exist without the inventory. The Inventory only recieves already-made items.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
