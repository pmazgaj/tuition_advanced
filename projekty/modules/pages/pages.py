"""
Define all pages for the application.
"""
import tkinter as tk
from projekty.modules.settings import LARGE_FONT


class StartPage(tk.Frame):
    """Start page class"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Start page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # lambda - to use parameter in function
        button = tk.Button(self, text="Visit page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):
    """Page one class"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page one', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # lambda - to use parameter in function
        button = tk.Button(self, text="Back to start page",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()

        button2 = tk.Button(self, text="Go to page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    """Page two class"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page Two', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # lambda - to use parameter in function
        button = tk.Button(self, text="Back to start page",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()
