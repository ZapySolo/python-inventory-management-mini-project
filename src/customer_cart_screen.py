from tkinter import *
from src.business_logic import BackendLogic
import datetime


class CustomerCartScreen:
    def __init__(self, root):

        self.db_logic = BackendLogic()

        self.customer_name = StringVar()
        self.customer_mobile = StringVar()
        self.product_name = StringVar()
        self.product_quantity = IntVar()

        self.frm_cart = Frame(root, height=500, width=475)
        self.frm_list = Frame(root, height=500, width=300)
        self.list = Frame(self.frm_list, height=400, width = 275)

        self.cart_label = Label(self.frm_cart, text="Cart", font="Helvetica 30 bold")
        self.list_label = Label(self.frm_list, text="List", font="Helvetica 30 bold")

        self.cart_frame = Frame(self.frm_cart, height=400, width=400)

        self.cart_customer_name = Label(self.cart_frame, text="Customer Name:", font="Helvetica 20 bold")
        self.cart_entry_customer_name = Entry(self.cart_frame, textvariable=self.customer_name, width=15,
            font="Helvetica 30 bold")
        self.cart_customer_mobile = Label(self.cart_frame, text="Mobile no:", font="Helvetica 20 bold")
        self.cart_entry_customer_mobile = Entry(self.cart_frame, textvariable=self.customer_mobile, width=15,
            font="Helvetica 30 bold")
        self.cart_product_mobile = Label(self.cart_frame, text="Product:", font="Helvetica 20 bold")
        self.cart_entry_product_mobile = Entry(self.cart_frame, textvariable=self.product_name, width=15,
            font="Helvetica 30 bold")
        self.cart_product_quantity = Label(self.cart_frame, text="Quantity:", font="Helvetica 20 bold")
        self.cart_entry_product_quantity = Entry(self.cart_frame, textvariable=self.product_quantity, width=15,
            font="Helvetica 30 bold")

        self.button_submit = Button(self.cart_frame, text="Submit", height=2, width=15, pady=5,
            command=self.onPressSubmit)

        self.scroll = Scrollbar(self.list)
        self.Lb1 = Listbox(self.list, width=28, height=23, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.Lb1.yview)
        self.btn_list_update = Button(self.frm_list, text="Update", command=self.updateInventoryList)

    def _place(self):
        self.frm_cart.place(relx=0.075, rely=0.083)
        self.frm_list.place(relx=0.625, rely=0.083)

        self.cart_label.place(relx=0.43, rely=0.05)
        self.list_label.place(relx=0.4, rely=0.05)

        self.cart_frame.place(relx=0.035, rely=0.3)

        self.cart_customer_name.grid(row=0, column=0, pady=5, sticky=E)
        self.cart_entry_customer_name.grid(row=0, column=1, pady=5)
        self.cart_customer_mobile.grid(row=2, column=0, pady=5, sticky=E)
        self.cart_entry_customer_mobile.grid(row=2, column=1, pady=5)
        self.cart_product_mobile.grid(row=4, column=0, pady=5, sticky=E)
        self.cart_entry_product_mobile.grid(row=4, column=1, pady=5)
        self.cart_product_quantity.grid(row=6, column=0, pady=5, sticky=E)
        self.cart_entry_product_quantity.grid(row=6, column=1, pady=5)

        self.button_submit.grid(row=7, columnspan=2, pady=(20, 0))

        self.list.place(relx=0.08, rely=0.15)
        self.Lb1.place(relx=0.00, rely=0.00)
        self.scroll.place(relx=0.935, rely=0.0)
        self.btn_list_update.place(rely=0.95, relx=0.4)

    def _placeForget(self):
        self.frm_cart.place_forget()
        self.frm_list.place_forget()

        self.cart_label.place_forget()
        self.list_label.place_forget()

        self.cart_frame.place_forget()

        self.cart_customer_name.grid_forget()
        self.cart_entry_customer_name.grid_forget()
        self.cart_customer_mobile.grid_forget()
        self.cart_entry_customer_mobile.grid_forget()
        self.cart_product_mobile.grid_forget()
        self.cart_entry_product_mobile.grid_forget()
        self.cart_product_quantity.grid_forget()
        self.cart_entry_product_quantity.grid_forget()

        self.button_submit.grid_forget()

        self.list.place_forget()
        self.Lb1.place_forget()
        self.scroll.place_forget()
        self.btn_list_update.place_forget()

        self.Lb1.delete(0, 'end')

    def onPressSubmit(self):
        result_inventory = self.db_logic.inventory_find_one_item(self.product_name.get())

        if result_inventory is None:
            self.cart_entry_product_mobile.delete(0, 'end')
        elif result_inventory['noOfItems'] is None or result_inventory['noOfItems'] < self.product_quantity.get():
            self.cart_entry_product_quantity.delete(0, 'end')
        else:
            result_customer = self.db_logic.customer_find_one(self.customer_name.get())
            if result_customer is None:
                if self.customer_name.get() is None:
                    customer_count = self.db_logic.customer_collection_count()
                    customer_name = ("customer " + str(customer_count))

                    self.db_logic.customer_insert_new(customer_name, self.product_name.get(), str(self.product_quantity.get()))

                    c = result_inventory["noOfItems"] - self.product_quantity.get()

                    self.db_logic.inventory_find_by_name_update_item_no(result_inventory["name"], c)

                    self.cart_entry_customer_name.delete(0, 'end')
                    self.cart_entry_customer_mobile.delete(0, 'end')
                    self.cart_entry_product_mobile.delete(0, 'end')
                    self.cart_entry_product_quantity.delete(0, 'end')
                else:
                    self.db_logic.customer_insert_new(self.customer_name.get(), self.product_name.get(),
                                                      str(self.product_quantity.get()))
                    c = result_inventory["noOfItems"] - self.product_quantity.get()
                    self.db_logic.inventory_find_by_name_update_item_no(result_inventory["name"], c)
                    self.cart_entry_customer_name.delete(0, 'end')
                    self.cart_entry_customer_mobile.delete(0, 'end')
                    self.cart_entry_product_mobile.delete(0, 'end')
                    self.cart_entry_product_quantity.delete(0, 'end')

            else:#when customer exist &
                purchase_history = (self.product_name.get() + " " + str(self.product_quantity.get()) + " " + str(datetime.datetime.now()))
                c = result_inventory["noOfItems"] - self.product_quantity.get()
                self.db_logic.inventory_find_by_name_update_item_no(result_inventory["name"], c)

                result_customer["purchase_history"].append(purchase_history)

                self.db_logic.customer_find_by_name_update_one(result_customer["name"], result_customer["purchase_history"])

                self.cart_entry_customer_name.delete(0, 'end')
                self.cart_entry_customer_mobile.delete(0, 'end')
                self.cart_entry_product_mobile.delete(0, 'end')
                self.cart_entry_product_quantity.delete(0, 'end')

    def updateInventoryList(self):
        self.Lb1.delete(0, 'end')
        result = self.db_logic.inventory_find_all()
        i = 0
        for eachItem in result:
            self.Lb1.insert(i, str(eachItem['noOfItems']) + "\t : " + eachItem['name'])
            i = i + 1


if __name__ == '__main__':
    root = Tk()
    cart = CustomerCartScreen(root)
    cart._place()
    root.title("Inventory Management")
    root.configure(bg="red")
    root.minsize(height=600, width=1000)
    root.maxsize(height=600, width=1000)
    root.mainloop()
