import tkinter as tk
from visuals_user import UserFrame

class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        window_width = 500
        window_height = 500
        base_width = self.winfo_screenwidth()
        base_height = self.winfo_screenheight()
        shift_x = base_width//2 - window_width//2
        shift_y = base_height//2 - window_height//2
        self.geometry('{}x{}+{}+{}'.format(window_width, window_height, shift_x, shift_y))

class EntryFrame(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.user_button = tk.Button(master=master, text='Купить хот-дог', height=4)
        self.admin_button = tk.Button(master=master, text='Войти в админку', height=4)

        self.user_button.pack()
        self.admin_button.pack()
        self.pack()

    def go_to_user_frame(self):
        self.user_button.pack_forget()
        self.admin_button.pack_forget()
        UserFrame(self.master)





# window = Window()
# entry = EntryFrame(window)
# window.mainloop()