# SG4 - Understanding Classes and Objects
## Context

 Video Game

## Class Name

InventoryItem

## Class Description

An InventoryItem represents an item that is stored in the player’s inventory. It stores information about the item and can perform actions involving it.

## Properties
| Property | Data Type | Description |
|---|---|---|
|ItemName|string |Name of the item |
|Quantity |int |Amount of the item you own |
|Price |double |Value of the item |
|IsUsable|boolean |Shows whether item can be used or not |
## Methods
| Method | Description |
|---|---|
|addItem(amount:int) |Adds a number of items into the inventory |
|useItem() |Uses the item and decreases the quantity of the item|
|displayInfo() |displays the information of the item |
## Class Diagram
![Class Diagram](images/classDiagram.png)
## Design Explanation
### Why did you choose this class?

I chose this class because inventory systems are simple to represent using properties and methods.

### Which property is the most important? Why?

I think that ItemName is the most important property because it shows the player what the item is and its name.

### Which method is the most useful? Why?

UseItem is the most useful method as it allows the player to actually use the item from their inventory.
