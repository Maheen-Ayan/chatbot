import tkinter as tk
from string import punctuation,digits

def code():
    user = tk.Tk()
    user.geometry("600x600")
    user.title("PASSWORD CHECKER APP")
    user.config(bg = "midnightblue")

    entry1 = tk.Entry(user, width = 35, highlightbackground = "#000000", font =("times new roman", 20),
                    highlightthickness = 3)
    entry1.place(x = 50, y = 50)
    bton1 = tk.Button(user, width = 53, text = "CHECK PASSWORD", font = ("cambria, 13"),
                    bg = "#fffa78", fg = "slateblue", activebackground = "cornsilk",
                    activeforeground = "mediumslateblue", command = lambda:pc(entry1.get()))
    bton1.place(x = 56, y = 100)
    lb1 = tk.Label(user, text = "LENGTH", fg = "#fffa78", bg = "midnightblue",
                font = ("times new roman", 20))
    lb1.place(x = 50, y = 150)
    lb2 = tk.Label(user, text = "SPECIAL CHARS", fg = "#fffa78", bg = "midnightblue", 
                font = ("times new roman", 20))
    lb2.place(x = 50, y = 200)
    lb3 = tk.Label(user, text = "CASE", fg = "#fffa78", bg = "midnightblue",
                font = ("times new roman", 20))
    lb3.place(x = 50, y = 250)
    lb4 = tk.Label(user, text = "NUMBERS", fg = "#fffa78", bg = "midnightblue",
                font = ("times new roman", 20))
    lb4.place(x = 50, y = 300)
    lb5 = tk.Label(user, fg = "#fffa78", bg = "midnightblue", 
                font = ("times new roman", 20))
    lb5.place(x = 420, y = 150)
    lb6 = tk.Label(user, fg = "#fffa78", bg = "midnightblue",
                font = ("times new roman", 20))
    lb6.place(x = 420, y = 200)
    lb7 = tk.Label(user, fg = "#fffa78", bg = "midnightblue",
                font = ("times new roman", 20))
    lb7.place(x = 420, y = 250)
    lb8 = tk.Label(user, fg = "#fffa78", bg = "midnightblue",
                font = ("times new roman", 20))
    lb8.place(x = 420, y = 300)
    def pc(password):
        
        marks = {'LENGTH':0, 'SPECIAL CHARS': 0, 'CASE': 0, 'NUMS': 0}
        if len(password) > 8:
            marks['LENGTH'] = 100
            lb5.config(text = 'PASS', fg = 'springgreen')
        else:
            lb5.config(text = "FAIL", fg = "red")

            
        for i in password:
            if i.islower() == True:
                marks['CASE'] += 50
                break
            
        for i in password:
            if i.isupper() == True:
                marks['CASE'] += 50
                break
            
        for i in password:
            if i in punctuation:
                marks['SPECIAL CHARS'] = 100
                lb6.config(text = 'PASS', fg = 'springgreen')
                break
            else:
                lb6.config(text = "FAIL", fg = "red")
            
        for i in password:
            if i in digits:
                marks['NUMS'] = 100
                lb8.config(text = 'PASS', fg = 'springgreen')
                break
            else:
                lb8.config(text = "FAIL", fg = "red")

        if marks["CASE"] == 100:
            lb7.config(text = "PASS", fg = "springgreen")
        else:
            lb7.config(text = "FAIL", fg = "red")
        print(marks)
    tk.mainloop()
