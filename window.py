from tkinter import *
from tkinter.ttk import Combobox
window=Tk()

photo = PhotoImage(file="doge.png")
imgLabel = Label(image=photo)
imgLabel.pack(side=TOP)

var = StringVar()
var.set("doge")
data=("doge", "cheems", "shiba", "dog")
cb=Combobox(window, values=data)
cb.place(x=60, y=150)

lb=Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=250, y=150)

v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="dog", variable=v0,value=1)
r2=Radiobutton(window, text="cat", variable=v0,value=2)
r1.place(x=100,y=50)
r2.place(x=180, y=50)
                
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "doge", variable = v1)
C2 = Checkbutton(window, text = "shibainu", variable = v2)
C1.place(x=100, y=100)
C2.place(x=180, y=100)




btn = Button(window, text = 'Click me')
btn.pack(side = 'top') 

window.title('window example')
window.geometry("400x250+10+10")
window.mainloop()