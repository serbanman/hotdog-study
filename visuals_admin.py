import tkinter as tk
from db_balance import Balance

class AdminFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.frame = tk.Frame(master=master)
        self.frame.pack()
        self.master = self.frame

        self.procurement_button = tk.Button(master=self.master,
                                            text='Перейти в меню закупок',
                                            command=...)
        self.procurement_button.pack()
        self.history_button = tk.Button(master=self.master,
                                            text='Перейти в историю операций',
                                            command=...)
        self.history_button.pack()

        self.back_button = tk.Button(master=self.master, text='Назад', command=self.back_action)
        self.back_button.pack(side=tk.BOTTOM)

    def back_action(self):
        pass



class ProcurementFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.frame = tk.Frame(master=master)
        self.frame.pack(expand=True)
        self.master = self.frame

        self.money_frame = tk.LabelFrame(master=self.master,
                                         background='lightblue',
                                         text='Денег:'
                                         )
        self.money_frame.pack(side=tk.BOTTOM)
        self.money = tk.StringVar()
        self.money.set('{}$'.format(Balance.read()))
        self.money_screen = tk.Label(master=self.money_frame,
                                     textvariable=self.money,
                                     font='Arial 28',
                                     background='lightblue')
        self.money_screen.pack(side=tk.BOTTOM, expand=True)


        self.back_button = tk.Button(master=self.master, text='Назад', command=self.back_action)
        self.back_button.pack(side=tk.BOTTOM)

    def back_action(self):
        pass

class OperationsFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.frame = tk.Frame(master=master)
        self.frame.pack()
        self.master = self.frame

        self.back_button = tk.Button(master=self.master, text='Назад', command=self.back_action)
        self.back_button.pack(side=tk.BOTTOM)

    def back_action(self):
        pass


