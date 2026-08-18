# Computational Thinking Exercise
## [Smart Vending Machine]
**Name: Roque Medin**

**Section: Magnesium**

**Last Name: Nicolas**

**Date: 08/18/2026** 

---

## Step 1: Identify the Big Problem
### Main Problem
Vending machines need to operate efficiently and accurately by giving students the correct item, calculating the correct change, monitoring item availability, and handling multiple users quickly

---
## Step 2: Identify the Sub-Problems
1. *Incorrect Change* - The machine sometimes gives out the wrong amount of change after a student pays

2. *Items Running Out* - The machine  does not detect or notify staff when snacks or drinks are out of stock

3. *Wrong Item Selection* - Students may press the wrong button and receive an item they did not want

4. *Item Does Not Fall* - Sometimes the selected item does not fall from the machine even after the student has paid and selected it
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Incorrect Change | Algorithmic Thinking | Calculate the change by subtracting the item price from the amount paid.  |
| Items Running Out | Pattern Recognition | Monitor inventory and notify staff when an item is low or out of stock. |
| Wrong Item Selection | Decomposition | Separate the process into selecting, confirming, and dispensing the item. |
| Item Does Not Fall | Algorithmic Thinking | Break the dispensing process into steps: check payment → check item → activate motor → check if item falls → notify the user if it gets stuck. |

---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Sub-Problem 4 - Item Does Not Fall
### Pseudocode

    START

    Student selects an item
    Check if item is available

    IF payment is enough THEN
        Activate the dispensing motor
        Check if the item falls

        IF item falls THEN
            Give the item to the student
            Return the correct change
        ELSE
            Display "Item is stuck"
            Return the student's money
        END IF

    ELSE
        Display "Insufficient money"
    END IF
    ELSE
        Display "Item is out of stock"
    END IF

    END

---
