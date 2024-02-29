### Class_Examples:


Creat objects and  mappingproxy

```
from colorama import Fore, Back, Style

class Peykan:
    color = 'red'

print(Peykan.color)
print(Fore.GREEN + 'model' + Fore.RESET, Peykan.__dict__)

Peykan.medel = 'Javanan'
Peykan.doors = 4

print(Peykan.__dict__)

p1 = Peykan()
p1.color = 'black'
print(p1.color)
print(Fore.RED + 'P1' + Fore.RESET, Peykan.__dict__)

```

Method and function

```
class Peykan:
    color = 'red'

    def drive(self):
        return f"Peykan is driving -> {self}"

print(Peykan.drive)

p1 = Peykan()
print(p1.drive())

p2 = Peykan()
print(p2.drive())

print(type(Peykan.drive))
print(type(p1.drive))
```

Set and get attributes / Static methods and class methods / __ init __

```
class Peykan:
    color = 'red'
    doors = 4

    def drive(self):
        return f"Peykan is driving --> {self}"

p1 = Peykan()

# getattr(p1, 'color')
print(getattr(p1, 'color'))

setattr(p1, 'color', 'black')
print(p1.color)

list_obj = [Peykan() for _ in range(2)]
variables = ['color', 'doors']
values = ['blue', 2]

for obj in list_obj:
  for variables, vlaue in zip(variables, values):
      setattr(obj, variables, vlaue)

print(list_obj[0].doors)

# Instead of using TRY and EXCEPTION
print(getattr(p1, 'tires', 'Tires Not Found'))
```
### __ int __
```
class Peykan:
    color = 'red'
    doors = 4

    def __init__(self, color='red'):
        self.color = color

    def drive(self):
        return f"Peykan is driving --> {self}"

p1= Peykan(color='blue')

print(p1.color)
```

### Static method and class method
```
```

















