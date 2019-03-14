import tkinter as tk

LARGE_FONT=("Veranda",12)
class DataForLibrary(tk.Tk):

    def _init_(self,*args,**kwargs):
        tk.Tk._init_(self,*args,**kwargs)
        container=tk.Frame(self)

        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnFigure(0,weight=1)

        self.frames={}

        frame=StartPage(container,self)

        self.frames[StartPage]=frame

        frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):

        frame=self.frames[cont]
        frame=tk.tkraise()

class StartPage(tk.Frame):

    def _init_(self,parent,controller):
        tk.Frame._init_(self,Parent)
        label=tk.Label(self,text="Start Page",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

app=DataForLibrary()
app.mainloop
