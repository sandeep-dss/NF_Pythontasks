from tkinter import *

root = Tk()

frame1 = Frame(root)

root.title("UI Frame")
label= Label(frame1,text="Frame Example",justify=CENTER)
label.pack(side=BOTTOM)
frame1.pack(padx=4,pady=4)

photo = PhotoImage(file="doge.png")
imgLabel = Label(root, image=photo)
imgLabel.pack(side=TOP)


root.mainloop()