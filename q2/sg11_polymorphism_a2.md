# Polymorphism Activity 2
## Roque Medin Nicolas
## 9_Magnesium


### 1.  According to the video, duck typing allows objects to be treated as if they are a different type as long as they meet the minimum necessary attributes and methods. The video also states that it is another way to achieve polymorphism besides inheritance.

### 2.
``` Python
class Car:
    def move(self):
        print("The car drives on the road")
        
class Boat:
    def move(self):
        print("The boat sails on water")

class Drone:
    def move(self):
        print("The drone flies in the air")
        
def start_trip(vehicle):
    vehicle.move()
    
c1 = Car()
b1 = Boat()
d1 = Drone()

start_trip(c1)
start_trip(b1)
start_trip(d1)

```

### 3. The code demonstrates polymorphism because even though the classes have the same move() method, they each produce a different outcome depending on the object. Car, Boat, and Drone all have different versions of the method and that allows the start_trp() function to work without any problems.
