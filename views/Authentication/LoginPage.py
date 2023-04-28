import tkinter as tk
from tkinter import messagebox
from Register import RegisterPage
from home import HomePage

class LoginPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.__parent = parent

        self.__username_label = tk.Label(self, text="Username")
        self.__username_entry = tk.Entry(self)

        self.__password_label = tk.Label(self, text="Password")
        self.__password_entry = tk.Entry(self, show="*")

        self.__login_button = tk.Button(self, text="Login", command=self._login)
        self.__register_button = tk.Button(self, text="Register", command=self._show_register)

        self.__username_label.pack()
        self.__username_entry.pack()
        self.__password_label.pack()
        self.__password_entry.pack()
        self.__login_button.pack()
        self.__register_button.pack()

    def _login(self):
        # Authenticate the user
        username = self.__username_entry.get()
        password = self.__password_entry.get()

        # Check if the username and password are correct
        if username == "admin" and password == "admin":
            # If the credentials are correct, switch to the home page
            self.__parent.switch_home()
        else:
            # If the credentials are incorrect, show an error message
            messagebox.showerror("Error", "Incorrect username or password")

    def _show_register(self):
        # Switch to the register page
        self.__parent.switch_register()