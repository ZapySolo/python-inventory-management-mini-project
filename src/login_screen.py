from tkinter import *
from src.business_logic import BackendLogic
from src.selection_screen import SelectionScreen


class LoginScreen:
    def __del__(self):
        print('LoginScreen Object destroyed...')

    def __init__(self, root):
        self.root = root

        self.username = StringVar()
        self.password = StringVar()

        self.login_frame = Frame(root, height=350, width=300, borderwidth=10)
        self.label_login_header = Label(self.login_frame, text="Login")
        self.frame_login_body = Frame(self.login_frame)
        self.label_login_body_username = Label(self.frame_login_body, text="Username", font="Helvetica 15 bold")
        self.entry_login_body_username = Entry(self.frame_login_body, textvariable=self.username,
            font="Helvetica 20 bold", width=14)
        self.label_login_body_password = Label(self.frame_login_body, text="Password", font="Helvetica 15 bold")
        self.entry_login_body_password = Entry(self.frame_login_body, textvariable=self.password,
            font="Helvetica 20 bold", width=14)
        self.button_login_body_submit = Button(self.frame_login_body, text="Submit", command=self.get_content,
            height=2, width=10)
        self.label_login_body_invalid_authentication = Label(self.frame_login_body, text="Invalid Validation")

    def _pack(self):
        self.login_frame.place(relx=0.35, rely=0.2)
        self.label_login_header.place(relx=0.3, rely=0.08)
        self.frame_login_body.place(relx=0.03, rely=0.35)
        self.label_login_header.config(font=("Courier", 35))
        self.label_login_body_username.grid(row=0, column=0, pady=(0, 30))
        self.entry_login_body_username.grid(row=0, column=1, pady=(0, 30))
        self.label_login_body_password.grid(row=1, column=0, pady=(0, 30))
        self.entry_login_body_password.grid(row=1, column=1, pady=(0, 30))
        self.button_login_body_submit.grid(row=3, columnspan=2, padx=(40, 0), pady=(15, 0))

    def _place_forget(self):
        self.login_frame.place_forget()
        self.label_login_header.place_forget()
        self.frame_login_body.place_forget()
        self.label_login_body_username.grid_forget()
        self.entry_login_body_username.grid_forget()
        self.label_login_body_password.grid_forget()
        self.entry_login_body_password.grid_forget()
        self.button_login_body_submit.grid_forget()

    def get_content(self):
        self.label_login_body_invalid_authentication.place_forget()

        _db_logic = BackendLogic()
        _account = _db_logic.manager_account_find_one(self.username.get(), self.password.get())

        if _account is None:
            self.label_login_body_invalid_authentication.place(x=90, y=110)
            self.entry_login_body_username.select_clear()
            self.entry_login_body_password.select_clear()
        else:
            selection_screen = SelectionScreen(self.root)
            self._place_forget()
            selection_screen._place()
