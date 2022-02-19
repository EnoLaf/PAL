import tkinter
import tkinter.font as tkFont
from PIL            import Image, ImageTk
from tkinter        import ttk

class Functions():

    def show_frame(self, frame):
        showframe = frame.tkraise()
        return showframe


    def create_frame(self, frame, couleur, posX, posY, largeur, hauteur, ancre="nw"):
        frame = tkinter.Frame(frame, bg=couleur)
        frame.place(x=posX, y=posY, anchor=ancre, width=largeur, height=hauteur)
        return frame


    def create_button(self, frame, texte, couleur, showframe, posX, posY, largeur, hauteur, relief="flat", ancre="nw"):
        button= tkinter.Button(frame, text=texte, bg=couleur, command=lambda:self.show_frame(showframe), relief=relief)
        button.place(x=posX, y=posY, anchor=ancre, width=largeur, height=hauteur)
        return button


    def create_button_image(self, frame, img, couleur, showframe, posX, posY):
        button_image = tkinter.Button(frame, image=img, bg=couleur, activebackground=couleur, borderwidth=0, command=lambda:self.show_frame(showframe))
        button_image.place(x=posX, y=posY)
        return button_image


    def create_label(self, frame, texte, couleur, posX, posY, alignement="left"):
        label = tkinter.Label(frame, text=texte, bg=couleur, justify=alignement)
        label.place(x=posX, y=posY)
        return label


    def create_image(self, image):
        path = 'D:/Code/PAL/Images/' + image
        photo_image = ImageTk.PhotoImage(Image.open(path))
        return photo_image

    def create_image_cover(self, image):
        path = 'D:/Code/PAL/Images/Cover/' + image + ".png"
        photo_image_cover = ImageTk.PhotoImage(Image.open(path))
        print("bipboup")
        print(photo_image_cover)

        return photo_image_cover


    def create_canvas(self, frame, img, couleur, posX, posY):
        canvas = tkinter.Canvas(frame, width=img.width(), height=img.height(), bg=couleur, highlightthickness=0)
        canvas.create_image(0,0, anchor=tkinter.NW, image=img)
        canvas.place(x=posX, y=posY, anchor="nw")
        return canvas


    def create_checkbutton(self, frame, texte, couleur, posX, posY, ancre="nw"):
        check_button = tkinter.Checkbutton(frame, text=texte, bg=couleur, offvalue=None, onvalue=texte)
        check_button.place(x=posX, y=posY, anchor=ancre)
        return check_button


    def create_radiobutton(self, frame, texte, couleur, var, valeur, posX, posY, ancre="nw"):
        radio_button = tkinter.Radiobutton(frame, text=texte, bg=couleur, variable=var, value=valeur)
        radio_button.place(x=posX, y=posY, anchor=ancre)
        return radio_button
