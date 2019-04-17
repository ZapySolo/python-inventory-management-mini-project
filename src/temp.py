from tkinter import *
from src.manage_inventory import ManageInventoryScreen
from src.customer_cart_screen import CustomerCartScreen


class SelectionScreen:
    def __del__(self):
        print('SelectionScreen Object destroyed...')

    def __init__(self, root):
        self.root = root

        self.stat = "this gives the detail information \nabout the profit made in the\n course of one month and also " \
            "\nas per day"
        self.update = "this screen contains functions \nto add new items to your \ninventory as well update " \
            "\nexisting items"
        self.cart = "this scree contains the functions \nsuch as to add the items in coustomer \ncart which will be " \
            "updated in\n the inventory document"

        self.frm_update = Frame(root, height=400, width=300)
        self.frm_stat = Frame(root, height=400, width=300)
        self.frm_cart = Frame(root, height=400, width=300)

        self.lbl_update = Label(self.frm_update, text="Update Inventory")
        self.lbl_stat = Label(self.frm_stat, text="Statistic")
        self.lbl_cart = Label(self.frm_cart, text="Cart")

        self.lbl_update_des = Label(self.frm_update, text=self.update)
        self.lbl_stat_des = Label(self.frm_stat, text=self.stat)
        self.lbl_cart_des = Label(self.frm_cart, text=self.cart)

        self.btn_update = Button(self.frm_update, text="Manage", command=self.onPressManage, height=2, width=10)
        self.btn_stat = Button(self.frm_stat, text="Statistic", command=self.onPressStat, height=2, width=10)
        self.btn_cart = Button(self.frm_cart, text="Cart", command=self.onPressCart, height=2, width=10)

        self.btn_back_to_statistic_from_manage_inventory = Button(root, text="Back", command=self.onPressBackToStatisticFromManageInventory, height=2, width=10)
        self.btn_back_to_statistic_from_customer_cart = Button(root, text="Back", command=self.onPressBackToStatisticFromCustomerCart, height=2, width=10)

        self.manage_inventory = ManageInventoryScreen(self.root)
        self.customer_screen = CustomerCartScreen(self.root)

        self.manageimg = PhotoImage(file="asset/manage.png", height=200, width=200)
        self.lbl_manage_inventory_image = Label(self.frm_update, image=self.manageimg)

        self.statimg = PhotoImage(file="asset/stat.png", height=200, width=200)
        self.lbl_stat_image = Label(self.frm_stat, image=self.statimg)

        self.cartimg = PhotoImage(file="asset/cart.png", height=200, width=200)
        self.lbl_cart_image = Label(self.frm_cart, image=self.cartimg)

    def _place(self):
        self.frm_update.place(relx=0.025, rely=0.16)
        self.frm_stat.place(relx=0.35, rely=0.16)
        self.frm_cart.place(relx=0.675, rely=0.16)

        self.lbl_update.place(relx=0.05, rely=0.1)
        self.lbl_update.config(font=("Courier", 25))
        self.lbl_manage_inventory_image.place(relx=0.13, rely=0.18)

        self.lbl_stat.place(relx=0.25, rely=0.1)
        self.lbl_stat.config(font=("Courier", 25))
        self.lbl_stat_image.place(relx=0.15, rely=0.18)

        self.lbl_cart.place(relx=0.4, rely=0.1)
        self.lbl_cart.config(font=("Courier", 25))
        self.lbl_cart_image.place(relx=0.13, rely=0.18)

        self.lbl_update_des.place(relx=0.14, rely=0.7)
        self.lbl_stat_des.place(relx=0.14, rely=0.7)
        self.lbl_cart_des.place(relx=0.07, rely=0.7)

        self.btn_update.place(relx=0.35, rely=0.91)
        self.btn_stat.place(relx=0.35, rely=0.91)
        self.btn_cart.place(relx=0.35, rely=0.91)

    def _selection_forget(self):
        self.frm_update.place_forget()
        self.frm_stat.place_forget()
        self.frm_cart.place_forget()

        self.lbl_update.place_forget()
        self.lbl_stat.place_forget()
        self.lbl_cart.place_forget()

        self.lbl_update_des.place_forget()
        self.lbl_stat_des.place_forget()
        self.lbl_cart_des.place_forget()

        self.btn_update.place_forget()
        self.btn_stat.place_forget()
        self.btn_cart.place_forget()

        self.lbl_manage_inventory_image.place_forget()
        self.lbl_stat_image.place_forget()
        self.lbl_cart_image.place_forget()
    def onPressStat(self):
        print("Not implemented yet...")

    def onPressManage(self):
        self._selection_forget()
        self.manage_inventory._place()
        self.btn_back_to_statistic_from_manage_inventory.place(relx=0, rely=0)

    def onPressCart(self):
        self._selection_forget()
        self.customer_screen._place()
        self.btn_back_to_statistic_from_customer_cart.place(relx=0, rely=0)

    def onPressBackToStatisticFromManageInventory(self):
        self._place()
        self.manage_inventory._placeForget()
        self.btn_back_to_statistic_from_manage_inventory.place_forget()

    def onPressBackToStatisticFromCustomerCart(self):
        self._place()
        self.customer_screen._placeForget()
        self.btn_back_to_statistic_from_customer_cart.place_forget()


if __name__ == '__main__':
    root = Tk()
    selection = SelectionScreen(root)
    selection._place()
    root.title("Inventory Management")
    root.configure(bg="red")
    root.minsize(height=600, width=1000)
    root.maxsize(height=600, width=1000)
    root.mainloop()
