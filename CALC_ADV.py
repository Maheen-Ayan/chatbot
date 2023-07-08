import tkinter as tk

def cal():
    calc = tk.Tk()
    calc.geometry("699x699")
    calc.title("ADVANCED CALCULATOR APP")
    calc.config(bg = "#262625")
    def symb(para):
        en = entry1.get()
        data = en + para
        print(data)
        entry1.delete(0,"end")
        entry1.insert(0,data)
        
    def equal():
        en2 = entry1.get()
        entry1.delete(0,"end")
        entry1.insert(0,eval(en2))
        
    entry1 = tk.Entry(calc, width = 30, font = ("times new roman",20))
    entry1.place(x = 70, y = 30)
    bton7 = tk.Button(calc, width = 5, text = "7", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("7"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    bton7.place(x = 70, y = 80)
    bton8 = tk.Button(calc, width = 5, text = "8", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("8"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    bton8.place(x = 170, y = 80)
    bton9 = tk.Button(calc, width = 5, text = "9", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("9"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    bton9.place(x = 270, y = 80)
    pbton = tk.Button(calc, width = 8, text = "+", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("+"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    pbton.place(x = 365, y = 80)
    bton4 = tk.Button(calc, width = 5, text = "4", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("4"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    bton4.place(x = 70, y = 150)
    bton5 = tk.Button(calc, width = 5, text = "5", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("5"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    bton5.place(x = 170, y = 150)
    bton6 = tk.Button(calc, width = 5, text = "6", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("6"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    bton6.place(x = 270, y = 150)
    sbton = tk.Button(calc, width = 8, text = "-", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("-"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    sbton.place(x = 365, y = 150)
    bton1 = tk.Button(calc, width = 5, text = "1", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("1"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    bton1.place(x = 70, y = 220)
    bton2 = tk.Button(calc, width = 5, text = "2", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("2"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    bton2.place(x = 170, y = 220)
    bton3 = tk.Button(calc, width = 5, text = "3", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("3"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    bton3.place(x = 270, y = 220)
    dbton = tk.Button(calc, width = 8, text = "÷", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("/"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    dbton.place(x = 365, y = 220)
    bton0 = tk.Button(calc, width = 5, text = "0", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("0"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    bton0.place(x = 70, y = 290)
    bton00 = tk.Button(calc, width = 5, text = "00", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("00"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    bton00.place(x = 170, y = 290)
    btondot = tk.Button(calc, width = 5, text = ".", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("."),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    btondot.place(x = 270, y = 290)
    tbton = tk.Button(calc, width = 8, text = "×", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:symb("*"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    tbton.place(x = 365, y = 290)
    btoneq = tk.Button(calc, width = 27, text = "=", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = equal,
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    btoneq.place(x = 75, y = 360)
    btonde = tk.Button(calc, width = 27, text = "CLEAR", font = ("Consolas",20),
                    bg= "#296292", fg= "#e8e4e3", command = lambda:entry1.delete(0,"end"),
                    activebackground="#377BB6", activeforeground="#e8e4e3" )
    btonde.place(x = 75, y = 432)
    calc.mainloop()