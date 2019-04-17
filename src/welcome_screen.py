from tkinter import *
from src.login_screen import LoginScreen


class WelcomeScreen:
    def __del__(self):
        print('WelcomeScreen Object destroyed...')

    def __init__(self, root):
        self.footer_note = "this is an inventory management application. It can be use to update the inventory, add" \
            " new objects to the list, delete objects from the list\n, the other part of the application consists of" \
            " customer cart where you can add list into the customer\n cart and after submitting the list will be " \
            "updated to the database. currently the statistic screen has not been completed.\n The application starts" \
            " off with a typical signin of manager or the person who handles the inventory. \nusername->'root'\n" \
            "password->'root'."

        self.label_welcome_top = Label(root, text="S.E Comp - group 4")
        self.label_welcome_bottom = Label(root, text=self.footer_note)
        self.next_login_button = Button(root, text="Next->", height=2, width=10, command=self.onPressNext)
        self.login = LoginScreen(root)

    def welcome_pack(self):
        self.label_welcome_top.config(font=("Courier", 80))
        self.label_welcome_top.place(relx=0.05, rely=0.3)
        self.label_welcome_bottom.place(relx=0.05, rely=0.7)
        self.next_login_button.place(relx=0.91, rely=0)

    def welcome_pack_forget(self):
        self.label_welcome_top.place_forget()
        self.label_welcome_bottom.place_forget()
        self.next_login_button.place_forget()

    def onPressNext(self):
        self.welcome_pack_forget()
        self.login._pack()

    def onPressBackToWelcomeScreenFromLogin(self):
        self.login._place_forget()
        self.welcome_pack()
