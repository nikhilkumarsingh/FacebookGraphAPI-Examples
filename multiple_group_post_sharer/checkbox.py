import Tkinter as tk


class CHECKBOX():
    def __init__(self,mylist):
        self.root = tk.Tk()
        self.cb = []     # check_buttons
        self.cb_v = []   # check_button_values
        self.checked = []

        self.frame = tk.Frame(self.root,width=300,height=300)
        self.frame.grid(row = 0,column = 0)
        
        self.vsb = tk.Scrollbar(self.frame, orient="vertical")
        self.text = tk.Text(self.frame, width=40, height=20,bg="light blue", 
                            yscrollcommand=self.vsb.set)
        self.vsb.config(command=self.text.yview)
        self.vsb.pack(side="right", fill="y")
        


        for ix,btext in enumerate(mylist):
            self.cb_v.append(tk.IntVar())
            self.cb.append(tk.Checkbutton(self.frame, text=btext, variable=self.cb_v[ix], command=self.cb_checked, bg = "light blue"))
            self.cb[ix].grid(row=ix, column=0, sticky='w')
            self.text.window_create("end", window=self.cb[ix])
            self.text.insert("end", "\n")

        self.text.pack(side="left", fill="both", expand=True)
        

        self.label = tk.Label(self.root, width=50,bg = 'light green')
        self.label.grid(row=ix+1, column=0, sticky='w')
        self.button_label = tk.Label(self.root, width=20)
        self.button_label.grid(row=ix+2, column=0, sticky='s')
        self.button = tk.Button(self.button_label, text='Done',command = self.result)
        self.button.pack()

        self.root.mainloop()


    def result(self):    
        for ix,item in enumerate(self.cb):
            if self.cb_v[ix].get():
                self.checked.append(1)
            else:
                self.checked.append(0)
        self.root.destroy()

    def cb_checked(self):
        self.label['text'] = ''
        for ix, item in enumerate(self.cb):
            if self.cb_v[ix].get():
                self.label['text'] += item['text'] + '\n'
