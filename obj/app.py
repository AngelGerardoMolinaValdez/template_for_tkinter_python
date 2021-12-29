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
        Builder.set_style_properties(self.frame, "", "")
        self.frame.grid(row = 0, column = 0, columnspan = 1, pady = 0, padx = 0)



        self.lbl_texto = Label(self.frame)
        self.lbl_texto['text'] = "Texto:"
        Builder.set_style_properties(self.lbl_texto, "", "")
        self.lbl_texto.grid(row = 1, column = 0, columnspan = 1, pady = 0, padx = 0)



        self.input_string = Entry(self.frame)
        self.input_string['text'] = "Texto:"
        Builder.set_style_properties(self.input_string, "", "")
        self.input_string.grid(row = 1, column = 2)
        self.input_string.focus()



        self.btn_convert = Button(self.frame)
        self.btn_convert['text'] = "Encriptar"
        Builder.set_style_properties(self.btn_convert, "black", "white")
        self.btn_convert['command'] = self.econde_str
        self.btn_convert.grid(row = 2, column = 0, columnspan = 5, sticky = W + E)



        self.lbl_encrypt_str = Label(self.frame)
        Builder.set_style_properties(self.lbl_encrypt_str, "auto", "")
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

        '''
        cwd = os.getcwd()
        print(cwd)
        cwd = os.chdir("..")
        cwd = os.chdir("img")
        cwd = os.getcwd()
        print(cwd)
        cwd += "\\"
        print(cwd[:len(cwd)-1])
        img = "{0}my_image.png".format(cwd)
        print(f"\n\n{img}")
        imagen = PhotoImage(file=img)
        #[len(cwd)-1]



        image = Image.open("my_image.png")
        #                   ancho, alto
        image = Image.resize((400,250), Image.HAMMING)
        self.frame.img = ImageTk.PhotoImage(image)


        lbl_image = Label(self.frame) #, compound='top')
        lbl_image["image"] = self.frame.img
        lbl_image.grid(row = 6, column = 0,  sticky = N + S)

        '''
        #Label(self.window, image=imagen, bd=0).grid(row = 7, column = 0, columnspan = 5, sticky = W + E)

        '''
        self.btn_copy = Button(self.window)
        self.btn_copy['text'] = "Copiar"
        self.btn_copy['font'] = ("Arial", 12)
        self.btn_copy['bg'] = "black"
        self.btn_copy['fg'] = "white"
        self.btn_copy.grid(row = 4, column = 0, columnspan = 5, sticky = W + E)
        self.btn_copy['command'] =


        self.btn_copy = Button(self.window)
        self.btn_copy['text'] = "Limpiar"
        self.btn_copy['font'] = ("Arial", 12)
        self.btn_copy['bg'] = "black"
        self.btn_copy['fg'] = "white"
        self.btn_copy.grid(row = 5, column = 0, columnspan = 5, sticky = W + E)
        self.btn_copy['command'] =

        '''


    def random_color(self, obj = None):
        list_values = []
        for i in range(0, 256):
            list_values.append(i)

        r = random.choice(list_values)
        g = random.choice(list_values)
        b = random.choice(list_values)
        #print(f"{r} {g} {b}")
        #print((r < 102 and g < 54 or b < 54))
        #print((g < 102 and r < 54 or b < 54))
        #print((b < 102 and r < 54 or g < 54))
        if (r < 102 and g < 54 or b < 54) or (g < 102 and r < 54 or b < 54) or (b < 102 and r < 54 or g < 54):
        #g < 102 or b < 102:
            obj["fg"] = "white"
        else:
            obj["fg"] = "black"
        RGB = (r, g, b)
        #print("#%02x%02x%02x" % RGB)
        return "#%02x%02x%02x" % RGB


    def econde_str(self):
        #self.str_encode['bg'] = self.random_color()
        str_user = self.input_string.get()
        #print(len(str_user))
        #self.str_encode.delete(0, "end")
        self.lbl_encrypt_str['bg'] = self.random_color(self.lbl_encrypt_str)
        self.lbl_encrypt_str["text"] = ""
        list_chars = list(str_user)
        #print(str_user)
        enconde_string = ""


        for char in list_chars:

            ascii_value = ord(char)
            ascii_value = str(ascii_value)

            if int(ascii_value) <= 99:

                ascii_value = "0" + ascii_value
                ascii_value = str(ascii_value)



            enconde_string += ascii_value + "&!%/"
            #ascii_value = ascii_value[::-1]
        #*****************************
        len_str = len(enconde_string)

        if int(len_str) <= 99:

            len_str = str(len_str)
            len_str = "0" + len_str


        enconde_string += "#/?{0}#/?".format(len_str)


        enconde_string = enconde_string[::-1]


        #text_entry = StringVar(enconde_string)


        #self.str_encode.textvariable = enconde_string
        #print(enconde_string)
        self.econde_str = enconde_string
        #self.str_encode.insert(0, self.econde_str)
        self.lbl_encrypt_str["text"] = self.econde_str


    def copy_to_clipboard(self):
        #self.window.withdraw()
        self.window.clipboard_clear()
        self.window.clipboard_append(str(self.econde_str))


    def _clean_all(self):
        self.input_string.delete('0', END)
        self.lbl_encrypt_str["text"] = ""
