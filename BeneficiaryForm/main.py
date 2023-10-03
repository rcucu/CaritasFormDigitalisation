from tkinter import Tk, Frame, Label
from content import MainView
from PIL import Image, ImageTk
from pathlib import Path


if __name__ == '__main__':
    path_dir = Path(r'C:\Users\rcucu\Documents\Bénévolat\Caritas\code')
    lang = 'fr'
    app = Tk()
    app.title('UserForm')
    app.wm_geometry('')

    # form.attributes('-fullscreen', 1)  # make the root window fullscreen
    w_screen = app.winfo_screenwidth()
    h_screen = app.winfo_screenheight()
    main_frame = Frame(app)

    img_bgd_ref = Image.open(path_dir / 'img_bkg3.jpg').resize((w_screen, h_screen))
    img_bgd = ImageTk.PhotoImage(img_bgd_ref)
    bgd_label = Label(main_frame, image=img_bgd)
    bgd_label['anchor'] = 'nw'
    bgd_label.place(x=0, y=0, relwidth=1, relheight=1)

    form = MainView(app, lang)

    form.pack(side="top", fill="both", expand=True)

    app.mainloop()
