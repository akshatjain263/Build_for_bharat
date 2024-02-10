ot_ele=[]
# from cat_name import *
from name import *
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
def subcate(cat):
    global window 
    import pandas as pd
    import webbrowser
    from pathlib import Path

    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Akshat\OneDrive\Desktop\chatbot dc\main\assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    def display_subcat(cat):
        df=pd.read_csv("final.csv")
        df=df[df['main_category'].str.lower().str.contains(cat.lower())]
        # print(df)
        l=len(df['sub_category'].value_counts())
        for i in range(l):
            subcat=df['sub_category'].value_counts().keys()[i]
            button_1 = Button(
                bg="yellow",
                text=subcat,
                borderwidth=0,
                highlightthickness=0,
                command=lambda sb=subcat:display(sb),
                relief="flat",
                font=('verdana',12)
            )
            button_1.place(
                x=95.0+240*i,
                y=50.0,
                width=230.0,
                height=54.0
            )
    root = Tk()
    w=root.winfo_screenwidth()
    h=root.winfo_screenheight()
    x=w/2 -600
    y=h/2-440
    root.geometry(f"1200x768+{int(x)}+{int(y)}")



    canvas = Canvas(
        root,
        # bg = "#01EFFF",
        height = 768,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    def enter(tag):
        canvas.config(cursor="hand2")

    def leave(tag):
        canvas.config(cursor="")
    def on_c(link,event):
        webbrowser.open_new(link) 
    def display(user):
        image_image_2 = PhotoImage(
        file=relative_to_assets("col_grad.png"))
        image_2 = canvas.create_image(
            600.0,
            266.0,
            image=image_image_2
        )

        canvas.create_text(
            67.0,
            236.0,
            anchor="nw",
            text="Name               Rating       Price          Link to Buy",
            fill="#FFFFFF",
            font=("Inter", 50 * -1)
        )
        global ot_ele
        for i in ot_ele:
            canvas.delete(i)
        ot_ele=[]
        print(user)
        df=pd.read_csv("final.csv")
        # df['name']=df['name'].str.lower()
        user=user.lower()
        df=df[df['sub_category'].str.lower().str.contains(user)]
        l=min(len(df),5)
        if(l==0):
            return 0
        for i in range(l):
            rec=df.iloc[i]
            # canvas.create_rectangle()
            r1=canvas.create_rectangle(
                40.0,
                311.0+i*85,
                396.0,
                396.0+i*85,
                fill="#D9D9D9",
                outline=""
            )
            t1=canvas.create_text(
                50.0,
                323.0+i*85,
                anchor="nw",
                text=rec['name'],
                fill="#000000",
                font=("Inter", 18 * -1)
            )

            r2=canvas.create_rectangle(
                396.0,
                311.0+i*85,
                550.0,
                396.0+i*85,
                fill="#D9D9D9",
                outline="")

            r3=canvas.create_rectangle(
                550.0,
                311.0+i*85,
                893.0,
                396.0+i*85,
                fill="#D9D9D9",
                outline="")

            t2=canvas.create_text(
                676.0,
                323.0+i*85,
                anchor="nw",
                text=rec['price'],
                fill="#000000",
                font=("Inter", 25 * -1)
            )

            r4=canvas.create_rectangle(
                893.0,
                311.0+i*85,
                1160.0,
                396.0+i*85,
                fill="#D9D9D9",
                outline="")

            link=canvas.create_text(
                916.0,
                323.0+i*85,
                anchor="nw",
                text="Click to Buy",
                fill="#000000",
                font=("Inter", 25 * -1)
            )
            canvas.tag_bind(link, '<Enter>', enter)
            canvas.tag_bind(link, '<Leave>', leave)
            canvas.tag_bind(link,'<ButtonPress-1>',lambda event,link=rec['link'] : on_c(link,event))
            t3=canvas.create_text(
                457.0,
                323.0+i*85,
                anchor="nw",
                text=rec['ratings'],
                fill="#000000",
                font=("Inter", 25 * -1)
            )
            ot_ele=ot_ele+[r1,r2,r3,r4,t1,t2,t3,link]
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("bg_name.png"))
    image_1 = canvas.create_image(
        600.0,
        384.0,
        image=image_image_1
    )
    def ret():
        root.destroy()
        category_name()
    btn1=Button(root,text="Back",command=ret,bg='yellow')
    btn1.place(
        relx=0.9,
        y=50.0,
        width=100,
        height=54.0
    )
    display_subcat(cat)
    root.resizable(False, False)
    root.mainloop()
