import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("Optymalizacja")
        # setting window size
        width = 800
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        func_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        func_label["font"] = ft
        func_label["fg"] = "#333333"
        func_label["justify"] = "center"
        func_label["text"] = "Funkcja"
        func_label.place(x=140, y=20, width=85, height=30)

        run_button = tk.Button(root)
        run_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        run_button["font"] = ft
        run_button["fg"] = "#000000"
        run_button["justify"] = "center"
        run_button["text"] = "RUN!"
        run_button.place(x=330, y=500, width=140, height=50)
        run_button["command"] = self.run_button_command

        alg_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        alg_label["font"] = ft
        alg_label["fg"] = "#333333"
        alg_label["justify"] = "center"
        alg_label["text"] = "Algorytm"
        alg_label.place(x=150, y=90, width=70, height=50)

        func_listbox = tk.Listbox(root)
        func_listbox.insert(1, "Rastrigin")
        func_listbox.insert(2, "Eggholder")
        ft = tkFont.Font(family='Times', size=10)
        func_listbox["font"] = ft
        func_listbox["fg"] = "#333333"
        func_listbox["justify"] = "center"
        func_listbox.place(x=270, y=20, width=130, height=40)
        func_listbox["exportselection"] = "0"
        func_listbox["selectmode"] = "single"

        alg_listbox = tk.Listbox(root)
        alg_listbox.insert(1, "PSO")
        alg_listbox.insert(2, "Genetic")
        ft = tkFont.Font(family='Times', size=10)
        alg_listbox["font"] = ft
        alg_listbox["fg"] = "#333333"
        alg_listbox["justify"] = "center"
        alg_listbox.place(x=270, y=90, width=130, height=40)
        alg_listbox["exportselection"] = "1"
        alg_listbox["listvariable"] = "alglist"
        alg_listbox["selectmode"] = "single"

    def run_button_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
