import tkinter as tk
from tkinter import messagebox
import os
from db_plugins import OperationsToDB
from module_ingredients import Ingredient
from visuals_root import Window, EntryFrame
from visuals_user import UserFrame, BuyMenu
from visuals_admin import AdminFrame, ProcurementFrame, OperationsFrame
from connector_buy import Buy
from db_balance import Balance
from db_config import recipes, nomenclature
from connector_sales import SalesProcessor

class UID:
    def __init__(self):
        self.root = Window()
        self.bg_img = tk.PhotoImage(file= self.find_image())

        self.background = tk.Label(self.root, image=self.bg_img)
        self.background.place(x=0, y=0, width=500, height=500)

        self.entry = EntryFrame(master=self.root)
        self.entry.user_button['command'] = self.change_to_user_interface
        self.entry.admin_button['command'] = self.change_to_admin_interface
        self.root.mainloop()

    def find_image(self):
        dir = os.getcwd()
        filename = 'hotdog_pic.png'
        picture_path = os.path.abspath(os.path.join(dir, filename))
        # if os.getcwd().endswith('visuals'):
        #     picture_path = os.path.join(dir, filename)
        # elif os.getcwd().endswith('hotdog'):
        #     dir += '/visuals/'
        #     picture_path = os.path.join(dir, filename)
        # else:
        #     dir = os.path.split(dir)[0] + '/visuals/'
        #     picture_path = os.path.join(dir, filename)
        return picture_path

    def change_to_user_interface(self):
        #  кнопка возврата в первое пользовательское меню
        self.root.unbind('<Button-1>')
        try:
            self.buy_menu.frame.destroy()
        except:
            pass

        self.entry.user_button.pack_forget()
        self.entry.admin_button.pack_forget()

        self.userframe = UserFrame(self.root)
        self.userframe.buy_button['command']=self.change_to_buy
        self.userframe.back_button['command'] = self.change_to_entry

    def change_to_buy(self):
        #  меню составления хот-дога
        try:
            self.userframe.frame.destroy()
            self.userframe.buy_button.destroy()
        except:
            pass

        # self.price = 0
        self.buy_menu = BuyMenu(self.root)
        # self.buy_menu.price['text'] = '{}$'.format(self.price)
        self.buy_menu.back_button['command'] = self.change_to_user_interface

        menu_objs = []
        for recipe in recipes:
            text = '{} - {}$'.format(recipe, recipes[recipe][1])
            temp = MenuButton(master=self.buy_menu.menu_frame,
                              text=text,
                              data=recipes[recipe][0],
                              price=recipes[recipe][1],
                              where_to_place_obj=self.buy_menu.recipe_frame)
            temp.pack(anchor = tk.W, padx=10)
            menu_objs.append(temp)

        self.sauce_price = 0
        def add_sauce(event=None):
            self.sauce_price = 0
            def do():
                for el in sauces_objs:
                    self.sauce_price += el.get_price()
                # print(f'total price now is {self.sauce_price}')
            self.root.after(100, do)

        sauces_objs = []
        for el in nomenclature['sauces']:
            text = '{} - {}$'.format(el[0], el[2])
            temp = SauceToppingPiece(
                master=self.buy_menu.sauces_frame,
                name=text,
                onvalue=1,
                offvalue=0,
                recipe_obj=el
            )
            temp.pack(anchor=tk.W, padx=10)
            sauces_objs.append(temp)
            temp.bind('<Button-1>', add_sauce)

        self.topping_price = 0
        def add_topping(event=None):
            self.topping_price = 0
            def do():
                for el in topping_objs:
                    self.topping_price += el.get_price()
                # print(f'total price now is {self.topping_price}')

            self.root.after(100, do)

        topping_objs = []
        for el in nomenclature['toppings']:
            text = '{} - {}$'.format(el[0], el[2])
            temp = SauceToppingPiece(
                master=self.buy_menu.toppings_frame,
                name=text,
                onvalue=1,
                offvalue=0,
                recipe_obj=el
            )
            temp.pack(anchor=tk.W, padx=10)
            topping_objs.append(temp)
            temp.bind('<Button-1>', add_topping)

        self.price = 0
        self.recipe = []

        def calcucate_price(event=None):
            def do():
                price = 0
                recipe = []
                price += MenuButton.price_of_chosen
                for el in MenuButton.recipe_of_chosen:
                    recipe.append(el)
                objects = [*sauces_objs, *topping_objs]
                for object in objects:
                    price += object.get_price()
                    recipe.append(object.get_name())
                try:
                    self.buy_menu.price['text'] = '{}$'.format(price)
                except:
                    pass
                self.price = price
                self.recipe = list(filter(lambda x: x!= 0, recipe))
                # print(self.recipe)
            self.root.after(100, do)

        self.root.bind('<Button-1>', calcucate_price)

        def process_sale():
            recipe_obj = (tuple((k, 1) for k in self.recipe), self.price)
            print(recipe_obj)
            if self.buy_menu.choicevar.get() not in [1,2]:
                messagebox.showerror(message='Выберите способ оплаты')
            else:
                if SalesProcessor.register_sell(recipe_obj) is True:
                    text = 'You bought {} for {}'.format(self.recipe, self.price)
                    messagebox.showinfo(message=text)
                    self.change_to_user_interface()
                else:
                    messagebox.showerror(message='Недостаточно ингредиентов')
        self.buy_menu.buy_button['command'] = process_sale


    def change_to_entry(self):
        #  кнопка возврата в основное меню
        try:
            self.userframe.frame.destroy()
            self.userframe.buy_button.destroy()
        except:
            pass
        try:
            self.adminframe.frame.destroy()
        except:
            pass
        self.entry.user_button.pack()
        self.entry.admin_button.pack()


    def change_to_admin_interface(self):
        #  первое админ меню
        try:
            self.procurementframe.frame.destroy()
        except:
            pass
        try:
            self.historyframe.frame.destroy()
        except:
            pass

        self.entry.user_button.pack_forget()
        self.entry.admin_button.pack_forget()
        self.adminframe = AdminFrame(self.root)
        self.adminframe.procurement_button['command'] = self.change_to_procurement_interface
        self.adminframe.history_button['command'] = self.change_to_history_interface
        self.adminframe.back_button['command'] = self.change_to_entry

    def change_to_procurement_interface(self):
        #  меню закупок
        self.adminframe.frame.destroy()
        self.procurementframe = ProcurementFrame(master=self.root)

        self.procurementframe.list_frame = tk.Frame(master=self.procurementframe.master)
        self.procurementframe.list_frame.pack()

        def refresh(event):
            def do():
                # print(f'Баланс на обновлении - {Balance.read()}')
                self.procurementframe.money.set('{}$'.format(Balance.read()))

            self.procurementframe.after(100, do)

        for ind, el in enumerate(Ingredient._varieties):
            text = 'Buy {} for {}$'.format(el.name, el.cost)
            temp = BuyButton(self.procurementframe.list_frame, text, el.name)
            temp.bind('<Button-1>', refresh)
            temp.grid(row=ind)
        self.procurementframe.back_button['command'] = self.change_to_admin_interface

    def change_to_history_interface(self):
        #  меню истории операций
        self.adminframe.frame.destroy()

        self.historyframe = OperationsFrame(master=self.root)

        self.historyframe.list_frame = tk.Frame(master=self.historyframe.master)
        self.historyframe.list_frame.pack()

        values = OperationsToDB.get()

        for el in values:
            text = '#{}  date:({}) type:"{}" sum:{}$'.format(el[0],el[1],el[2],el[3])
            temp = tk.Label(master=self.historyframe.list_frame, text=text)
            temp.grid()

        self.historyframe.back_button['command'] = self.change_to_admin_interface


