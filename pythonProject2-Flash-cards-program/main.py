BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random





word_display= {}
korean_dict={}
def card_front():
    global word_display, flip_timer
    window.after_cancel(flip_timer)
    word_display= random.choice(korean_dict)
    canvas.itemconfig(card_title, text= "Korean", fill="black" )
    canvas.itemconfig(card_word, text=word_display["Korean"], fill= "black")
#     canvas.create_image(400, 263, image=card_img_f)
#     canvas.grid(column=0, row=0, columnspan=2)
    canvas.itemconfig(card_bg, image= card_img_f)
    flip_timer= window.after(3000, func= flip_card)
def flip_card():
    canvas.itemconfig(card_bg,image= card_img_b)
    canvas.itemconfig(card_title, text= "English", fill= "white")
    canvas.itemconfig(card_word, text= word_display["English"], fill="white")

def is_known():
    korean_dict.remove(word_display)
    data=pandas.DataFrame(korean_dict)
    data.to_csv("need_to_revise", index=False)
    card_front()

window= Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer= window.after(3000, func=flip_card)

try:
    data= pandas.read_csv("need_to_revise")

except FileNotFoundError:
    data= pandas.read_csv("Korean.csv")
    korean_dict=data.to_dict(orient="records")
else:
    korean_dict= data.to_dict(orient="records")


canvas= Canvas(width=800, height= 526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img_f = PhotoImage(file="card_front.png")
card_bg= canvas.create_image(400, 263, image=card_img_f)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word= canvas.create_text(400, 263, text= "", font=("Ariel", 45, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
card_img_b= PhotoImage(file= "card_back.png")

cross_img= PhotoImage(file= "wrong.png")
cross_button= Button(image=cross_img, highlightthickness=0, command= card_front)
cross_button.grid(column=0, row=1)
right_img= PhotoImage(file= "right.png")
right_button= Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

card_front()

window.mainloop()