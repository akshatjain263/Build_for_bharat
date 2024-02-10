
    # This file was generated by the Tkinter Designer by Parth Jadhav
    # https://github.com/ParthJadhav/Tkinter-Designer

from name import *
from cate import *
def category_name():
    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Akshat\OneDrive\Desktop\chatbot dc\main\assets")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    # window.geometry("1200x768")
    w=window.winfo_screenwidth()
    h=window.winfo_screenheight()
    x=w/2 -600
    y=h/2-440
    window.geometry(f"1200x768+{int(x)}+{int(y)}")
    window.configure(bg = "#FFFFFF")

    def subcateg(sb):
        window.destroy()
        subcate(sb)
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 768,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("bg_2.png"))
    image_1 = canvas.create_image(
        606.0,
        384.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("name_inp.png"))
    entry_bg_1 = canvas.create_image(
        265.0,
        177.0,
        image=entry_image_1
    )
    name_inp = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        font=("verdana",12),
        highlightthickness=0
    )
    name_inp.place(
        x=40.0,
        y=142.0,
        width=450.0,
        height=68.0
    )
    def sbyname(temp):
        name=name_inp.get()
        window.destroy()
        name_search(name)
    name_inp.bind("<Return>",sbyname)
    canvas.create_text(
        40.0,
        106.0,
        anchor="nw",
        text="search product by name :",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        40.0,
        267.0,
        anchor="nw",
        text="Browse through categories :",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("elec_button.png"))
    elec_btn = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: subcateg("electronics"),
        relief="flat"
    )
    elec_btn.place(
        x=40.0,
        y=334.0,
        width=350.0,
        height=50.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("kitchen_button.png"))
    kitchen_btn = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: subcateg("kitchen"),
        relief="flat"
    )
    kitchen_btn.place(
        x=40.0,
        y=658.0,
        width=350.0,
        height=50.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("fit_btn.png"))
    fit_btn = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: subcateg("fitness"),
        relief="flat"
    )
    fit_btn.place(
        x=40.0,
        y=577.0,
        width=350.0,
        height=50.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("furn_btn.png"))
    furn_btn = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: subcateg("furniture"),
        relief="flat"
    )
    furn_btn.place(
        x=40.0,
        y=496.0,
        width=350.0,
        height=50.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("cloth_btn.png"))
    cloth_btn = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: subcateg("clothing"),
        relief="flat"
    )
    cloth_btn.place(
        x=40.0,
        y=415.0,
        width=350.0,
        height=50.0
    )
    window.resizable(False, False)
    # window.eval('tk::PlaceWindow . center')
    window.mainloop()
