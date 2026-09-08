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


item1 = InventoryItem("Health Potion", 5, 50.0, True)
item2 = InventoryItem("Iron Sword", 1, 500.0, False)


print("--- BEFORE ---")
print("Object 1:")
item1.displayInfo()

print("\nObject 2:")
item2.displayInfo()


print("\nUsing one Health Potion...")
item1.useItem()


print("\n--- AFTER ---")
print("Object 1:")
item1.displayInfo()

print("\nObject 2:")
item2.displayInfo()
