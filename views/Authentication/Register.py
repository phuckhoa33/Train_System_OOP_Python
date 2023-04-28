import tkinter as tk
from tkinter import messagebox
from LoginPage import LoginPage

class RegisterPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.__parent = parent

        self.__username_label = tk.Label(self, text="Username")
        self.__username_entry = tk.Entry(self)

        self.__password_label = tk.Label(self, text="Password")
        self.__password_entry = tk.Entry(self, show="*")

        self.__confirm_password_label = tk.Label(self, text="Confirm Password")
        self.__confirm_password_entry = tk.Entry(self, show="*")

        self.__register_button = tk.Button(self, text="Register", command=self._register)
        self.__back_button = tk.Button(self, text="Back", command=self._show_login)

        self.__username_label.pack()
        self.__username_entry.pack()
        self.__password_label.pack()
        self.__password_entry.pack()
        self.__confirm_password_label.pack()
        self.__confirm_password_entry.pack()
        self.__register_button.pack()
        self.__back_button.pack()

    def _register(self):
        # Register a new user
        username = self.__username_entry.get()
        password = self.__password_entry.get()
        confirm_password = self.__confirm_password_entry.get()

        # Check if the password and confirm password match
        if password == confirm_password:
            # If the password and confirm password match, show a success message and switch to the login page
            messagebox.showinfo("Success", "You have successfully registered")
            self._show_login()
        else:
            # If the password and confirm password do not match, show an error message
            messagebox.showerror("Error", "The password and confirm password do not match")

    def _show_login(self):
        # Switch to the login page
        self.__parent.switch_login()
