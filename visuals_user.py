import tkinter as tk
from module_ingredients import Ingredient
from connector_sales import SalesProcessor
from module_recipes import Hotdog
from db_config import recipes
from db_balance import Balance
from tkinter import messagebox

class UserFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.buy_button = tk.Button(master=master,
                                    text='Перейти в меню составления хот-дога',
                                    height=4,
                                    command=self.buy)
        self.buy_button.pack(expand=True)

        self.frame = tk.Frame(master=master)
        self.frame.pack(expand=True)
        self.master = self.frame

        self.money_frame = tk.LabelFrame(master=self.master,
                                         background='lightblue',
                                         text='Денег:'
                                        )
        self.money_frame.pack(side=tk.LEFT)
        self.money = tk.StringVar()
        self.money.set('{}$'.format(Balance.read()))
        self.money_screen = tk.Label(master=self.money_frame,
                                     textvariable=self.money,
                                     font='Arial 28',
                                     background='lightblue')
        self.money_screen.pack()

        # self.prices = []
        # for el in recipes:
        #     self.prices.append(recipes[el][1])
        #
        # self.dutch_button = tk.Button(master=self.master,
        #                               text='Купить датский хот-дог - {}$'.format(self.prices[0]),
        #                               height=2,
        #                               command=self.dutch_action
        #                               )
        # self.french_button = tk.Button(master=self.master,
        #                                text='Купить французский хот-дог - {}$'.format(self.prices[1]),
        #                                height=2,
        #                                command=self.french_action
        #                                )
        # self.mexican_button = tk.Button(master=self.master,
        #                                 text='Купить мексиканский хот-дог - {}$'.format(self.prices[2]),
        #                                 height=2,
        #                                 command=self.mexican_action
        #                                 )
        #
        # self.french_button.pack()
        # self.dutch_button.pack()
        # self.mexican_button.pack()

        self.remains_label = tk.Label(master=self.master, text='Текущие остатки:')
        self.remains_label.pack()

        self.show_remains()

        self.back_button = tk.Button(master=self.master, text='Назад', command=self.back_action)
        self.back_button.pack(side=tk.BOTTOM)

    def show_remains(self):
        self.remain_frame = tk.Frame(master=self.master, background='white')
        self.remain_frame.pack()
        for el in Ingredient._varieties:
            text = el.name + ' ' + str(el.remain)
            temp = tk.Label(master=self.remain_frame, text=text, background='white', font='Arial 16')
            temp.pack(anchor= tk.E)

    def buy(self):
        pass


    def dutch_action(self):
        if SalesProcessor.register_sell(Hotdog.get_data('Dutch')) is True:
            self.money.set('{}$'.format(Balance.read()))
            self.remain_frame.destroy()
            self.show_remains()
        else:
            messagebox.showerror(message='Недостаточно ингредиентов')

    def french_action(self):
        if SalesProcessor.register_sell(Hotdog.get_data('French')) is True:
            self.money.set('{}$'.format(Balance.read()))
            self.remain_frame.destroy()
            self.show_remains()
        else:
            messagebox.showerror(message='Недостаточно ингредиентов')

    def mexican_action(self):
        if SalesProcessor.register_sell(Hotdog.get_data('Mexican')) is True:
            self.money.set('{}$'.format(Balance.read()))
            self.remain_frame.destroy()
            self.show_remains()
        else:
            messagebox.showerror(message='Недостаточно ингредиентов')

    def back_action(self):
        pass


class BuyMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.frame = tk.Frame(master=master)
        self.frame.place(width=400, height=400, x=50, y=50)
        self.master = self.frame

        self.menu_frame = tk.LabelFrame(master=self.master, background='white', text='Menu:')
        self.menu_frame.place(width=198, height=148, x=0)

        self.recipe_frame = tk.LabelFrame(master=self.master, background='white', text='Recipe:')
        self.recipe_frame.place(width=198, height=148, x=200)

        self.sauces_frame = tk.LabelFrame(master=self.master, background='white', text='Sauces:')
        self.sauces_frame.place(width=198, height=148, x=0, y=150)

        self.toppings_frame = tk.LabelFrame(master=self.master, background='white', text='Toppings:')
        self.toppings_frame.place(width=198, height=148, x=200, y=150)

        self.display_frame = tk.Frame(master=self.master)
        self.display_frame.place(width=300, height=70, x=50, y=300)
        self.display_price = tk.LabelFrame(master=self.display_frame, text='Price:')
        self.display_price.place(width=100, height=70, x=0, y=0)
        self.price = tk.Label(master=self.display_price, text='0$', font='Arial 20')
        self.price.pack()
        self.buy_button = tk.Button(master=self.display_frame, text='Купить', font='Arial 20')
        self.buy_button.place(width=150, height=40, x=150, y=4)
        self.choicevar = tk.IntVar()
        self.choice1 = tk.Radiobutton(
            master=self.display_frame,
            variable=self.choicevar,
            value=1,
            text='Наличными')
        self.choice1.place(x=110, y=45)
        self.choice2 = tk.Radiobutton(
            master=self.display_frame,
            variable=self.choicevar,
            value=2,
            text='Картой')
        self.choice2.place(x=230, y=45)

        self.back_button = tk.Button(master=self.master, text='Назад', command=self.back_action)
        self.back_button.pack(side=tk.BOTTOM)

    def back_action(self):
        pass
