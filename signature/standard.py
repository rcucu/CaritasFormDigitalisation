from pathlib import Path
from tkinter import Button, Canvas

from PIL import Image, ImageDraw

from windows.standard_format import Window


class SignatureWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.text_form = parent.form
        self.path_dir_save = Path(r'C:\Users\rcucu\Documents\Bénévolat\Caritas\code\data')
        self.posx, self.posy = 50, 300
        self.sizex, self.sizey = 600, 200
        self.xold, self.yold = None, None
        self.b1 = 'up'
        self.drawing_area = Canvas(self, width=self.sizex, height=self.sizey, bg='white')
        self.drawing_area.place(x=self.posx, y=self.posy)
        self.drawing_area.bind('<Motion>', self.motion)
        self.drawing_area.bind('<ButtonPress-1>', self.b1down)
        self.drawing_area.bind('<ButtonRelease-1>', self.b1up)
        self.butt_done = Button(self, text='Enregistrer', width=10, command=self.save, bg='white')
        self.butt_done.place(x=(self.sizex / 6), y=2.5 * self.sizey + 20)
        self.butt_erase = Button(self, text='Effacer', width=10, command=self.clear, bg='white')
        self.butt_erase.place(x=(self.sizex / 6) + 80, y=2.5 * self.sizey + 20)

        self.image = Image.new('RGB', (self.sizex, self.sizey), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

    def get_text_label(self, number):
        return self.text_form.get_field_text(number)

    def b1down(self, event):
        self.b1 = 'down'

    def b1up(self, event):
        self.b1 = 'up'
        self.xold = None
        self.yold = None

    def save(self, filename):
        self.image.save(filename)

    def clear(self):
        print(f' clear: {self.b1}')
        self.drawing_area.delete('all')
        self.image = Image.new('RGB', (self.sizex, self.sizey), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        print('canvas erased')

    def motion(self, event):
        print(self.b1)
        # thickness = 4
        # x1, y1 = (event.x - thickness), (event.y - thickness)
        # x2, y2 = (event.x + thickness), (event.y + thickness)
        # event.widget.create_oval(x1, y1, x2, y2, fill='black')

        if self.b1 == 'down':
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold, self.yold, event.x, event.y, smooth='true', width=3, fill='black')
                self.draw.line(((self.xold, self.yold), (event.x, event.y)), (0, 0, 0), width=3)

        self.xold = event.x
        self.yold = event.y
