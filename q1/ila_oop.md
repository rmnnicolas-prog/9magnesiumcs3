# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation

We can apply encapsulation by creating a *Product* object that groups the product's name, price, and quantity together with methods such as addStock(), removeStock(), and displayInfo(). Doing this instead of having separate variables like name1, price1, and quantity makes the inventory more organized by making each product object contain its own related properties and actions. 

### 2. Abstraction

Abstraction can be used if the inventory system can give the user simple methods like addProduct(), removeProduct(), and displayProducts() without showing them everything happening in the background . For example, the user can use removeProduct() without needing to know exactly how the program handles finding the product and updating it. This makes the inventory system simpler to use because it hides the unnecessary implementation details. 

### 3. Inheritance

For inheritance, it can be applied if the sari-sari store has different types of products that share common information. There could be a general Product class that would contain properties such as name, price, and quantity. Classes such as FoodProduct and DrinkProduct could inherit these properties and methods. This means we don't have to write the same code again for every type of product. 

### 4. Polymorphism

Polymorphism will be useful when different types of products have different ways to behave in their own way while using the same method. For instance, both FoodProduct and DrinkProduct could use displayInfo(), but the information shown could be different for each one. The program can still use the same method name even though the result depends on what type of product it is.

## Reflection
I think encapsulation would be the most useful for the sari-sari store inventory system. It would keep the name, price, and quantity of each product together instead of having many separate variables. It also makes it easier to update the stock using methods like addStock() and removeStock(). Overall, I think this would make the inventory much more organized and easier to manage.
