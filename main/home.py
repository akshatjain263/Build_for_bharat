

from pathlib import Path
from cat_name import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Akshat\OneDrive\Desktop\chatbot dc\main\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
w=window.winfo_screenwidth()
h=window.winfo_screenheight()
x=w/2 -512
y=h/2-440
window.geometry(f"1024x768+{int(x)}+{int(y)}")
window.configure(bg = "#FFFFFF")
# window.eval('tk::PlaceWindow . center')

def start():
    window.destroy()
    category_name()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("home.png"))
image_1 = canvas.create_image(
    512.0,
    384.0,
    image=image_image_1
)

canvas.create_text(
    41.0,
    200.0,
    anchor="nw",
    text="This is a \nConversational Interface\n to help you surf \neasily through the digital\nmarket.",
    fill="#FFFFFF",
    font=("Inter", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("shop_btn.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=start,
    relief="flat"
)
button_1.place(
    x=12.0,
    y=565.0,
    width=336.0,
    height=136.0
)
window.resizable(False, False)
window.mainloop()
