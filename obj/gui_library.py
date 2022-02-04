class Configuration:

    StyleFont = tuple()


    def __init__(self, obj_form):
        self.obj_form = obj_form

    '''
---------------------------------------------------------------------------------------------------------
    Metodo:         define_window_features

    Descripcion:    Define las configuraciones inciales de una ventana de la clase Tkinter

    Argumentos:
                    title           =   Es el titulo de la ventana
                    bg_color        =   Es el color del fondo de la pantalla
                    width           =   Es el ancho de la ventana
                    height          =   Es el alto de la ventana
                    center_window   =   Indica si se desea centrar la ventana en la pantalla
                    resizable       =   Indica si se podra agrander o hacer mas pequena la ventana
                    tranparency     =   Indica si se desea hacer transparente la ventana
                    path_icon       =   Es la ruta donde esta alojado el icono de la ventana

    Ejemplo:
                    Object.define_window_features("Ventana", 420, 400, "black", True, False, True,  "style/Icon.ico")

---------------------------------------------------------------------------------------------------------
    '''
    def define_window_features(self, title, width, height, bg_color = "", center_window = True, resizable = False, tranparency_yes = False, path_icon = None):
        
        self._get_data_window()

        if len(title) > 1:
            try:
                self.obj_form.title(title)

            except Exception as E_windown_title:
                print("No fue asignado ningun nombre para la ventana creada, sera asignada por un valor default")
                self.obj_form.title("Ventana Default")


        if len(bg_color) > 1:
            try:
                self.obj_form.configure(bg = str(bg_color))

            except Exception as E_windown_bg:
                print("No fue posible asignar color de fondo a la ventana")


        try:
            self.obj_form.iconbitmap(path_icon)
        except Exception as E_fail_set_icon:
            print(f"Error al asignar icono en la ventana requerida, verfique la ruta!")


        if center_window:
            x_obj_form = self.obj_form.winfo_screenwidth() // 2 - width // 2
            y_obj_form = self.obj_form.winfo_screenheight() // 2 - height // 2
            posicion = str(width) + "x" + str(height) + "+" + str(x_obj_form) + "+" + str(y_obj_form)
            self.obj_form.geometry(posicion)
        else:
            self.obj_form.geometry(width, height)
        

        if resizable:
            self.obj_form.resizable(0,0)
        else:
            self.obj_form.resizable(1,1)


        if tranparency_yes:
            self.obj_form.attributes('-alpha', 0.7)

    '''
---------------------------------------------------------------------------------------------------------
    Metodo:         set_style_properties

    Descripcion:    Define las configuraciones de un objeto de la clase Tkinter

    Argumentos:
                    obj_tag                     =   Es el objeto en el que se van a realizar las configuraciones 
                    bg_color                    =   Es el color del fondo de la ventana
                    fg_color                    =   Es el color de la letra de la ventana
                    tuple_style_letter          =   Contiene una tupla de datos con la informacion referente al tipo de letra


    Ejemplo:
                    Object.set_style_properties(self.lblUser, "black", "white", ("Arial", 12))

---------------------------------------------------------------------------------------------------------
    '''

    def set_style_properties(self, obj_tag, bg_color = None, fg_color = None):
        try:
                
            if bg_color.lower() == 'auto':
                ran_bg = self._get_auto_bg() 
                obj_tag['bg'] = ran_bg

            elif len(bg_color) > 1 and  bg_color.lower() != 'auto':
                obj_tag['bg'] = bg_color 

        except Exception as E_fail_property_bg:
            print(f"Error al asignar la propiedad: bg en el objeto: {type_tag}, excepcion: {E_fail_property_bg}")



        try:
            if len(fg_color) > 1:
                obj_tag['fg'] = fg_color
            elif len(bg_color) > 1 and len(fg_color) < 1:
                self._define_auto_fg(obj_tag, tuple_colors)

        except Exception as E_fail_property_fg:
            print(f"Error al asignar la propiedad: fg en el objeto: {type_tag}, excepcion: {E_fail_property_fg}")



        try:
            if tuple_style_letter != None:
                obj_tag['font'] = StyleFont

        except Exception as E_fail_property_font:
            print(f"Error al asignar la propiedad: font en el objeto: {type_tag}, excepcion: {E_fail_property_font}")


        #self.obj_form.grid(dict_grid)

    '''
---------------------------------------------------------------------------------------------------------
    Metodo:         set_ubication

    Descripcion:    Define laa ubicaciones de un objeto de la clase Tkinter

    Argumentos:
                    obj_tag                     =   Es el objeto en el que se van a realizar las configuraciones 
                    fg_color                    =   Es el color de la letra de la ventana
                    bg_color                    =   Es el color del fondo de la ventana
                    tuple_style_letter          =   Contiene una tupla de datos con la informacion referente al tipo de letra


    Ejemplo:
                    Object.set_ubication(self.lblUser, "white", "black", ("Arial", 12))

---------------------------------------------------------------------------------------------------------
    '''
    def set_ubication(self):
        pass



    def _get_auto_bg(self):

        list_values = []
        for i in range(0, 256):
            list_values.append(i)
            
        r = random.choice(list_values)
        g = random.choice(list_values)
        b = random.choice(list_values)
        RGB = (r, g, b)

        return "#%02x%02x%02x" % RGB


    def _define_auto_fg(self, obj, tuple_rgb_bg):

        r = tuple_rgb_bg[0]
        g = tuple_rgb_bg[1]
        b = tuple_rgb_bg[2]

        if (r < 102 and g < 54 or b < 54) or (g < 102 and r < 54 or b < 54) or (b < 102 and r < 54 or g < 54):
        #g < 102 or b < 102:
            obj['fg'] = "white"
        else:
            obj['fg'] = "black"


    def _get_data_window(self):
            type_tag = self.obj_form.winfo_class()
            print(f"Clase: {type_tag}")

            screen_width = self.obj_form.winfo_screenwidth()
            print(f"Ancho: {screen_width}")

            screen_height = self.obj_form.winfo_screenheight()
            print(f"Altura: {screen_height}")

            obj_form = self.obj_form.winfo_cells()
            print(f"Celdas: {obj_form}")

            visuals = self.obj_form.winfo_visualsavailable()
            print(f"Celdas: {visuals}")
             
        #Este metodo retorna la clase del objeto que se pasa por parametro, es decir
    #si pasamos un label el resultado sera un label, si ingresamos un input la clase sera input, etc
    type_tag = obj_tag.winfo_class()
    #print(f"La clase del objeto ingresado es: {type_tag}")

    #Este metodo retornara informacion referente al ancho de la ventana ingresada
    screen_width = self.obj_form.winfo_screenwidth()
    #print(f"el ancho del objeto ingresado es: {screen_width}")

    #Este metodo retornara informacion referente a la altura de la ventana ingresada
    screen_height = self.obj_form.winfo_screenheight()
    #print(f"La altura del objeto ingresado es: {screen_height}")

    #pendiente de validacion
    window = self.obj_form.winfo_cells()
    #print(f"El numero de celdas dentro del objeto ingresado son: {window}")        
