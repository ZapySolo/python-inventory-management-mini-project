from tkinter import *
from src.welcome_screen import WelcomeScreen

if __name__ == '__main__':
    root = Tk()
    root.title("Inventory Management")
    root.minsize(height=600, width=1000)
    root.maxsize(height=600, width=1000)
    manage = PhotoImage(file="asset/wallpaper.png")
    lbl_update_image = Label(root, image=manage).place(x=0, y=0)
    start = WelcomeScreen(root)
    start.welcome_pack()
    root.mainloop()
