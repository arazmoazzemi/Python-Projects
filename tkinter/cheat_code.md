### Tkinter cheat codes:

---

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

windows.mainloop()
```

#### 06-02: Keyboard events:
```
# windows.bind("<Key>", print_button)
# windows.bind("<Return>", print_button)
# windows.bind("<Tab>", print_button)
# windows.bind("<a>", print_button)
# windows.bind("<Up>", print_button)
# windows.bind("<BackSpace>", print_button)
# windows.bind("<F1>", print_button)
# windows.bind("<Shift-Up>", print_button)

```

---

## 07
#### Input Values:

#### Simple Entry:
```
import tkinter as tk
from _ast import Return
from tkinter import *

window = tk.Tk()
window.title("Face")
window.geometry("500x500")
window.resizable(width=False, height=False)

inp_entry = Entry(master=window, width=10, bg="yellow", fg="black", bd=2, cursor='hand2', font=("Helvetica"), selectbackground='green', selectforeground='blue' )
inp_entry.pack()
def print_entry(events):
     print("Test Entry")

window.bind('<Return>', print_entry)
window.mainloop()

```


#### Delete :
```
import tkinter as tk
from _ast import Return
from tkinter import *

window = tk.Tk()
window.title("Face")
window.geometry("500x500")
window.resizable(width=False, height=False)

inp_entry = Entry(master=window, width=10, bg="yellow", fg="black", bd=2, cursor='hand2', font=("Helvetica"), selectbackground='green', selectforeground='blue' )
inp_entry.pack()
def print_entry(events):
    inp_entry.delete(1, 4)

window.bind('<Return>', print_entry)

window.mainloop()

```
#### Print Input:
```
import tkinter as tk
from _ast import Return
from tkinter import *

window = tk.Tk()
window.title("Face")
window.geometry("500x500")
window.resizable(width=False, height=False)

inp_entry = Entry(master=window, width=10, bg="yellow", fg="black", bd=2, cursor='hand2', font=("Helvetica"), selectbackground='green', selectforeground='blue' )
inp_entry.pack()
def print_entry(events):
    print(inp_entry.get())


window.bind('<Return>', print_entry)

window.mainloop()

```
### Move Cursor:
```
import tkinter as tk
from _ast import Return
from tkinter import *

window = tk.Tk()
window.title("Face")
window.geometry("500x500")
window.resizable(width=False, height=False)

inp_entry = Entry(master=window, width=10, bg="yellow", fg="black", bd=2, cursor='hand2', font=("Helvetica"), selectbackground='green', selectforeground='blue' )
inp_entry.pack()
def print_entry(events):
    inp_entry.icursor(3)


window.bind('<Return>', print_entry)

window.mainloop()
```
#### Move Cursor befor Enter your
```
import tkinter as tk
from _ast import Return
from tkinter import *

window = tk.Tk()
window.title("Face")
window.geometry("500x500")
window.resizable(width=False, height=False)

inp_entry = Entry(master=window, width=10, bg="yellow", fg="black", bd=2, cursor='hand2', font=("Helvetica"), selectbackground='green', selectforeground='blue' )
inp_entry.pack()
def print_entry(events):
    inp_entry.insert(3, 'Enter your')


window.bind('<Return>', print_entry)

window.mainloop()
```

### Slect input valuse to {3} characters

```
import tkinter as tk
from _ast import Return
from tkinter import *

window = tk.Tk()
window.title("Face")
window.geometry("500x500")
window.resizable(width=False, height=False)

inp_entry = Entry(master=window, width=10, bg="yellow", fg="black", bd=2, cursor='hand2', font=("Helvetica"), selectbackground='green', selectforeground='blue' )
inp_entry.pack()
def print_entry(events):
    inp_entry.select_to(3)


window.bind('<Return>', print_entry)

window.mainloop()
```

### Select range of input valuse, From start to end of charactes:

```
import tkinter as tk
from _ast import Return
from tkinter import *

window = tk.Tk()
window.title("Face")
window.geometry("500x500")
window.resizable(width=False, height=False)

inp_entry = Entry(master=window, width=10, bg="yellow", fg="black", bd=2, cursor='hand2', font=("Helvetica"), selectbackground='green', selectforeground='blue' )
inp_entry.pack()
def print_entry(events):
    inp_entry.select_range(start=1, end=5)


window.bind('<Return>', print_entry)

window.mainloop()
```
### Return boolean valuse

```
import tkinter as tk
from _ast import Return
from tkinter import *

window = tk.Tk()
window.title("Face")
window.geometry("500x500")
window.resizable(width=False, height=False)

inp_entry = Entry(master=window, width=10, bg="yellow", fg="black", bd=2, cursor='hand2', font=("Helvetica"), selectbackground='green', selectforeground='blue' )
inp_entry.pack()
def print_entry(events):
    print(inp_entry.select_present())


window.bind('<Return>', print_entry)

window.mainloop()
```
---

### 08
### Text Editor
```
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Text Title")
window.geometry('500x500')
window.resizable(False, False)

txt = Text(master=window, width=50, height=30, bg='white', fg='red', font='Arial', wrap='word', bd=5, relief=SUNKEN, insertofftime=0, insertwidth=4)
# txt.insert(INSERT, 'Hello')
txt.pack()

window.mainloop()
```
---

### 09
### Radio Button
```
import tkinter as tk
from tkinter import *


window = tk.Tk()
window.title("Radio Button")
window.geometry("500x500")
var = IntVar()
radio_button_1 = tk.Radiobutton(master=window, text="yes", variable=var, value=1)
radio_button_2 = tk.Radiobutton(master=window, text="no", variable=var, value=2)
radio_button = Button(master=window, text="submit")

radio_button_1.pack()
radio_button_2.pack()
radio_button.pack()

def show_message(event):
    if(var.get() == 1):
        print("Yes")
    if(var.get() == 2):
        print("No")

radio_button.bind('<Button>', show_message)

window.mainloop()
```

---

### 10
### Check Button(CheckBox)
```
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Face")
window.geometry("500x500")

var1 = IntVar()
var2 = IntVar()

chkbox_01 = Checkbutton(window, text="one", variable=var1, onvalue=1, offvalue=0)
chkbox_02 = Checkbutton(window, text="two", variable=var2, onvalue=1, offvalue=0)

button = Button(master=window, text="submit")
def m(event):
    if (var1.get() == 1):
        print("one marked")
    if (var1.get() == 0):
        print("one unmarked")

    if (var2.get() == 1):
        print("one marked")
    if (var2.get() == 0):
        print("one unmarked")

button.bind("<Button>", m)


chkbox_01.pack()
chkbox_02.pack()
button.pack()
window.mainloop()


```
---


















