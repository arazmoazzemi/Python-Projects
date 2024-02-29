### Class_Examples:


Creat objects and  mappingproxy

```
from colorama import Fore, Back, Style

class Peykan:
    color = 'red'

print(Peykan.color)
print(Fore.GREEN + 'model' + Fore.RESET, Peykan.__dict__)

Peykan.medel = 'Javanan'
Peykan.doors = '4'

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
```
