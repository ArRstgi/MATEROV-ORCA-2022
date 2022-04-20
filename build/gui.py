from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

#from manual_control import task1start, task1stop
#from task2 import task2start, task2stop
from Photomosaic.photomosaic import takescreenshot, makemosaic, task3stop

def fullgui():

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("1209x765")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 765,
        width = 1209,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    canvas.create_rectangle(
        53.0,
        358.0,
        1157.0,
        731.0,
        fill="#000000",
        outline="")

    canvas.create_text(
        314.0,
        452.0,
        anchor="nw",
        text="CAMERA",
        fill="#FFFFFF",
        font=("Inter", 128 * -1)
    )

    canvas.create_text(
        494.0,
        50.0,
        anchor="nw",
        text="Task 2",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        823.0,
        50.0,
        anchor="nw",
        text="Task 3",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        165.0,
        50.0,
        anchor="nw",
        text="Task 1",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_img_t1start = PhotoImage(
            file=relative_to_assets("task 1 start.png"))
    button_t1start = Button(
            image=button_img_t1start,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('task1start()'),
            relief="flat"
        )
    button_t1start.place(
            x=136.0,
            y=94.0,
            width=289.0,
            height=55.0
        )


    button__img_t1stop = PhotoImage(
            file=relative_to_assets('task 1 stop.png'))
    button_t1stop = Button(
            image=button__img_t1stop,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('task1stop()'),
            relief="flat"
        )
    button_t1stop.place(
            x=135.0,
            y=175.0,
            width=289.0,
            height=55.0
        )


    button_img_t2start = PhotoImage(
        file=relative_to_assets("task 2 start.png"))
    button_t2start = Button(
        image=button_img_t2start,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print('task2start()'),
        relief="flat"
    )
    button_t2start.place(
        x=461.0,
        y=94.0,
        width=289.0,
        height=55.0
    )


    button_img_t2stop = PhotoImage(
            file=relative_to_assets("task 2 stop.png"))
    button_t2stop = Button(
            image=button_img_t2stop,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('task2stop()'),
            relief="flat"
        )
    button_t2stop.place(
            x=460.0,
            y=175.0,
            width=289.0,
            height=55.0
        )
        


    button_img_screenshot = PhotoImage(
        file=relative_to_assets("take screenshot.png"))
    button_screenshot = Button(
        image=button_img_screenshot,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: takescreenshot(),
        relief="flat"
    )
    button_screenshot.place(
        x=789.0,
        y=94.0,
        width=289.0,
        height=55.0
    )


    button_img_mosaic = PhotoImage(
        file=relative_to_assets("make mosaic.png"))
    button_mosaic = Button(
        image=button_img_mosaic,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: makemosaic(),
        relief="flat"
    )
    button_mosaic.place(
        x=789.0,
        y=175.0,
        width=289.0,
        height=55.0
    )


    button_img_t3stop = PhotoImage(
        file=relative_to_assets("task 3 stop.png"))
    button_t3stop = Button(
        image=button_img_t3stop,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: task3stop(),
        relief="flat"
    )
    button_t3stop.place(
        x=789.0,
        y=256.0,
        width=289.0,
        height=55.0
    )


    window.resizable(False, False)
    window.mainloop()
