class BuyButton(tk.Button):
    #  класс кнопки закупки ингредиента
    def __init__(self, master, text, value):
        tk.Button.__init__(self, master)

        self.value = value
        self['text'] = text
        self['command'] = self.process

    def process(self):
        Buy.register(self.value)


class MenuButton(tk.Button):
    #  класс кнопки рецепта хот-дога в меню покупки
    _instances = []
    price_of_chosen = 0
    recipe_of_chosen = ''

    def __init__(self, master, text, data, price, where_to_place_obj):
        tk.Button.__init__(self, master)

        self.obj = where_to_place_obj
        self.text = text
        self.data = data
        self.price = price
        self['text'] = text
        self['command'] = self.process

        self.frame = tk.Frame(master=where_to_place_obj)
        self.frame.pack()

        MenuButton._instances.append(self)

    def get(self):
        return MenuButton.price_of_chosen

    def process(self):
        for el in MenuButton._instances:
            el.frame.pack_forget()

        self.frame = tk.Frame(master=self.obj, background='white')
        self.frame.pack()
        for el in self.data:
            temp = tk.Label(master=self.frame,
                            text=el,
                            background='white',
                            font='Arial 20')
            temp.pack()
        MenuButton.price_of_chosen = self.price
        MenuButton.recipe_of_chosen = self.data


class SauceToppingPiece(tk.Checkbutton):
    #  кнопка выбора соуса/топпинга
    def __init__(self, master, name, onvalue, offvalue, recipe_obj):
        tk.Checkbutton.__init__(self, master)

        self.name = name
        self['text'] = name
        self.intvar = tk.IntVar()
        self['variable'] = self.intvar
        self['onvalue'] = onvalue
        self['offvalue'] = offvalue
        self.recipe_obj = recipe_obj

    def get_price(self):
        # print(self.recipe_obj[2])
        if self.intvar.get() == 1:
            return self.recipe_obj[2]
        else:
            return 0

    def get_name(self):
        if self.intvar.get() == 1:
            return self.recipe_obj[0]
        else:
            return 0

