

import tkinter as tk

window = tk.Tk()

### Examples:

Example of Create Windows:
```
# window.configure(bg='green', cursor='')
# window.geometry("500x500+200+200")
# window.title("Test Windows")
# window.resizable(width=False, height=False)
# window.maxsize(width=500, height=500)
```

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




window.mainloop()
