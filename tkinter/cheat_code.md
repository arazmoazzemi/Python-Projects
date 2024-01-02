
```
import tkinter as tk
window = tk.Tk()
{

}
window.mainloop()
```
### Examples:
## 01
Example of Create Windows:
```
# window.configure(bg='green', cursor='')
# window.geometry("500x500+200+200")
# window.title("Test Windows")
# window.resizable(width=False, height=False)
# window.maxsize(width=500, height=500)
```
---

## 02
Exmaple of Show messages:
```
# messagebox.showerror('Error', 'Please')
# messagebox.showinfo("Error", "Info", parent=window)
# messagebox.askquestion("ASK", "Do you want to")
# messagebox.askokcancel("ASK", "Do you want to")
# messagebox.askyesnocancel('ASK', 'Do you want to')
```
## 03
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

## 04
Button examples:
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

## 05
Label example:
```

label = tk.Label(master=window, text="label1",width=10, height=2, fg="red", bg="yellow", font=("Arial, 10"), underline=1, anchor=CENTER)
label.pack()
# label.place(x='30', y='40')


```
---
## 06
Events examples:

#### 06-01 : Mouse events:
```
import tkinter as tk
from tkinter import *


windows = tk.Tk()
windows.title("Face")
windows.geometry("500x500")
windows.resizable(width=False, height=False)

button = tk.Button(windows, text="click me")
button.pack()
def print_button(event):
    print("event printed")

button.bind('<Button-1>', print_button)
# ---
# button.bind('<Button-1>', print_button)
# button.bind('<Button-2>', print_button)
# button.bind('<Button-3>', print_button)
# ---
# button.bind('<ButtonRelease-1>', print_button)
# button.bind('<ButtonRelease-2>', print_button)
# button.bind('<ButtonRelease-3>', print_button)
# ---
# button.bind('<MouseWheel>', print_button)
# ---
# button.bind('<Enter>', print_button)
# ---
button.bind('<Leave>', print_button)
# ---
button.bind('<Double-Button-1>', print_button)
button.bind('<Double-Button-2>', print_button)
button.bind('<Double-Button-3>', print_button)

```

#### 06-02: Keyboard events:
```




```




windows.mainloop()





```


