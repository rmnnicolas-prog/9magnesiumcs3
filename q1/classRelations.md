# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: inventoryItem

Description: An InventoryItem represents an item that is stored in the player’s inventory. It stores information about the item and can perform actions involving it.
## New Related Class
Class: Inventory
Description: It represents the player's collection of items. It includes the item's name, description, and whether it can be used.
## Association
Relationship: Inventory contains inventoryItem
Explanation: The Inventory class is connected to the inventoryItem class because an inventory can hold multiple items.
## Multiplicity

Multiplicity: Inventory 1 ───────── 0..* inventoryItem
Explanation: One Inventory can contain zero or multiple inventoryItems
## UML Class Relationship Diagram
![Class Relationship Diagram](Images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](Images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](Images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
An Inventory can store multiple inventoryItems that are added to it.
### What multiplicity did you choose and why?
I chose the zero or more (0..*) multiplicity because and inventory can be empty or hold many items.
### How did you implement the relationship in Python?
I used a list called items inside the Inventory class. The addItem() method adds an InventoryItem object to the list. This stores the actual objects instead of just their names.
### Why did you store an object reference instead of copying its data?
So the inventory can access and use the item's methods and current information.
### If your relationship uses many, why is a list appropriate?
It is appropriate because it can store multiple item objects at the same time.
