fif __name__ == "__main__":

    import sys, os
    sys.path.insert(0, '../')

    try:
        from tkinter import *
        from tkinter import ttk
        from tkinter import messagebox as msgbox

    except Exception as e:
        os.system('pip install tk')
        from tkinter import *
        from tkinter import ttk
        from tkinter import messagebox as msgbox

    from obj.app import GUI


# **************************************************
    Form = Tk()
    desing_test_gui = GUI(Form)
    Form.mainloop()
# **************************************************