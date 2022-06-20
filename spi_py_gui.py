import tkinter as tk
"""
https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

"""

# class MyWindow:
    # def __init__(self, win):
        # self.lbl1=Label(win, text='First number')
        # self.lbl2=Label(win, text='Second number')
        # self.lbl3=Label(win, text='Result')
        # self.t1=Entry(bd=3)
        # self.t2=Entry()
        # self.t3=Entry()
        # self.btn1 = Button(win, text='Add')
        # self.btn2=Button(win, text='Subtract')
        # self.lbl1.place(x=100, y=50)
        # self.t1.place(x=200, y=50)
        # self.lbl2.place(x=100, y=100)
        # self.t2.place(x=200, y=100)
        # self.b1=Button(win, text='Add', command=self.add)
        # self.b2=Button(win, text='Subtract')
        # self.b2.bind('<Button-1>', self.sub)
        # self.b1.place(x=100, y=150)
        # self.b2.place(x=200, y=150)
        # self.lbl3.place(x=100, y=200)
        # self.t3.place(x=200, y=200)
        
        # v0=IntVar()
        # v0.set(1)
        # self.r1=Radiobutton(win, text="male", variable=v0,value=1)
        # self.r2=Radiobutton(win, text="female", variable=v0,value=2)
        # self.r1.place(x=220, y=200)
        # self.r2.place(x=220, y=240)
        
        # # menu
        # #menubar = MenuBar(self)
        # #self.config(menu=menubar) was using inherited app properties
        
    # def add(self):
        # self.t3.delete(0, 'end')
        # num1=int(self.t1.get())
        # num2=int(self.t2.get())
        # result=num1+num2
        # self.t3.insert(END, str(result))
    # def sub(self, event):
        # self.t3.delete(0, 'end')
        # num1=int(self.t1.get())
        # num2=int(self.t2.get())
        # result=num1-num2
        # self.t3.insert(END, str(result))

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        
        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=menu_file)
        
        # menu_file = tk.Menu(self, tearoff=0)
        # self.add_cascade(label="Menu1", menu=menu_file)
        # menu_file.add_command(label="All Widgets", command=lambda: parent.show_frame(Some_Widgets))
        # menu_file.add_separator()
        # menu_file.add_command(label="Exit Application", command=lambda: parent.Quit_application())

        # menu_orders = tk.Menu(self, tearoff=0)
        # self.add_cascade(label="Menu2", menu=menu_orders)

        # menu_pricing = tk.Menu(self, tearoff=0)
        # self.add_cascade(label="Menu3", menu=menu_pricing)
        # menu_pricing.add_command(label="Page One", command=lambda: parent.show_frame(PageOne))

        # menu_operations = tk.Menu(self, tearoff=0)
        # self.add_cascade(label="Menu4", menu=menu_operations)
        # menu_operations.add_command(label="Page Two", command=lambda: parent.show_frame(PageTwo))
        # menu_positions = tk.Menu(menu_operations, tearoff=0)
        # menu_operations.add_cascade(label="Menu5", menu=menu_positions)
        # menu_positions.add_command(label="Page Three", command=lambda: parent.show_frame(PageThree))
        # menu_positions.add_command(label="Page Four", command=lambda: parent.show_frame(PageFour))

        # menu_help = tk.Menu(self, tearoff=0)
        # self.add_cascade(label="Menu6", menu=menu_help)
        # menu_help.add_command(label="Open New Window", command=lambda: parent.OpenNewWindow())
        
class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        # self.resizable(0, 0) prevents the app from being resized
        # self.geometry("1024x600") fixes the applications size
        self.frames = {}
        pages = (PageOne)#(Some_Widgets, PageOne, PageTwo, PageThree, PageFour)
        # for F in pages:
            # frame = F(main_frame, self)
            # self.frames[F] = frame
            # frame.grid(row=0, column=0, sticky="nsew")
        frame = PageOne(main_frame, self)
        self.frames[PageOne] = frame
        frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(PageOne)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def OpenNewWindow(self):
        OpenNewWindow()

    def Quit_application(self):
        self.destroy()

class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#EFF6F5", height=600, width=1024)
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

class PageOne(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="SPI PY GUI")
        
        v1=tk.IntVar()
        v1.set(1)
        self.r1=tk.Radiobutton(self.main_frame, text="Load an excel sheet", variable=v1,value=1)
        self.r2=tk.Radiobutton(self.main_frame, text="Open a spec", variable=v1,value=2)
        self.r3=tk.Radiobutton(self.main_frame, text="Create a spec", variable=v1,value=3)
        self.r1.place(x=220, y=200)
        self.r2.place(x=220, y=240)
        self.r3.place(x=220, y=260)
        label1.pack(side="top")
        

def create_user_window():
    root = MyApp()
    root.title("Smart Plant Instrumentation GUI")
    root.geometry("400x300+10+10")
    root.mainloop()