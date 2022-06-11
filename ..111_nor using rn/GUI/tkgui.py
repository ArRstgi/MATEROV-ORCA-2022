from email.mime import image
import tkinter as tk
import tkinter.font as tkFont
from Fish_Length_Detection.fish_length import detectFishLength
from Wreck_Length_Detection.wreck_length import detectWreckLength

from photomosaic_A import takeScreenshot, makemosaic
from Fish_Length_Detection.fish_length import detectFishLength
from Wreck_Length_Detection.wreck_length import detectWreckLength

class App:
    def __init__(self, root):
        #setting title
        root.title("ORCA Robotics GUI")
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
        GLabel_433.config(bg = "black")
        GLabel_433["justify"] = "center"
        GLabel_433["text"] = ""
        GLabel_433.place(x=70,y=0,width=760,height=558)

        GLabel_381=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_381["font"] = ft
        GLabel_381["fg"] = "#333333"
        GLabel_381.config(bg = "grey20")
        GLabel_381["justify"] = "center"
        GLabel_381["text"] = ""
        GLabel_381.place(x=0,y=0,width=73,height=558)

        lineFollower= tk.Button(root)#, image = tk.PhotoImage(file = r"linefollower.png"))
        lineFollower["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        lineFollower["font"] = ft
        lineFollower["fg"] = "#000000"
        lineFollower["justify"] = "center"
        lineFollower["text"] = ""
        lineFollower.place(x=130,y=30,width=66,height=65)
        lineFollower["command"] = self.lineFollower_command

        lfText=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lfText["font"] = ft
        lfText["fg"] = "#ffffff"
        lfText.config(bg = "black")
        lfText["justify"] = "center"
        lfText["text"] = "Line Follower"
        lfText.place(x=135,y=100,width=64,height=10)

        mortDetection=tk.Button(root)
        mortDetection["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        mortDetection["font"] = ft
        mortDetection["fg"] = "#000000"
        mortDetection["justify"] = "center"
        mortDetection["text"] = ""
        mortDetection.place(x=280,y=30,width=65,height=65)
        mortDetection["command"] = self.mortDetection_command

        mdText=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        mdText["font"] = ft
        mdText["fg"] = "#ffffff"
        mdText.config(bg = "black")
        mdText["justify"] = "center"
        mdText["text"] = "Mort Detection"
        mdText.place(x=280,y=100,width=68,height=10)

        fishLength=tk.Button(root)
        fishLength["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        fishLength["font"] = ft
        fishLength["fg"] = "#000000"
        fishLength["justify"] = "center"
        fishLength["text"] = ""
        fishLength.place(x=430,y=30,width=65,height=65)
        fishLength["command"] = self.fishLength_command

        flText=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        flText["font"] = ft
        flText["fg"] = "#ffffff"
        flText.config(bg = "black")
        flText["justify"] = "center"
        flText["text"] = "Fish Length"
        flText.place(x=435,y=100,width=55,height=10)

        wreckLength=tk.Button(root)
        wreckLength["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        wreckLength["font"] = ft
        wreckLength["fg"] = "#000000"
        wreckLength["justify"] = "center"
        wreckLength["text"] = ""
        wreckLength.place(x=580,y=30,width=65,height=65)
        wreckLength["command"] = self.wreckLength_command

        wlText=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        wlText["font"] = ft
        wlText["fg"] = "#ffffff"
        wlText.config(bg = "black")
        wlText["justify"] = "center"
        wlText["text"] = "Wreck Length"
        wlText.place(x=581,y=100,width=63,height=10)

        docking=tk.Button(root)
        docking["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        docking["font"] = ft
        docking["fg"] = "#000000"
        docking["justify"] = "center"
        docking["text"] = ""
        docking.place(x=205,y=120,width=65,height=65)
        docking["command"] = self.docking_command

        dText=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        dText["font"] = ft
        dText["fg"] = "#ffffff"
        dText.config(bg = "black")
        dText["justify"] = "center"
        dText["text"] = "Docking "
        dText.place(x=220,y=190,width=40,height=10)

        photomosaic=tk.Button(root)
        photomosaic["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        photomosaic["font"] = ft
        photomosaic["fg"] = "#000000"
        photomosaic["justify"] = "center"
        photomosaic["text"] = ""
        photomosaic.place(x=510,y=120,width=65,height=65)
        photomosaic["command"] = self.photomosaic_command

        pText=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        pText["font"] = ft
        pText["fg"] = "#ffffff"
        pText.config(bg = "black")
        pText["justify"] = "center"
        pText["text"] = "Photomosaic"
        pText.place(x=514,y=190,width=58,height=10)

        startScreenshot=tk.Button(root)
        startScreenshot["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        startScreenshot["font"] = ft
        startScreenshot["fg"] = "#000000"
        startScreenshot["justify"] = "center"
        startScreenshot["text"] = ""
        startScreenshot.place(x=360,y=120,width=65,height=65)
        startScreenshot["command"] = self.startScreenshot_command

        ssText=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        ssText["font"] = ft
        ssText["fg"] = "#ffffff"
        ssText.config(bg = "black")
        ssText["justify"] = "center"
        ssText["text"] = "Start Screenshot"
        ssText.place(x=357,y=190,width=73,height=10)

    def lineFollower_command(self):
        print("linefollower()")


    def mortDetection_command(self):
        print("mortdetection()")


    def fishLength_command(self):
        detectFishLength()


    def wreckLength_command(self):
        detectWreckLength()


    def docking_command(self):
        print("docking()")


    def photomosaic_command(self):
        makemosaic()


    def startScreenshot_command(self):
        takeScreenshot()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

