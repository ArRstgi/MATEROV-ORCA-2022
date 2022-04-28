import tkinter as tk
import tkinter.font as tkFont


from Docking.docking import docking_start
from Line_Following.line_following import linefollowing
from Fish_Length_Detection.fish_length import detectFishLength
from Wreck_Length_Detection.wreck_length import detectWreckLength
from Manual.manual_control import stop
from Photomosaic.photomosaic import makemosaic, takeScreenshot

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
        T2End["command"] = self.T2End_command

        Task3=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Task3["font"] = ft
        Task3["fg"] = "#333333"
        Task3["justify"] = "center"
        Task3["text"] = "Task 3"
        Task3.place(x=400,y=70,width=70,height=25)

        T3MakeMosaic=tk.Button(root)
        T3MakeMosaic["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        T3MakeMosaic["font"] = ft
        T3MakeMosaic["fg"] = "#000000"
        T3MakeMosaic["justify"] = "center"
        T3MakeMosaic["text"] = "MAKE MOSAIC"
        T3MakeMosaic.place(x=310,y=180,width=85,height=52)
        T3MakeMosaic["command"] = self.T3MakeMosaic_command

        T3Stop=tk.Button(root)
        T3Stop["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        T3Stop["font"] = ft
        T3Stop["fg"] = "#000000"
        T3Stop["justify"] = "center"
        T3Stop["text"] = "STOP"
        T3Stop.place(x=440,y=180,width=89,height=52)
        T3Stop["command"] = self.T3Stop_command

        fishLength=tk.Button(root)
        fishLength["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        fishLength["font"] = ft
        fishLength["fg"] = "#000000"
        fishLength["justify"] = "center"
        fishLength["text"] = "Fish Length"
        fishLength.place(x=160,y=250,width=70,height=25)
        fishLength["command"] = self.fishLength_command

        wreckLength=tk.Button(root)
        wreckLength["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        wreckLength["font"] = ft
        wreckLength["fg"] = "#000000"
        wreckLength["justify"] = "center"
        wreckLength["text"] = "Wreck Length"
        wreckLength.place(x=330,y=250,width=70,height=25)
        wreckLength["command"] = self.wreckLength_command

        bottomCamera=tk.Button(root)
        bottomCamera["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        bottomCamera["font"] = ft
        bottomCamera["fg"] = "#000000"
        bottomCamera["justify"] = "center"
        bottomCamera["text"] = "Bottom Cam"
        bottomCamera.place(x=450,y=250,width=70,height=25)
        bottomCamera["command"] = self.bottomCamera_command


    def T1Start_command(self):
        docking_start()

    def T1Stop_command(self):
        stop()

    def T2Start_command(self):
        linefollowing()

    def T2End_command(self):
        stop()

    def T3MakeMosaic_command(self):
        makemosaic()

    def T3Stop_command(self):
        stop()

    def fishLength_command(self):
        detectFishLength()

    def wreckLength_command(self):
        detectWreckLength()

    def bottomCamera_command(self):
        takeScreenshot()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
