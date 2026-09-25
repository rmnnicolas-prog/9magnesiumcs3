class InventoryItem:
    def __init__(self, itemName, quantity, price, isUsable):
        self.itemName = itemName
        self.isUsable = isUsable
        self.__quantity = quantity
        self.__price = price

    def addItem(self, amount):
        self.__quantity += amount

    def useItem(self):
        if self.__quantity > 0 and self.isUsable:
            self.__quantity -= 1

    def displayInfo(self):
        print("Item:", self.itemName)
        print("Quantity:", self.__quantity)
        print("Price:", self.__price)
        print("Usable:", self.isUsable)


class Weapon(InventoryItem):
    def __init__(self, itemName, quantity, price, isUsable, damage):
        super().__init__(itemName, quantity, price, isUsable)
        self.damage = damage

    def displayInfo(self):
        super().displayInfo()
        print("Damage:", self.damage)


class Inventory:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def displayItems(self):
        for item in self.items:
            item.displayInfo()


inventory = Inventory("Player Inventory", 10)

item1 = InventoryItem("Health Potion", 5, 50.0, True)
item2 = InventoryItem("Mana Potion", 3, 75.0, True)

weapon1 = Weapon("Iron Sword", 1, 500.0, False, 25)

print("--- INHERITANCE TEST ---")
print("Weapon name:", weapon1.itemName)
print("Weapon damage:", weapon1.damage)

print("\n--- AGGREGATION TEST ---")

inventory.addItem(item1)
inventory.addItem(item2)
inventory.addItem(weapon1)

print("Inventory:", inventory.name)
print("Items in inventory:")

inventory.displayItems()
