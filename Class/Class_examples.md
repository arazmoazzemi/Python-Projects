### Class_Examples:


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
