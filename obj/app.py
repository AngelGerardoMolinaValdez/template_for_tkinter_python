import os

try:
    from tkinter import *
    from tkinter import ttk
    from PIL import ImageTk, Image
    from tkinter import messagebox as msgbox

except Exception as e:
    os.system('pip install tk')
    from tkinter import *
    from tkinter import ttk
    from PIL import ImageTk, Image
    from tkinter import messagebox as msgbox

finally:
    import random
    from obj.common import Configuration



class GUI:

    def __init__(self, window):

        self.window = window
        Builder = Configuration(self.window)
        Builder.set_StyleFont(("Arial", 12))
        Builder.define_window_features("String Enconder", 420, 200)


        self.frame = LabelFrame(self.window)
        self.frame['text'] = "String Enconder"
        Builder.set_style_properties(self.frame)
        self.frame.grid(row = 0, column = 0, columnspan = 1, pady = 0, padx = 0)



        self.lbl_texto = Label(self.frame)
        self.lbl_texto['text'] = "Texto:"
        Builder.set_style_properties(self.lbl_texto)
        self.lbl_texto.grid(row = 1, column = 0, columnspan = 1, pady = 0, padx = 0)



        self.input_string = Entry(self.frame)
        self.input_string['text'] = "Texto:"
        Builder.set_style_properties(self.input_string)
        self.input_string.grid(row = 1, column = 2)
        self.input_string.focus()



        self.btn_convert = Button(self.frame)
        self.btn_convert['text'] = "Encriptar"
        Builder.set_style_properties(self.btn_convert, "black", "white")
        self.btn_convert['command'] = self.econde_str
        self.btn_convert.grid(row = 2, column = 0, columnspan = 5, sticky = W + E)



        self.lbl_encrypt_str = Label(self.frame)
        Builder.set_style_properties(self.lbl_encrypt_str, "auto")
        self.lbl_encrypt_str.grid(row = 3, column = 0, columnspan = 1, pady = 0, padx = 0)



        self.btn_copy = Button(self.frame)
        self.btn_copy['text'] = "Copiar"
        Builder.set_style_properties(self.btn_copy, "black", "white")
        self.btn_copy['command'] = self.copy_to_clipboard
        self.btn_copy.grid(row = 4, column = 0, columnspan = 5, sticky = W + E)


        self.btn_copy = Button(self.frame)
        self.btn_copy['text'] = "Limpiar"
        Builder.set_style_properties(self.btn_copy, "black", "white")
        self.btn_copy['command'] = self._clean_all
        self.btn_copy.grid(row = 5, column = 0, columnspan = 5, sticky = W + E)