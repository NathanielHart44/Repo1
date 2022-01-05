from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Fun with images")
root.iconbitmap("c:/Downloads/cheese_icon.ico")
button_quit = Button(root, text="Exit Program", command=root.quit)

my_image = ImageTk.PhotoImage(Image.open("Mareena_lecture.jpg"))
my_image_container = Label(image=my_image)
my_image_container.grid(row=0, column=0)

button_quit.grid(row=1, column=0)
root.mainloop()
