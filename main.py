#his is a sample Python script
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
words=pd.read_csv('french_words.csv')
current_card=0
data= words.to_dict(orient='records')
dictator=[]
#dict ={row.French:row.English for (index,row) in words.iterrows()}#


def next_card():
    global current_card
    canv.itemconfig(pic, image=img)
    current_card = random.choice(data)
    canv.itemconfig(v_text, text='FRENCH')
    canv.itemconfig(t_text, text=current_card['French'])
    root.after(5000, english)


def add_card():
    global current_card
    canv.itemconfig(pic, image=img)
    current_card = random.choice(data)
    canv.itemconfig(v_text, text='FRENCH')
    canv.itemconfig(t_text, text= current_card['French'])
    root.after(3000, english)
    try:
        with open('learnt.txt',mode='a') as file:
            file.write(f'\nFRENCH:{current_card["French"]}, ENGLISH:{current_card["English"]}')

    except FileNotFoundError:
        with open('learnt.txt', mode='w') as file:
            file.write(f'FRENCH:{current_card["French"]}, ENGLISH:{current_card["English"]}')


def english():
    canv.itemconfig(pic,image=img4)
    canv.itemconfig(v_text, text='ENGLISH')
    canv.itemconfig(t_text, text=current_card['English'])

root = Tk()
root.title('FLASH CARD')
root.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
canv = Canvas(width=810,height=530)
img= PhotoImage(file='card_front.png')
img2= PhotoImage(file='right.png')
img4 = PhotoImage(file='card_back.png')
img3 = PhotoImage(file='wrong.png')
pic= canv.create_image(405,265,image=img)
canv.config(bg=BACKGROUND_COLOR,highlightthickness=0)
v_text= canv.create_text(405,210,text= 'LANGUAGE',font=('Arial', 20, 'italic'))
t_text= canv.create_text(405,265,text= 'WORDS',font=('Arial', 30, 'bold'))
b= Button(image=img2, command= next_card)
b2= Button(image= img3, command=add_card)
b2.grid(row=1, column=2)
b.grid(row=1,column=0)
canv.grid(row=0,column=0,columnspan=3)
mainloop()