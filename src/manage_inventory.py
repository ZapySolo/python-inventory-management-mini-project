from tkinter import *
from src.business_logic import BackendLogic


class ManageInventoryScreen:
    def __del__(self):
        print('ManageInventoryScreen Object destroyed...')

    def __init__(self, root):

        self.db_logic = BackendLogic()

        # entry details
            # add new
        self.name_new = StringVar()
        self.category_0 = StringVar()
        self.category_1 = StringVar()
        self.supplier = StringVar()
        self.packetsCount = IntVar()
        self.actualCost = IntVar()
        self.sellingPrice = IntVar()
            # update
        self.name_update = StringVar()
        self.packetCount_update = IntVar()

        #frames
        self.addnew = Frame(root, height=500, width=350)
        self.update = Frame(root, height=500, width=250)
        self.list = Frame(root, height=500, width=300)
        self.lbl_addnew = Label(self.addnew, text="Add New Item")
        self.lbl_update = Label(self.update, text="Update Item")
        self.lbl_list = Label(self.list, text="Inventory")

        self.frm_addnew_form = Frame(self.addnew)

        #Add Product
        self.lbl_addnew_product_name = Label(self.frm_addnew_form, text="name:")
        self.entry_addnew_product_name = Entry(self.frm_addnew_form, textvariable=self.name_new)

        self.lbl_addnew_category = Label(self.frm_addnew_form, text="category:")
        self.entry_addnew_category_0 = Entry(self.frm_addnew_form, textvariable=self.category_0)
        self.entry_addnew_category_1 = Entry(self.frm_addnew_form, textvariable=self.category_1)

        self.lbl_addnew_supplier = Label(self.frm_addnew_form, text="supplier:")
        self.entry_addnew_supplier = Entry(self.frm_addnew_form, textvariable=self.supplier)

        self.lbl_addnew_packets = Label(self.frm_addnew_form, text="no. of \npackets:")
        self.entry_addnew_packets = Entry(self.frm_addnew_form, textvariable=self.packetsCount)

        self.lbl_addnew_actual_price = Label(self.frm_addnew_form, text="actual cost:")
        self.entry_addnew_actual_price = Entry(self.frm_addnew_form, textvariable=self.actualCost)

        self.lbl_addnew_selling_price = Label(self.frm_addnew_form, text="selling price:")
        self.entry_addnew_selling_price = Entry(self.frm_addnew_form, textvariable=self.sellingPrice)

        self.button_addnew_submit = Button(self.frm_addnew_form, text="SUBMIT", height=2, width=15, command=self.onPressAddNewSubmit)

        #Update Product
        self.update_form = Frame(self.update)
        self.lbl_update_name = Label(self.update_form, text="name")
        self.entry_update_name = Entry(self.update_form, textvariable=self.name_update)
        self.lbl_update_quantity = Label(self.update_form, text="quantity")
        self.entry_update_quantity = Entry(self.update_form, textvariable=self.packetCount_update)
        self.button_update_submit = Button(self.update_form, text="SUBMIT", height=2, width=15, command=self.onPressUpdateSubmit)

        #inventory list
        self.scroll = Scrollbar(self.list)
        self.Lb1 = Listbox(self.list, width=28, height=23, yscrollcommand=self.scroll.set)
        self.scroll.config(command = self.Lb1.yview)

        self.btn_list_update = Button(self.list, text="Update", command=self.updateInventoryList)

    def _place(self):
        self.addnew.place(relx=0.025, rely=0.083)
        self.update.place(relx=0.4, rely=0.083)
        self.list.place(relx=0.675, rely=0.083)

        self.lbl_addnew.place(relx=0.23, rely=0.05)
        self.lbl_addnew.config(font=("Courier", 25))
        self.lbl_update.place(relx=0.15, rely=0.05)
        self.lbl_update.config(font=("Courier", 25))
        self.lbl_list.place(relx=0.27, rely=0.05)
        self.lbl_list.config(font=("Courier", 25))

        self.frm_addnew_form.place(relx=0.02, rely=0.2)

        #add new item
        self.lbl_addnew_product_name.grid(row=0, column=0, pady = 10,sticky = E)
        self.lbl_addnew_product_name.config(font=("Courier", 15))
        self.entry_addnew_product_name.grid(row=0, column=1,pady = 10)

        self.lbl_addnew_category.grid(row=1, column=0,pady = 10,sticky = E)
        self.lbl_addnew_category.config(font=("Courier", 15))
        self.entry_addnew_category_0.grid(row=1, column=1,pady = 10)
        self.entry_addnew_category_1.grid(row=2, column=1,pady = (0,10))

        self.lbl_addnew_supplier.grid(row=3, column=0,pady = 10,sticky = E)
        self.lbl_addnew_supplier.config(font=("Courier", 15))
        self.entry_addnew_supplier.grid(row=3, column=1,pady = 10)

        self.lbl_addnew_packets.grid(row=4, column=0,pady = 10,sticky = E)
        self.lbl_addnew_packets.config(font=("Courier", 15))
        self.entry_addnew_packets.grid(row=4, column=1,pady = 10)

        self.lbl_addnew_actual_price.grid(row=5, column=0,pady = 10,sticky = E)
        self.lbl_addnew_actual_price.config(font=("Courier", 15))
        self.entry_addnew_actual_price.grid(row=5, column=1,pady = 10)

        self.lbl_addnew_selling_price.grid(row=6, column=0,pady = 10,sticky = E)
        self.lbl_addnew_selling_price.config(font=("Courier", 15))
        self.entry_addnew_selling_price.grid(row=6, column=1,pady = 10)

        self.button_addnew_submit.grid(row=7, columnspan=2, pady=(0, 10))

        #update item
        self.update_form.place(relx=0.1, rely=0.3)
        self.lbl_update_name.grid(row=1, column=0)
        self.lbl_update_name.config(font=("Courier", 15))
        self.entry_update_name.grid(row=2, column=0, pady=(0, 10))
        self.lbl_update_quantity.grid(row=3, column=0)
        self.lbl_update_quantity.config(font=("Courier", 15))
        self.entry_update_quantity.grid(row=4, column=0, pady=(0, 10))
        self.button_update_submit.grid(row=5, column=0, pady=10)

        #inventory list
        self.Lb1.place(relx=0.07, rely=0.15)
        self.scroll.place(relx=0.93, rely=0.15)
        self.btn_list_update.place(rely=0.95, relx=0.4)

    def _placeForget(self):
        self.addnew.place_forget()
        self.update.place_forget()
        self.list.place_forget()

        self.lbl_addnew.place_forget()
        self.lbl_update.place_forget()
        self.lbl_list.place_forget()

        self.frm_addnew_form.place_forget()

        # add new item
        self.lbl_addnew_product_name.grid_forget()
        self.entry_addnew_product_name.grid_forget()

        self.lbl_addnew_category.grid_forget()
        self.entry_addnew_category_0.grid_forget()
        self.entry_addnew_category_1.grid_forget()

        self.lbl_addnew_supplier.grid_forget()
        self.entry_addnew_supplier.grid_forget()

        self.lbl_addnew_packets.grid_forget()
        self.entry_addnew_packets.grid_forget()

        self.lbl_addnew_actual_price.grid_forget()
        self.entry_addnew_actual_price.grid_forget()

        self.lbl_addnew_selling_price.grid_forget()
        self.entry_addnew_selling_price.grid_forget()

        self.button_addnew_submit.grid_forget()

        # update item
        self.update_form.place_forget()
        self.lbl_update_name.grid_forget()
        self.entry_update_name.grid_forget()
        self.lbl_update_quantity.grid_forget()
        self.entry_update_quantity.grid_forget()
        self.button_update_submit.grid_forget()

        # inventory list
        self.Lb1.place_forget()
        self.scroll.place_forget()
        self.btn_list_update.place_forget()

        self.Lb1.delete(0, 'end')

    def onPressAddNewSubmit(self):
        if self.name_new.get() == '' or self.packetsCount.get() == '':
            return
        elif self.db_logic.inventory_find_one_item(self.name_new.get()) is not None:
            self.entry_addnew_product_name.delete(0, 'end')
            print("Type of...", type(self.db_logic.inventory_find_one_item(self.name_new.get())))
        else:
            obj = {
                "name": self.name_new.get(),
                "category": [self.category_0.get(), self.category_1.get()],
                "supplier": self.supplier.get(),
                "noOfItems": self.packetsCount.get(),
                "actualPrice": self.actualCost.get(),
                "sellingPrice": self.sellingPrice.get()
            }
            self.db_logic.inventory_insert_one_item(obj)

            self.entry_addnew_product_name.delete(0, 'end')
            self.entry_addnew_category_0.delete(0, 'end')
            self.entry_addnew_category_1.delete(0, 'end')
            self.entry_addnew_supplier.delete(0, 'end')
            self.entry_addnew_packets.delete(0, 'end')
            self.entry_addnew_actual_price.delete(0, 'end')
            self.entry_addnew_selling_price.delete(0, 'end')

    def onPressUpdateSubmit(self):
        if self.db_logic.inventory_find_one_item(self.name_update.get()) is None:
            self.entry_update_name.delete(0, 'end')
        else:
            self.db_logic.inventory_find_by_name_update_item_no(self.name_update.get(), self.packetCount_update.get())
            self.entry_update_name.delete(0, 'end')
            self.entry_update_quantity.delete(0, 'end')

    def updateInventoryList(self):
        self.Lb1.delete(0, 'end')
        result = self.db_logic.inventory_find_all()
        i = 0
        number = 00
        for eachItem in result:
            try:
                number = eachItem['noOfItems']
            except:
                eachItem['noOfItems'] = 0

            self.Lb1.insert(i, str(number) + "\tx : " + eachItem['name'])
            i = i + 1


if __name__ == '__main__':
    root = Tk()
    cart = ManageInventoryScreen(root)
    cart._place()
    root.title("Inventory Management")
    root.configure(bg="red")
    root.minsize(height=600, width=1000)
    root.maxsize(height=600, width=1000)
    root.mainloop()
