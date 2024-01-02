
```
import tkinter as tk
window = tk.Tk()
{

}
window.mainloop()
```
### Examples:

Example of Create Windows:
```
# window.configure(bg='green', cursor='')
# window.geometry("500x500+200+200")
# window.title("Test Windows")
# window.resizable(width=False, height=False)
# window.maxsize(width=500, height=500)
```
---

Exmaple of Show messages:
```
# messagebox.showerror('Error', 'Please')
# messagebox.showinfo("Error", "Info", parent=window)
# messagebox.askquestion("ASK", "Do you want to")
# messagebox.askokcancel("ASK", "Do you want to")
# messagebox.askyesnocancel('ASK', 'Do you want to')
```

Message Example:
```
result = messagebox.askyesnocancel('ASK', 'Do you want to')

if result is True:
    messagebox.showinfo('Result Is True', 'True')
elif result is False:
    messagebox.showinfo('Result Is False', 'False')
else:
    messagebox.showerror('Result Is Canceled', 'Canceled')

```
---

Button examoes:
```
btn = Button(master=window, text="click me", width=10, height=2, bd=4, fg="blue", bg="yellow", activebackground="red")




# btn.pack(fill='x')
# btn.pack(fill='y', expand=True)
# btn.grid(column=2, row=2)
# btn.place(x=200, y=350)

```
Button examle:
```
import tkinter as tk
from tkinter import Button
window = tk.Tk()
window.title("Face")
window.geometry("500x500+200+200")

def print_test():
    print("Hello")

btn = Button(master=window, text="click me", width=10, height=2, bd=4, fg="blue", bg="yellow", activebackground="red", command=print_test)

btn.place(x=200, y=350)

tk.mainloop()
```
Button exampe:
```
import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title("Face")
window.geometry("500x500+200+200")

def print_test():
    print("Hello")

button = Button(master=window, text="click me", command=print_test, height= 35, width=70)
img = PhotoImage(file='click-here-button-icon.png')
button.config(image=img)
button.pack()
button.place(x=200, y=350)

tk.mainloop()
```

Label example:
```





```


