import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        T1Start=tk.Button(root)
        T1Start["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        T1Start["font"] = ft
        T1Start["fg"] = "#000000"
        T1Start["justify"] = "center"
        T1Start["text"] = "Start"
        T1Start.place(x=70,y=110,width=70,height=25)
        T1Start["command"] = self.T1Start_command

        Task1=tk.Label(root)
        Task1["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        Task1["font"] = ft
        Task1["fg"] = "#333333"
        Task1["justify"] = "center"
        Task1["text"] = "Task 1"
        Task1.place(x=70,y=60,width=72,height=44)

        T1Stop=tk.Button(root)
        T1Stop["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        T1Stop["font"] = ft
        T1Stop["fg"] = "#000000"
        T1Stop["justify"] = "center"
        T1Stop["text"] = "Stop"
        T1Stop.place(x=70,y=150,width=70,height=25)
        T1Stop["command"] = self.T1Stop_command

        Task2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Task2["font"] = ft
        Task2["fg"] = "#333333"
        Task2["justify"] = "center"
        Task2["text"] = "Task 2"
        Task2.place(x=180,y=70,width=70,height=25)

        T2Start=tk.Button(root)
        T2Start["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        T2Start["font"] = ft
        T2Start["fg"] = "#000000"
        T2Start["justify"] = "center"
        T2Start["text"] = "Start"
        T2Start.place(x=180,y=110,width=70,height=25)
        T2Start["command"] = self.T2Start_command

        T2End=tk.Button(root)
        T2End["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        T2End["font"] = ft
        T2End["fg"] = "#000000"
        T2End["justify"] = "center"
        T2End["text"] = "End"
        T2End.place(x=180,y=150,width=70,height=25)
        T2End["command"] = self.GT2End_command

        Task3=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Task3["font"] = ft
        Task3["fg"] = "#333333"
        Task3["justify"] = "center"
        Task3["text"] = "Task 3"
        Task3.place(x=400,y=70,width=70,height=25)

        SS2=tk.Button(root)
        SS2["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        SS2["font"] = ft
        SS2["fg"] = "#000000"
        SS2["justify"] = "center"
        SS2["text"] = "SS 2"
        SS2.place(x=360,y=100,width=70,height=25)
        SS2["command"] = self.SS2_command

        SS1=tk.Button(root)
        SS1["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        SS1["font"] = ft
        SS1["fg"] = "#000000"
        SS1["justify"] = "center"
        SS1["text"] = "SS 1"
        SS1.place(x=280,y=100,width=70,height=25)
        SS1["command"] = self.SS1_command

        T3MakeMosaic=tk.Button(root)
        T3MakeMosaic["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        T3MakeMosaic["font"] = ft
        T3MakeMosaic["fg"] = "#000000"
        T3MakeMosaic["justify"] = "center"
        T3MakeMosaic["text"] = "MAKE MOSAIC"
        T3MakeMosaic.place(x=310,y=180,width=85,height=52)
        T3MakeMosaic["command"] = self.T3MakeMosaic_command

        SS7=tk.Button(root)
        SS7["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        SS7["font"] = ft
        SS7["fg"] = "#000000"
        SS7["justify"] = "center"
        SS7["text"] = "SS 6"
        SS7.place(x=360,y=140,width=70,height=25)
        SS7["command"] = self.SS7_command

        T3Stop=tk.Button(root)
        T3Stop["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        T3Stop["font"] = ft
        T3Stop["fg"] = "#000000"
        T3Stop["justify"] = "center"
        T3Stop["text"] = "STOP"
        T3Stop.place(x=440,y=180,width=89,height=52)
        T3Stop["command"] = self.T3Stop_command

        SS7=tk.Button(root)
        SS7["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        SS7["font"] = ft
        SS7["fg"] = "#000000"
        SS7["justify"] = "center"
        SS7["text"] = "SS 7"
        SS7.place(x=440,y=140,width=70,height=25)
        SS7["command"] = self.SS7_command

        SS8=tk.Button(root)
        SS8["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        SS8["font"] = ft
        SS8["fg"] = "#000000"
        SS8["justify"] = "center"
        SS8["text"] = "SS 8"
        SS8.place(x=520,y=140,width=70,height=25)
        SS8["command"] = self.SS8_command

        SS4=tk.Button(root)
        SS4["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        SS4["font"] = ft
        SS4["fg"] = "#000000"
        SS4["justify"] = "center"
        SS4["text"] = "SS 4"
        SS4.place(x=520,y=100,width=70,height=25)
        SS4["command"] = self.SS4_command

        SS3=tk.Button(root)
        SS3["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        SS3["font"] = ft
        SS3["fg"] = "#000000"
        SS3["justify"] = "center"
        SS3["text"] = "SS 3"
        SS3.place(x=440,y=100,width=70,height=25)
        SS3["command"] = self.SS3_command

        SS5=tk.Button(root)
        SS5["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        SS5["font"] = ft
        SS5["fg"] = "#000000"
        SS5["justify"] = "center"
        SS5["text"] = "SS 5"
        SS5.place(x=280,y=140,width=70,height=25)
        SS5["command"] = self.SS5_command

    def T1Start_command(self):
        print("command")


    def T1Stop_command(self):
        print("command")


    def T2Start_command(self):
        print("command")


    def GT2End_command(self):
        print("command")


    def SS2_command(self):
        print("command")


    def SS1_command(self):
        print("command")


    def T3MakeMosaic_command(self):
        print("command")


    def SS7_command(self):
        print("command")


    def T3Stop_command(self):
        print("command")


    def SS7_command(self):
        print("command")


    def SS8_command(self):
        print("command")


    def SS4_command(self):
        print("command")


    def SS3_command(self):
        print("command")


    def SS5_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

