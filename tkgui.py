import tkinter as tk
import tkinter.font as tkFont

from Photomosaic.photomosaic import makemosaic

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=828
        height=558
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_433=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_433["font"] = ft
        GLabel_433["fg"] = "#333333"
        GLabel_433["justify"] = "center"
        GLabel_433["text"] = ""
        GLabel_433.place(x=70,y=0,width=755,height=556)

        GLabel_381=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_381["font"] = ft
        GLabel_381["fg"] = "#333333"
        GLabel_381["justify"] = "center"
        GLabel_381["text"] = ""
        GLabel_381.place(x=0,y=0,width=73,height=554)

        lineFollower=tk.Button(root)
        lineFollower["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        lineFollower["font"] = ft
        lineFollower["fg"] = "#000000"
        lineFollower["justify"] = "center"
        lineFollower["text"] = ""
        lineFollower.place(x=130,y=30,width=63,height=51)
        lineFollower["command"] = self.lineFollower_command

        GLabel_738=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_738["font"] = ft
        GLabel_738["fg"] = "#333333"
        GLabel_738["justify"] = "center"
        GLabel_738["text"] = "line follower"
        GLabel_738.place(x=130,y=80,width=70,height=25)

        mortDetection=tk.Button(root)
        mortDetection["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        mortDetection["font"] = ft
        mortDetection["fg"] = "#000000"
        mortDetection["justify"] = "center"
        mortDetection["text"] = ""
        mortDetection.place(x=260,y=30,width=57,height=49)
        mortDetection["command"] = self.mortDetection_command

        GLabel_861=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_861["font"] = ft
        GLabel_861["fg"] = "#333333"
        GLabel_861["justify"] = "center"
        GLabel_861["text"] = "mort detection"
        GLabel_861.place(x=250,y=70,width=86,height=42)

        fishLength=tk.Button(root)
        fishLength["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        fishLength["font"] = ft
        fishLength["fg"] = "#000000"
        fishLength["justify"] = "center"
        fishLength["text"] = ""
        fishLength.place(x=410,y=30,width=66,height=50)
        fishLength["command"] = self.fishLength_command

        GLabel_90=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_90["font"] = ft
        GLabel_90["fg"] = "#333333"
        GLabel_90["justify"] = "center"
        GLabel_90["text"] = "Fish Length"
        GLabel_90.place(x=400,y=70,width=87,height=37)

        wreckLength=tk.Button(root)
        wreckLength["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        wreckLength["font"] = ft
        wreckLength["fg"] = "#000000"
        wreckLength["justify"] = "center"
        wreckLength["text"] = ""
        wreckLength.place(x=530,y=30,width=63,height=50)
        wreckLength["command"] = self.wreckLength_command

        GLabel_217=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_217["font"] = ft
        GLabel_217["fg"] = "#333333"
        GLabel_217["justify"] = "center"
        GLabel_217["text"] = "Wreck Length"
        GLabel_217.place(x=520,y=80,width=92,height=30)

        docking=tk.Button(root)
        docking["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        docking["font"] = ft
        docking["fg"] = "#000000"
        docking["justify"] = "center"
        docking["text"] = ""
        docking.place(x=210,y=120,width=54,height=48)
        docking["command"] = self.docking_command

        GLabel_762=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_762["font"] = ft
        GLabel_762["fg"] = "#333333"
        GLabel_762["justify"] = "center"
        GLabel_762["text"] = "docking "
        GLabel_762.place(x=200,y=160,width=68,height=30)

        photomosaic=tk.Button(root)
        photomosaic["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        photomosaic["font"] = ft
        photomosaic["fg"] = "#000000"
        photomosaic["justify"] = "center"
        photomosaic["text"] = ""
        photomosaic.place(x=480,y=120,width=60,height=50)
        photomosaic["command"] = self.photomosaic_command

        GLabel_209=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_209["font"] = ft
        GLabel_209["fg"] = "#333333"
        GLabel_209["justify"] = "center"
        GLabel_209["text"] = "photomosaic"
        GLabel_209.place(x=470,y=160,width=82,height=30)

        startScreenshot=tk.Button(root)
        startScreenshot["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        startScreenshot["font"] = ft
        startScreenshot["fg"] = "#000000"
        startScreenshot["justify"] = "center"
        startScreenshot["text"] = ""
        startScreenshot.place(x=340,y=120,width=56,height=48)
        startScreenshot["command"] = self.startScreenshot_command

        GLabel_398=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_398["font"] = ft
        GLabel_398["fg"] = "#333333"
        GLabel_398["justify"] = "center"
        GLabel_398["text"] = "start screenshot"
        GLabel_398.place(x=320,y=170,width=98,height=30)

    def lineFollower_command(self):
        print("linefollower()")


    def mortDetection_command(self):
        print("mortdetection()")


    def fishLength_command(self):
        print("fishlength()")


    def wreckLength_command(self):
        print("wrecklength()")


    def docking_command(self):
        print("docking()")


    def photomosaic_command(self):
        makemosaic()


    def startScreenshot_command(self):
        print("takescreenshot()")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
