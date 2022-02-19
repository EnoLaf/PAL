import tkinter
import tkinter.font as tkFont
from PIL            import Image, ImageTk
from tkinter        import ttk
from utiles         import Functions
import sys

sys.path.append("D:\Code\PAL")
from Backend.mainv2 import read_a_book

F = Functions()

color1 = '#F6E5D4'
color2 = '#DCCCB5'
color3 = '#A66254'

# Création de la fenêtre + paramètrage
app = tkinter.Tk()              # Initialisation de tkinter
app.geometry("1000x600+0+0")   # Dimmensionnement de la fenêtre
app.title("PAL")                # Définir titre de la fenêtre
app['bg'] = color1              # Définir la couleur du fond

icon_return = F.create_image("menu_close.png")
cover1       = F.create_image_cover("les-100-tome-2-21-jour")
cover2       = F.create_image_cover("la-cite-du-ciel-tome-1")
cover3       = F.create_image_cover("le-cycle-de-dune-tome-1-dune")
cover4       = F.create_image_cover("le-prieure-de-loranger")

#==================================Menu=========================================
frame_menu      = F.create_frame(app, color1, 0, 0, 1000, 600)
frame_central   = F.create_frame(frame_menu, color3, 200, 0, 600, 600)

#==============================Livre choisi=====================================
# frame_chosen_book       = F.create_frame(app, color1, 0, 0, 1000, 600)
# frame_chosen_book_left  = F.create_frame(frame_chosen_book, color3, 0, 0, 250, 600)
# frame_chosen_book_right = F.create_frame(frame_chosen_book, color3, 975, 0, 25, 600)
# frame_chosen_book_canva = F.create_frame(frame_chosen_book, color1, 100, 100, 300, 400)
# return_button5          = F.create_button_image(frame_chosen_book, icon_return, color3, frame_menu, 25, 25)

#==============================Ajouter un livre=================================
frame_add       = F.create_frame(app, color1, 0, 0, 1000, 600)
frame_add_left  = F.create_frame(frame_add, color3, 0, 0, 250, 600)
frame_add_right = F.create_frame(frame_add, color3, 975, 0, 25, 600)
canva_add_cover = F.create_canvas(frame_add, cover4, color1, 100, 100)
return_button1  = F.create_button_image(frame_add, icon_return, color3, frame_menu, 25, 25)

#============================Supprimer un livre=================================
frame_delete        = F.create_frame(app, color1, 0, 0, 1000, 600)
frame_delete_top    = F.create_frame(frame_delete, color3, 0, 0, 1000, 175)
frame_delete_bottom = F.create_frame(frame_delete, color3, 0, 575, 1000, 25)
return_button2      = F.create_button_image(frame_delete, icon_return, color3, frame_menu, 25, 25)

#================================Livre lus======================================
frame_books         = F.create_frame(app, color1, 0, 0, 1000, 600)
frame_books_top     = F.create_frame(frame_books, color3, 0, 0, 1000, 175)
frame_books_bottom  = F.create_frame(frame_books, color3, 0, 575, 1000, 25)
return_button3      = F.create_button_image(frame_books, icon_return, color3, frame_menu, 25, 25)

#==============================Lire un livre====================================
frame_read          = F.create_frame(app, color1, 0, 0, 1000, 600)
frame_read_top      = F.create_frame(frame_read, color3, 0, 0, 1000, 175)
frame_read_bottom   = F.create_frame(frame_read, color3, 0, 575, 1000, 25)
return_button4      = F.create_button_image(frame_read, icon_return, color3, frame_menu, 25, 25)

size  = tkinter.IntVar()
style = tkinter.StringVar()

check_400           = F.create_radiobutton(frame_read, "moins de 400 pages", color1, size, 1, 105, 225)
check_400_600       = F.create_radiobutton(frame_read, "400 à 600 pages", color1, size, 2, 315, 225)
check_600_800       = F.create_radiobutton(frame_read, "600 à 800 pages", color1, size, 3, 525, 225)
check_800           = F.create_radiobutton(frame_read, "plus de 800 pages", color1, size, 4, 735, 225)
fantasy             = F.create_checkbutton(frame_read, "fantasy", color1, 105, 315)
science_fiction     = F.create_checkbutton(frame_read, "Science-Fiction", color1, 105, 355)
romance             = F.create_checkbutton(frame_read, "Romance", color1, 105, 395)
aventure            = F.create_checkbutton(frame_read, "Aventure", color1, 105, 435)
amitie              = F.create_checkbutton(frame_read, "Amitié", color1, 315, 315)
famille             = F.create_checkbutton(frame_read, "Famille", color1, 315, 355)
royaute             = F.create_checkbutton(frame_read, "Royauté", color1, 315, 395)
pouvoir             = F.create_checkbutton(frame_read, "Pouvoir", color1, 315, 435)
magie               = F.create_checkbutton(frame_read, "Magie", color1, 525, 315)
sorciere            = F.create_checkbutton(frame_read, "Sorcière", color1, 525, 355)
vampire             = F.create_checkbutton(frame_read, "Vampire", color1, 525, 395)
loup_garou          = F.create_checkbutton(frame_read, "Loup Garou", color1, 525, 435)
ado                 = F.create_checkbutton(frame_read, "Ado", color1, 735, 315)
young_adult         = F.create_checkbutton(frame_read, "Young Adult", color1, 735, 355)
smut                = F.create_checkbutton(frame_read, "Smut", color1, 735, 395)
horreur             = F.create_checkbutton(frame_read, "Horreur", color1, 735, 435)

def clicked_button(size, style):
    title, writer, cover, styles = read_a_book(size, style)
    frame_chosen_book       = F.create_frame(app, color1, 0, 0, 1000, 600)
    frame_chosen_book_left  = F.create_frame(frame_chosen_book, color3, 0, 0, 250, 600)
    frame_chosen_book_right = F.create_frame(frame_chosen_book, color3, 975, 0, 25, 600)
    # frame_chosen_book_canva = F.create_frame(frame_chosen_book, color1, 100, 100, 300, 400)
    label_title             = F.create_label(frame_chosen_book, title, color1, 550, 300)
    label_writer            = F.create_label(frame_chosen_book, writer, color1, 550, 325)
    label_styles            = F.create_label(frame_chosen_book, styles, color1, 550, 350)
    return_button5          = F.create_button_image(frame_chosen_book, icon_return, color3, frame_menu, 25, 25)
    cover_image             = F.create_image_cover(cover)
    canva_chosen_book_cover = F.create_canvas(frame_chosen_book, cover_image, 'blue', 100, 100)


def create_button1(frame, texte, couleur, posX, posY, largeur, hauteur, relief="flat", ancre="nw"):
    button= tkinter.Button(frame, text=texte, bg=couleur, command=lambda:clicked_button(size.get(), style.get()), relief=relief)
    button.place(x=posX, y=posY, anchor=ancre, width=largeur, height=hauteur)
    return button


button_confirm = create_button1(frame_read, "Valider", color3, 750, 500, 200, 50)

#=============================Menu's button=====================================
button_read     = F.create_button(frame_central, "Lire un livre", color2, frame_read, 200, 80, 200, 50)
button_add      = F.create_button(frame_central, "Ajouter un livre", color2, frame_add, 200, 210, 200, 50)
button_delete   = F.create_button(frame_central, "Supprimer un livre", color2, frame_delete, 200, 340, 200, 50)
button_books    = F.create_button(frame_central, "Livres lus", color2, frame_books, 200, 470, 200, 50)


F.show_frame(frame_menu)

app.mainloop()
