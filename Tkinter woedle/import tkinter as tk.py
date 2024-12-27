import tkinter as tk
from tkinter import *
import random
from random import choice
import importlib
import sys
import time
from importlib import util


def validate_input(char):
    return len(char) <= 1
window = tk.Tk()
window.geometry("400x400")
window.title("Wordle")

vcmd = (window.register(validate_input), '%P')

def get_list_of_words(path):
    with open('fiveLetterWords.txt', 'r', encoding='utf-8') as f:
        return f.read().splitlines()
words = get_list_of_words('/usr/share/dict/words')
random_word = random.choice(words)
random_word_letters = list(random_word)
randomtest = Label(window, text=random_word)


Letter1 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter2 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter3= Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter4 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter5 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter6 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter7 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter8= Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter9 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter10 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter11 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter12 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter13= Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter14 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter15 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter16 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter17 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter18= Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter19 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter20 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter21 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter22 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter23 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter24= Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)
Letter25 = Entry(window, width=1, font=("Times New Roman", 24), validate='key', validatecommand=vcmd)


list_for_first_word_guess = []
list_for_second_word_guess = []
list_for_third_word_guess = []
list_for_fourth_word_guess = []
list_for_fifth_word_guess = []


Letters = [Letter1, Letter2, Letter3, Letter4, Letter5, Letter6, 
           Letter7, Letter8, Letter9, Letter10, Letter11, Letter12, 
           Letter13, Letter14, Letter15, Letter16, Letter17, Letter18, 
           Letter19, Letter20, Letter21, Letter22, Letter23, Letter24, Letter25]
Letters_1column = [Letter1, Letter2, Letter3, Letter4, Letter5]
Letters_2column = [Letter6, Letter7, Letter8, Letter9, Letter10]
Letters_3column = [Letter11, Letter12, Letter13, Letter14, Letter15]
Letters_4column = [Letter16, Letter17, Letter18, Letter19, Letter20]
Letters_5column = [Letter21, Letter22, Letter23, Letter24, Letter25]
Letter1.config(state="normal")
Letter2.config(state="normal")
Letter3.config(state="normal")
Letter4.config(state="normal")
Letter5.config(state="normal")
Letter6.config(state="disabled")
Letter7.config(state="disabled")
Letter8.config(state="disabled")
Letter9.config(state="disabled")
Letter10.config(state="disabled")
Letter11.config(state="disabled")
Letter12.config(state="disabled")
Letter13.config(state="disabled")
Letter14.config(state="disabled")
Letter15.config(state="disabled")
Letter16.config(state="disabled")
Letter17.config(state="disabled")
Letter18.config(state="disabled")
Letter19.config(state="disabled")
Letter20.config(state="disabled")
Letter21.config(state="disabled")
Letter22.config(state="disabled")
Letter23.config(state="disabled")
Letter24.config(state="disabled")
Letter25.config(state="disabled")



VariableForListOfLetters = -1

def print_q(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "q")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<q>", print_q)

def print_w(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "w")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<w>", print_w)

def print_e(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "e")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<e>", print_e)

def print_r(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "r")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<r>", print_r)

def print_t(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "t")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<t>", print_t)

def print_y(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "y")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<y>", print_y)

def print_u(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "u")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<u>", print_u)

def print_i(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "i")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<i>", print_i)

def print_o(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "o")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<o>", print_o)

def print_p(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "p")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<p>", print_p)

def print_a(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "a")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<a>", print_a)

def print_s(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "s")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<s>", print_s)

def print_d(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "d")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<d>", print_d)

def print_f(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "f")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<f>", print_f)

def print_g(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "g")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<g>", print_g)

def print_h(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "h")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<h>", print_h)

def print_j(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "j")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<j>", print_j)

def print_k(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "k")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<k>", print_k)

def print_l(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "l")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<l>", print_l)

def print_z(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "z")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<z>", print_z)

def print_x(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "x")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<x>", print_x)

def print_c(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "c")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<c>", print_c)

def print_v(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "v")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<v>", print_v)

def print_b(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "b")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<b>", print_b)

def print_n(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "n")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<n>", print_n)

def print_m(event):
    global VariableForListOfLetters
    VariableForListOfLetters = VariableForListOfLetters + 1
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].insert(0, "m")
    else:
        VariableForListOfLetters = VariableForListOfLetters - 1
window.bind("<m>", print_m)

def bksp(event):
    global VariableForListOfLetters
    if Letters[VariableForListOfLetters].cget("state") == "normal":
      Letters[VariableForListOfLetters].delete(0, END)
      VariableForListOfLetters = VariableForListOfLetters - 1
    else:
      VariableForListOfLetters = VariableForListOfLetters + 1
window.bind("<BackSpace>", bksp)

Alphabetq = Button(window, text="q")
Alphabetw = Button(window, text="w")
Alphabete = Button(window, text="e")
Alphabetr = Button(window, text="r")
Alphabett = Button(window, text="t")
Alphabety = Button(window, text="y")
Alphabetu = Button(window, text="u")
Alphabeti = Button(window, text="i")
Alphabeto = Button(window, text="o")
Alphabetp = Button(window, text="p")
Alphabeta = Button(window, text="a")
Alphabets = Button(window, text="s")
Alphabetd = Button(window, text="d")
Alphabetf = Button(window, text="f")
Alphabetg = Button(window, text="g")
Alphabeth = Button(window, text="h")
Alphabetj = Button(window, text="j")
Alphabetk = Button(window, text="k")
Alphabetl = Button(window, text="l")
Alphabetz = Button(window, text="z")
Alphabetx = Button(window, text="x")
Alphabetc = Button(window, text="c")
Alphabetv = Button(window, text="v")
Alphabetb = Button(window, text="b")
Alphabetn = Button(window, text="n")
Alphabetm = Button(window, text="m")



TextWordle = Label(window, font=("TimesNewRoman", 40), text="Wordle")

FinalUserAnswer = Label(window, font=("TimesNewRoman", 20))

def enterbutton(event):
   if Letters[0].cget("state") == "normal":
      global list_for_first_word_guess
      global Letters_1column
      list_for_first_word_guess = [Letter1.get(), Letter2.get(), Letter3.get(), Letter4.get(), Letter5.get()]


      if list_for_first_word_guess[0] == random_word_letters[0]:
          Letters_1column[0].config(disabledbackground="Yellow")
          if list_for_first_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[0] == random_word_letters[1]:
          Letters_1column[0].config(disabledbackground="Yellow")
          if list_for_first_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[0] == random_word_letters[2]:
          Letters_1column[0].config(disabledbackground="Yellow")
          if list_for_first_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[0] == random_word_letters[3]:
          Letters_1column[0].config(disabledbackground="Yellow")
          if list_for_first_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[0] == random_word_letters[4]:
          Letters_1column[0].config(disabledbackground="Yellow")
          if list_for_first_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      if list_for_first_word_guess[1] == random_word_letters[0]:
          Letters_1column[1].config(disabledbackground="Yellow")
          if list_for_first_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[1] == random_word_letters[1]:
          Letters_1column[1].config(disabledbackground="Yellow")
          if list_for_first_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[1] == random_word_letters[2]:
          Letters_1column[1].config(disabledbackground="Yellow")
          if list_for_first_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[1] == random_word_letters[3]:
          Letters_1column[1].config(disabledbackground="Yellow")
          if list_for_first_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[1] == random_word_letters[4]:
          Letters_1column[1].config(disabledbackground="Yellow")
          if list_for_first_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_first_word_guess[2] == random_word_letters[0]:
          Letters_1column[2].config(disabledbackground="Yellow")
          if list_for_first_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[2] == random_word_letters[1]:
          Letters_1column[2].config(disabledbackground="Yellow")
          if list_for_first_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[2] == random_word_letters[2]:
          Letters_1column[2].config(disabledbackground="Yellow")
          if list_for_first_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[2] == random_word_letters[3]:
          Letters_1column[2].config(disabledbackground="Yellow")
          if list_for_first_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[2] == random_word_letters[4]:
          Letters_1column[2].config(disabledbackground="Yellow")
          if list_for_first_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_first_word_guess[3] == random_word_letters[0]:
          Letters_1column[3].config(disabledbackground="Yellow")
          if list_for_first_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[3] == random_word_letters[1]:
          Letters_1column[3].config(disabledbackground="Yellow")
          if list_for_first_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[3] == random_word_letters[2]:
          Letters_1column[3].config(disabledbackground="Yellow")
          if list_for_first_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[3] == random_word_letters[3]:
          Letters_1column[3].config(disabledbackground="Yellow")
          if list_for_first_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[3] == random_word_letters[4]:
          Letters_1column[3].config(disabledbackground="Yellow")
          if list_for_first_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_first_word_guess[4] == random_word_letters[0]:
          Letters_1column[4].config(disabledbackground="Yellow")
          if list_for_first_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[4] == random_word_letters[1]:
          Letters_1column[4].config(disabledbackground="Yellow")
          if list_for_first_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[4] == random_word_letters[2]:
          Letters_1column[4].config(disabledbackground="Yellow")
          if list_for_first_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[4] == random_word_letters[3]:
          Letters_1column[4].config(disabledbackground="Yellow")
          if list_for_first_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_first_word_guess[4] == random_word_letters[4]:
          Letters_1column[4].config(disabledbackground="Yellow")
          if list_for_first_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_first_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")

      if list_for_first_word_guess[0] == random_word_letters[0]:
          Letters_1column[0].config(disabledbackground="Green")
          if list_for_first_word_guess[0] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_first_word_guess[0] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_first_word_guess[0] == "e":
            Alphabete.config(bg="Green")
          elif list_for_first_word_guess[0] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_first_word_guess[0] == "t":
            Alphabett.config(bg="Green")
          elif list_for_first_word_guess[0] == "y":
            Alphabety.config(bg="Green")
          elif list_for_first_word_guess[0] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_first_word_guess[0] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_first_word_guess[0] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_first_word_guess[0] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_first_word_guess[0] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_first_word_guess[0] == "s":
            Alphabets.config(bg="Green")
          elif list_for_first_word_guess[0] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_first_word_guess[0] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_first_word_guess[0] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_first_word_guess[0] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_first_word_guess[0] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_first_word_guess[0] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_first_word_guess[0] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_first_word_guess[0] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_first_word_guess[0] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_first_word_guess[0] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_first_word_guess[0] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_first_word_guess[0] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_first_word_guess[0] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_first_word_guess[0] == "m":
            Alphabetm.config(bg="Green")
      if list_for_first_word_guess[1] == random_word_letters[1]:
          Letters_1column[1].config(disabledbackground="Green")
          if list_for_first_word_guess[1] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_first_word_guess[1] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_first_word_guess[1] == "e":
            Alphabete.config(bg="Green")
          elif list_for_first_word_guess[1] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_first_word_guess[1] == "t":
            Alphabett.config(bg="Green")
          elif list_for_first_word_guess[1] == "y":
            Alphabety.config(bg="Green")
          elif list_for_first_word_guess[1] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_first_word_guess[1] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_first_word_guess[1] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_first_word_guess[1] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_first_word_guess[1] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_first_word_guess[1] == "s":
            Alphabets.config(bg="Green")
          elif list_for_first_word_guess[1] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_first_word_guess[1] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_first_word_guess[1] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_first_word_guess[1] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_first_word_guess[1] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_first_word_guess[1] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_first_word_guess[1] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_first_word_guess[1] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_first_word_guess[1] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_first_word_guess[1] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_first_word_guess[1] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_first_word_guess[1] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_first_word_guess[1] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_first_word_guess[1] == "m":
            Alphabetm.config(bg="Green")
      if list_for_first_word_guess[2] == random_word_letters[2]:
          Letters_1column[2].config(disabledbackground="Green")
          if list_for_first_word_guess[2] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_first_word_guess[2] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_first_word_guess[2] == "e":
            Alphabete.config(bg="Green")
          elif list_for_first_word_guess[2] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_first_word_guess[2] == "t":
            Alphabett.config(bg="Green")
          elif list_for_first_word_guess[2] == "y":
            Alphabety.config(bg="Green")
          elif list_for_first_word_guess[2] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_first_word_guess[2] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_first_word_guess[2] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_first_word_guess[2] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_first_word_guess[2] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_first_word_guess[2] == "s":
            Alphabets.config(bg="Green")
          elif list_for_first_word_guess[2] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_first_word_guess[2] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_first_word_guess[2] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_first_word_guess[2] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_first_word_guess[2] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_first_word_guess[2] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_first_word_guess[2] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_first_word_guess[2] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_first_word_guess[2] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_first_word_guess[2] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_first_word_guess[2] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_first_word_guess[2] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_first_word_guess[2] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_first_word_guess[2] == "m":
            Alphabetm.config(bg="Green")
      if list_for_first_word_guess[3] == random_word_letters[3]:
          Letters_1column[3].config(disabledbackground="Green")
          if list_for_first_word_guess[3] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_first_word_guess[3] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_first_word_guess[3] == "e":
            Alphabete.config(bg="Green")
          elif list_for_first_word_guess[3] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_first_word_guess[3] == "t":
            Alphabett.config(bg="Green")
          elif list_for_first_word_guess[3] == "y":
            Alphabety.config(bg="Green")
          elif list_for_first_word_guess[3] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_first_word_guess[3] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_first_word_guess[3] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_first_word_guess[3] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_first_word_guess[3] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_first_word_guess[3] == "s":
            Alphabets.config(bg="Green")
          elif list_for_first_word_guess[3] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_first_word_guess[3] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_first_word_guess[3] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_first_word_guess[3] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_first_word_guess[3] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_first_word_guess[3] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_first_word_guess[3] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_first_word_guess[3] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_first_word_guess[3] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_first_word_guess[3] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_first_word_guess[3] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_first_word_guess[3] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_first_word_guess[3] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_first_word_guess[3] == "m":
            Alphabetm.config(bg="Green")
      if list_for_first_word_guess[4] == random_word_letters[4]:
          Letters_1column[4].config(disabledbackground="Green")
          if list_for_first_word_guess[4] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_first_word_guess[4] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_first_word_guess[4] == "e":
            Alphabete.config(bg="Green")
          elif list_for_first_word_guess[4] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_first_word_guess[4] == "t":
            Alphabett.config(bg="Green")
          elif list_for_first_word_guess[4] == "y":
            Alphabety.config(bg="Green")
          elif list_for_first_word_guess[4] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_first_word_guess[4] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_first_word_guess[4] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_first_word_guess[4] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_first_word_guess[4] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_first_word_guess[4] == "s":
            Alphabets.config(bg="Green")
          elif list_for_first_word_guess[4] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_first_word_guess[4] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_first_word_guess[4] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_first_word_guess[4] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_first_word_guess[4] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_first_word_guess[4] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_first_word_guess[4] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_first_word_guess[4] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_first_word_guess[4] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_first_word_guess[4] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_first_word_guess[4] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_first_word_guess[4] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_first_word_guess[4] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_first_word_guess[4] == "m":
            Alphabetm.config(bg="Green")
      if list_for_first_word_guess == random_word_letters:
        new_window = Toplevel(window)
        new_window.title("Wordle")
        new_window.geometry("150x150")
        text_win = "You won! Word was: "
        Label_new_window = Label(new_window, text=f"{text_win}{random_word}")
        Label_new_window.pack()
        new_window.mainloop()

        Letter1.config(state="disabled")
        Letter2.config(state="disabled")
        Letter3.config(state="disabled")
        Letter4.config(state="disabled")
        Letter5.config(state="disabled")
        Letter6.config(state="disabled")
        Letter7.config(state="disabled")
        Letter8.config(state="disabled")
        Letter9.config(state="disabled")
        Letter10.config(state="disabled")
        Letter11.config(state="disabled")
        Letter12.config(state="disabled")
        Letter13.config(state="disabled")
        Letter14.config(state="disabled")
        Letter15.config(state="disabled")
        Letter16.config(state="disabled")
        Letter17.config(state="disabled")
        Letter18.config(state="disabled")
        Letter19.config(state="disabled")
        Letter20.config(state="disabled")
        Letter21.config(state="disabled")
        Letter22.config(state="disabled")
        Letter23.config(state="disabled")
        Letter24.config(state="disabled")
        Letter25.config(state="disabled")

      Letter1.config(state="disabled")
      Letter2.config(state="disabled")
      Letter3.config(state="disabled")
      Letter4.config(state="disabled")
      Letter5.config(state="disabled")
      Letter6.config(state="normal")
      Letter7.config(state="normal")
      Letter8.config(state="normal")
      Letter9.config(state="normal")
      Letter10.config(state="normal")
      Letter11.config(state="disabled")
      Letter12.config(state="disabled")
      Letter13.config(state="disabled")
      Letter14.config(state="disabled")
      Letter15.config(state="disabled")
      Letter16.config(state="disabled")
      Letter17.config(state="disabled")
      Letter18.config(state="disabled")
      Letter19.config(state="disabled")
      Letter20.config(state="disabled")
      Letter21.config(state="disabled")
      Letter22.config(state="disabled")
      Letter23.config(state="disabled")
      Letter24.config(state="disabled")
      Letter25.config(state="disabled")


   elif Letters[5].cget("state") == "normal":
      global list_for_second_word_guess
      global Letters_2column
      list_for_second_word_guess = [Letter6.get(), Letter7.get(), Letter8.get(), Letter9.get(), Letter10.get()]
      if list_for_second_word_guess[0] == random_word_letters[0]:
          Letters_2column[0].config(disabledbackground="Yellow")
          if list_for_second_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[0] == random_word_letters[1]:
          Letters_2column[0].config(disabledbackground="Yellow")
          if list_for_second_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[0] == random_word_letters[2]:
          Letters_2column[0].config(disabledbackground="Yellow")
          if list_for_second_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[0] == random_word_letters[3]:
          Letters_2column[0].config(disabledbackground="Yellow")
          if list_for_second_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[0] == random_word_letters[4]:
          Letters_2column[0].config(disabledbackground="Yellow")
          if list_for_second_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_second_word_guess[1] == random_word_letters[0]:
          Letters_2column[1].config(disabledbackground="Yellow")
          if list_for_second_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[1] == random_word_letters[1]:
          Letters_2column[1].config(disabledbackground="Yellow")
          if list_for_second_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[1] == random_word_letters[2]:
          Letters_2column[1].config(disabledbackground="Yellow")
          if list_for_second_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[1] == random_word_letters[3]:
          Letters_2column[1].config(disabledbackground="Yellow")
          if list_for_second_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[1] == random_word_letters[4]:
          Letters_2column[1].config(disabledbackground="Yellow")
          if list_for_second_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_second_word_guess[2] == random_word_letters[0]:
          Letters_2column[2].config(disabledbackground="Yellow")
          if list_for_second_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[2] == random_word_letters[1]:
          Letters_2column[2].config(disabledbackground="Yellow")
          if list_for_second_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[2] == random_word_letters[2]:
          Letters_2column[2].config(disabledbackground="Yellow")
          if list_for_second_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[2] == random_word_letters[3]:
          Letters_2column[2].config(disabledbackground="Yellow")
          if list_for_second_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[2] == random_word_letters[4]:
          Letters_2column[2].config(disabledbackground="Yellow")
          if list_for_second_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_second_word_guess[3] == random_word_letters[0]:
          Letters_2column[3].config(disabledbackground="Yellow")
          if list_for_second_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[3] == random_word_letters[1]:
          Letters_2column[3].config(disabledbackground="Yellow")
          if list_for_second_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[3] == random_word_letters[2]:
          Letters_2column[3].config(disabledbackground="Yellow")
          if list_for_second_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[3] == random_word_letters[3]:
          Letters_2column[3].config(disabledbackground="Yellow")
          if list_for_second_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[3] == random_word_letters[4]:
          Letters_2column[3].config(disabledbackground="Yellow")
          if list_for_second_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_second_word_guess[4] == random_word_letters[0]:
          Letters_2column[4].config(disabledbackground="Yellow")
          if list_for_second_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[4] == random_word_letters[1]:
          Letters_2column[4].config(disabledbackground="Yellow")
          if list_for_second_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[4] == random_word_letters[2]:
          Letters_2column[4].config(disabledbackground="Yellow")
          if list_for_second_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[4] == random_word_letters[3]:
          Letters_2column[4].config(disabledbackground="Yellow")
          if list_for_second_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_second_word_guess[4] == random_word_letters[4]:
          Letters_2column[4].config(disabledbackground="Yellow")
          if list_for_second_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_second_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_second_word_guess[0] == random_word_letters[0]:
          Letters_2column[0].config(disabledbackground="Green")
          if list_for_second_word_guess[0] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_second_word_guess[0] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_second_word_guess[0] == "e":
            Alphabete.config(bg="Green")
          elif list_for_second_word_guess[0] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_second_word_guess[0] == "t":
            Alphabett.config(bg="Green")
          elif list_for_second_word_guess[0] == "y":
            Alphabety.config(bg="Green")
          elif list_for_second_word_guess[0] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_second_word_guess[0] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_second_word_guess[0] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_second_word_guess[0] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_second_word_guess[0] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_second_word_guess[0] == "s":
            Alphabets.config(bg="Green")
          elif list_for_second_word_guess[0] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_second_word_guess[0] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_second_word_guess[0] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_second_word_guess[0] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_second_word_guess[0] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_second_word_guess[0] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_second_word_guess[0] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_second_word_guess[0] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_second_word_guess[0] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_second_word_guess[0] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_second_word_guess[0] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_second_word_guess[0] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_second_word_guess[0] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_second_word_guess[0] == "m":
            Alphabetm.config(bg="Green")
      if list_for_second_word_guess[1] == random_word_letters[1]:
          Letters_2column[1].config(disabledbackground="Green")
          if list_for_second_word_guess[1] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_second_word_guess[1] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_second_word_guess[1] == "e":
            Alphabete.config(bg="Green")
          elif list_for_second_word_guess[1] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_second_word_guess[1] == "t":
            Alphabett.config(bg="Green")
          elif list_for_second_word_guess[1] == "y":
            Alphabety.config(bg="Green")
          elif list_for_second_word_guess[1] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_second_word_guess[1] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_second_word_guess[1] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_second_word_guess[1] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_second_word_guess[1] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_second_word_guess[1] == "s":
            Alphabets.config(bg="Green")
          elif list_for_second_word_guess[1] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_second_word_guess[1] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_second_word_guess[1] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_second_word_guess[1] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_second_word_guess[1] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_second_word_guess[1] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_second_word_guess[1] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_second_word_guess[1] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_second_word_guess[1] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_second_word_guess[1] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_second_word_guess[1] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_second_word_guess[1] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_second_word_guess[1] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_second_word_guess[1] == "m":
            Alphabetm.config(bg="Green")
      if list_for_second_word_guess[2] == random_word_letters[2]:
          Letters_2column[2].config(disabledbackground="Green")
          if list_for_second_word_guess[2] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_second_word_guess[2] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_second_word_guess[2] == "e":
            Alphabete.config(bg="Green")
          elif list_for_second_word_guess[2] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_second_word_guess[2] == "t":
            Alphabett.config(bg="Green")
          elif list_for_second_word_guess[2] == "y":
            Alphabety.config(bg="Green")
          elif list_for_second_word_guess[2] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_second_word_guess[2] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_second_word_guess[2] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_second_word_guess[2] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_second_word_guess[2] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_second_word_guess[2] == "s":
            Alphabets.config(bg="Green")
          elif list_for_second_word_guess[2] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_second_word_guess[2] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_second_word_guess[2] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_second_word_guess[2] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_second_word_guess[2] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_second_word_guess[2] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_second_word_guess[2] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_second_word_guess[2] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_second_word_guess[2] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_second_word_guess[2] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_second_word_guess[2] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_second_word_guess[2] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_second_word_guess[2] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_second_word_guess[2] == "m":
            Alphabetm.config(bg="Green")
      if list_for_second_word_guess[3] == random_word_letters[3]:
          Letters_2column[3].config(disabledbackground="Green")
          if list_for_second_word_guess[3] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_second_word_guess[3] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_second_word_guess[3] == "e":
            Alphabete.config(bg="Green")
          elif list_for_second_word_guess[3] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_second_word_guess[3] == "t":
            Alphabett.config(bg="Green")
          elif list_for_second_word_guess[3] == "y":
            Alphabety.config(bg="Green")
          elif list_for_second_word_guess[3] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_second_word_guess[3] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_second_word_guess[3] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_second_word_guess[3] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_second_word_guess[3] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_second_word_guess[3] == "s":
            Alphabets.config(bg="Green")
          elif list_for_second_word_guess[3] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_second_word_guess[3] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_second_word_guess[3] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_second_word_guess[3] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_second_word_guess[3] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_second_word_guess[3] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_second_word_guess[3] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_second_word_guess[3] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_second_word_guess[3] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_second_word_guess[3] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_second_word_guess[3] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_second_word_guess[3] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_second_word_guess[3] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_second_word_guess[3] == "m":
            Alphabetm.config(bg="Green")
      if list_for_second_word_guess[4] == random_word_letters[4]:
          Letters_2column[4].config(disabledbackground="Green")
          if list_for_second_word_guess[4] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_second_word_guess[4] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_second_word_guess[4] == "e":
            Alphabete.config(bg="Green")
          elif list_for_second_word_guess[4] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_second_word_guess[4] == "t":
            Alphabett.config(bg="Green")
          elif list_for_second_word_guess[4] == "y":
            Alphabety.config(bg="Green")
          elif list_for_second_word_guess[4] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_second_word_guess[4] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_second_word_guess[4] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_second_word_guess[4] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_second_word_guess[4] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_second_word_guess[4] == "s":
            Alphabets.config(bg="Green")
          elif list_for_second_word_guess[4] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_second_word_guess[4] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_second_word_guess[4] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_second_word_guess[4] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_second_word_guess[4] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_second_word_guess[4] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_second_word_guess[4] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_second_word_guess[4] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_second_word_guess[4] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_second_word_guess[4] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_second_word_guess[4] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_second_word_guess[4] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_second_word_guess[4] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_second_word_guess[4] == "m":
            Alphabetm.config(bg="Green")
      if list_for_second_word_guess == random_word_letters:
        new_window = Toplevel(window)
        new_window.title("Wordle")
        new_window.geometry("150x150")
        text_win = "You won! Word was: "
        Label_new_window = Label(new_window, text=f"{text_win}{random_word}")
        Label_new_window.pack()
        new_window.mainloop()
        Letter1.config(state="disabled")
        Letter2.config(state="disabled")
        Letter3.config(state="disabled")
        Letter4.config(state="disabled")
        Letter5.config(state="disabled")
        Letter6.config(state="disabled")
        Letter7.config(state="disabled")
        Letter8.config(state="disabled")
        Letter9.config(state="disabled")
        Letter10.config(state="disabled")
        Letter11.config(state="disabled")
        Letter12.config(state="disabled")
        Letter13.config(state="disabled")
        Letter14.config(state="disabled")
        Letter15.config(state="disabled")
        Letter16.config(state="disabled")
        Letter17.config(state="disabled")
        Letter18.config(state="disabled")
        Letter19.config(state="disabled")
        Letter20.config(state="disabled")
        Letter21.config(state="disabled")
        Letter22.config(state="disabled")
        Letter23.config(state="disabled")
        Letter24.config(state="disabled")
        Letter25.config(state="disabled")

      Letter1.config(state="disabled")
      Letter2.config(state="disabled")
      Letter3.config(state="disabled")
      Letter4.config(state="disabled")
      Letter5.config(state="disabled")
      Letter6.config(state="disabled")
      Letter7.config(state="disabled")
      Letter8.config(state="disabled")
      Letter9.config(state="disabled")
      Letter10.config(state="disabled")
      Letter11.config(state="normal")
      Letter12.config(state="normal")
      Letter13.config(state="normal")
      Letter14.config(state="normal")
      Letter15.config(state="normal")
      Letter16.config(state="disabled")
      Letter17.config(state="disabled")
      Letter18.config(state="disabled")
      Letter19.config(state="disabled")
      Letter20.config(state="disabled")
      Letter21.config(state="disabled")
      Letter22.config(state="disabled")
      Letter23.config(state="disabled")
      Letter24.config(state="disabled")
      Letter25.config(state="disabled")


   elif Letters[11].cget("state") == "normal":
      global list_for_third_word_guess
      global Letters_3column
      list_for_third_word_guess = [Letter11.get(), Letter12.get(), Letter13.get(), Letter14.get(), Letter15.get()]


      if list_for_third_word_guess[0] == random_word_letters[0]:
          Letters_3column[0].config(disabledbackground="Yellow")
          if list_for_third_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[0] == random_word_letters[1]:
          Letters_3column[0].config(disabledbackground="Yellow")
          if list_for_third_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[0] == random_word_letters[2]:
          Letters_3column[0].config(disabledbackground="Yellow")
          if list_for_third_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[0] == random_word_letters[3]:
          Letters_3column[0].config(disabledbackground="Yellow")
          if list_for_third_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[0] == random_word_letters[4]:
          Letters_3column[0].config(disabledbackground="Yellow")
          if list_for_third_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_third_word_guess[1] == random_word_letters[0]:
          Letters_3column[1].config(disabledbackground="Yellow")
          if list_for_third_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[1] == random_word_letters[1]:
          Letters_3column[1].config(disabledbackground="Yellow")
          if list_for_third_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[1] == random_word_letters[2]:
          Letters_3column[1].config(disabledbackground="Yellow")
          if list_for_third_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[1] == random_word_letters[3]:
          Letters_3column[1].config(disabledbackground="Yellow")
          if list_for_third_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[1] == random_word_letters[4]:
          Letters_3column[1].config(disabledbackground="Yellow")
          if list_for_third_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_third_word_guess[2] == random_word_letters[0]:
          Letters_3column[2].config(disabledbackground="Yellow")
          if list_for_third_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[2] == random_word_letters[1]:
          Letters_3column[2].config(disabledbackground="Yellow")
          if list_for_third_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[2] == random_word_letters[2]:
          Letters_3column[2].config(disabledbackground="Yellow")
          if list_for_third_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[2] == random_word_letters[3]:
          Letters_3column[2].config(disabledbackground="Yellow")
          if list_for_third_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[2] == random_word_letters[4]:
          Letters_3column[2].config(disabledbackground="Yellow")
          if list_for_third_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_third_word_guess[3] == random_word_letters[0]:
          Letters_3column[3].config(disabledbackground="Yellow")
          if list_for_third_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[3] == random_word_letters[1]:
          Letters_3column[3].config(disabledbackground="Yellow")
          if list_for_third_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[3] == random_word_letters[2]:
          Letters_3column[3].config(disabledbackground="Yellow")
          if list_for_third_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[3] == random_word_letters[3]:
          Letters_3column[3].config(disabledbackground="Yellow")
          if list_for_third_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[3] == random_word_letters[4]:
          Letters_3column[3].config(disabledbackground="Yellow")
          if list_for_third_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_third_word_guess[4] == random_word_letters[0]:
          Letters_3column[4].config(disabledbackground="Yellow")
          if list_for_third_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[4] == random_word_letters[1]:
          Letters_3column[4].config(disabledbackground="Yellow")
          if list_for_third_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[4] == random_word_letters[2]:
          Letters_3column[4].config(disabledbackground="Yellow")
          if list_for_third_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[4] == random_word_letters[3]:
          Letters_3column[4].config(disabledbackground="Yellow")
          if list_for_third_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_third_word_guess[4] == random_word_letters[4]:
          Letters_3column[4].config(disabledbackground="Yellow")
          if list_for_third_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_third_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_third_word_guess[0] == random_word_letters[0]:
          Letters_3column[0].config(disabledbackground="Green")
          if list_for_third_word_guess[0] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_third_word_guess[0] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_third_word_guess[0] == "e":
            Alphabete.config(bg="Green")
          elif list_for_third_word_guess[0] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_third_word_guess[0] == "t":
            Alphabett.config(bg="Green")
          elif list_for_third_word_guess[0] == "y":
            Alphabety.config(bg="Green")
          elif list_for_third_word_guess[0] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_third_word_guess[0] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_third_word_guess[0] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_third_word_guess[0] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_third_word_guess[0] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_third_word_guess[0] == "s":
            Alphabets.config(bg="Green")
          elif list_for_third_word_guess[0] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_third_word_guess[0] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_third_word_guess[0] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_third_word_guess[0] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_third_word_guess[0] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_third_word_guess[0] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_third_word_guess[0] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_third_word_guess[0] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_third_word_guess[0] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_third_word_guess[0] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_third_word_guess[0] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_third_word_guess[0] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_third_word_guess[0] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_third_word_guess[0] == "m":
            Alphabetm.config(bg="Green")
      if list_for_third_word_guess[1] == random_word_letters[1]:
          Letters_3column[1].config(disabledbackground="Green")
          if list_for_third_word_guess[1] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_third_word_guess[1] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_third_word_guess[1] == "e":
            Alphabete.config(bg="Green")
          elif list_for_third_word_guess[1] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_third_word_guess[1] == "t":
            Alphabett.config(bg="Green")
          elif list_for_third_word_guess[1] == "y":
            Alphabety.config(bg="Green")
          elif list_for_third_word_guess[1] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_third_word_guess[1] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_third_word_guess[1] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_third_word_guess[1] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_third_word_guess[1] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_third_word_guess[1] == "s":
            Alphabets.config(bg="Green")
          elif list_for_third_word_guess[1] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_third_word_guess[1] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_third_word_guess[1] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_third_word_guess[1] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_third_word_guess[1] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_third_word_guess[1] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_third_word_guess[1] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_third_word_guess[1] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_third_word_guess[1] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_third_word_guess[1] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_third_word_guess[1] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_third_word_guess[1] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_third_word_guess[1] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_third_word_guess[1] == "m":
            Alphabetm.config(bg="Green")
      if list_for_third_word_guess[2] == random_word_letters[2]:
          Letters_3column[2].config(disabledbackground="Green")
          if list_for_third_word_guess[2] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_third_word_guess[2] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_third_word_guess[2] == "e":
            Alphabete.config(bg="Green")
          elif list_for_third_word_guess[2] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_third_word_guess[2] == "t":
            Alphabett.config(bg="Green")
          elif list_for_third_word_guess[2] == "y":
            Alphabety.config(bg="Green")
          elif list_for_third_word_guess[2] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_third_word_guess[2] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_third_word_guess[2] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_third_word_guess[2] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_third_word_guess[2] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_third_word_guess[2] == "s":
            Alphabets.config(bg="Green")
          elif list_for_third_word_guess[2] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_third_word_guess[2] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_third_word_guess[2] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_third_word_guess[2] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_third_word_guess[2] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_third_word_guess[2] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_third_word_guess[2] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_third_word_guess[2] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_third_word_guess[2] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_third_word_guess[2] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_third_word_guess[2] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_third_word_guess[2] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_third_word_guess[2] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_third_word_guess[2] == "m":
            Alphabetm.config(bg="Green")
      if list_for_third_word_guess[3] == random_word_letters[3]:
          Letters_3column[3].config(disabledbackground="Green")
          if list_for_third_word_guess[3] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_third_word_guess[3] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_third_word_guess[3] == "e":
            Alphabete.config(bg="Green")
          elif list_for_third_word_guess[3] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_third_word_guess[3] == "t":
            Alphabett.config(bg="Green")
          elif list_for_third_word_guess[3] == "y":
            Alphabety.config(bg="Green")
          elif list_for_third_word_guess[3] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_third_word_guess[3] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_third_word_guess[3] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_third_word_guess[3] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_third_word_guess[3] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_third_word_guess[3] == "s":
            Alphabets.config(bg="Green")
          elif list_for_third_word_guess[3] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_third_word_guess[3] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_third_word_guess[3] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_third_word_guess[3] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_third_word_guess[3] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_third_word_guess[3] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_third_word_guess[3] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_third_word_guess[3] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_third_word_guess[3] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_third_word_guess[3] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_third_word_guess[3] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_third_word_guess[3] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_third_word_guess[3] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_third_word_guess[3] == "m":
            Alphabetm.config(bg="Green")
      if list_for_third_word_guess[4] == random_word_letters[4]:
          Letters_3column[4].config(disabledbackground="Green")
          if list_for_third_word_guess[4] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_third_word_guess[4] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_third_word_guess[4] == "e":
            Alphabete.config(bg="Green")
          elif list_for_third_word_guess[4] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_third_word_guess[4] == "t":
            Alphabett.config(bg="Green")
          elif list_for_third_word_guess[4] == "y":
            Alphabety.config(bg="Green")
          elif list_for_third_word_guess[4] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_third_word_guess[4] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_third_word_guess[4] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_third_word_guess[4] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_third_word_guess[4] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_third_word_guess[4] == "s":
            Alphabets.config(bg="Green")
          elif list_for_third_word_guess[4] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_third_word_guess[4] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_third_word_guess[4] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_third_word_guess[4] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_third_word_guess[4] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_third_word_guess[4] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_third_word_guess[4] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_third_word_guess[4] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_third_word_guess[4] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_third_word_guess[4] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_third_word_guess[4] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_third_word_guess[4] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_third_word_guess[4] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_third_word_guess[4] == "m":
            Alphabetm.config(bg="Green")

      if list_for_third_word_guess == random_word_letters:
        new_window = Toplevel(window)
        new_window.title("Wordle")
        new_window.geometry("150x150")
        text_win = "You won! Word was: "
        Label_new_window = Label(new_window, text=f"{text_win}{random_word}")
        Label_new_window.pack()
        new_window.mainloop()
        Letter1.config(state="disabled")
        Letter2.config(state="disabled")
        Letter3.config(state="disabled")
        Letter4.config(state="disabled")
        Letter5.config(state="disabled")
        Letter6.config(state="disabled")
        Letter7.config(state="disabled")
        Letter8.config(state="disabled")
        Letter9.config(state="disabled")
        Letter10.config(state="disabled")
        Letter11.config(state="disabled")
        Letter12.config(state="disabled")
        Letter13.config(state="disabled")
        Letter14.config(state="disabled")
        Letter15.config(state="disabled")
        Letter16.config(state="disabled")
        Letter17.config(state="disabled")
        Letter18.config(state="disabled")
        Letter19.config(state="disabled")
        Letter20.config(state="disabled")
        Letter21.config(state="disabled")
        Letter22.config(state="disabled")
        Letter23.config(state="disabled")
        Letter24.config(state="disabled")
        Letter25.config(state="disabled")

      Letter1.config(state="disabled")
      Letter2.config(state="disabled")
      Letter3.config(state="disabled")
      Letter4.config(state="disabled")
      Letter5.config(state="disabled")
      Letter6.config(state="disabled")
      Letter7.config(state="disabled")
      Letter8.config(state="disabled")
      Letter9.config(state="disabled")
      Letter10.config(state="disabled")
      Letter11.config(state="disabled")
      Letter12.config(state="disabled")
      Letter13.config(state="disabled")
      Letter14.config(state="disabled")
      Letter15.config(state="disabled")
      Letter16.config(state="normal")
      Letter17.config(state="normal")
      Letter18.config(state="normal")
      Letter19.config(state="normal")
      Letter20.config(state="normal")
      Letter21.config(state="disabled")
      Letter22.config(state="disabled")
      Letter23.config(state="disabled")
      Letter24.config(state="disabled")
      Letter25.config(state="disabled")


   elif Letters[16].cget("state") == "normal":
      global list_for_fourth_word_guess
      global Letters_4column
      list_for_fourth_word_guess = [Letter16.get(), Letter17.get(), Letter18.get(), Letter19.get(), Letter20.get()]
      if list_for_fourth_word_guess[0] == random_word_letters[0]:
          Letters_4column[0].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[0] == random_word_letters[1]:
          Letters_4column[0].config(disabledbackground="Yellow")
      if list_for_fourth_word_guess[0] == random_word_letters[0]:
          Letters_4column[0].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[0] == random_word_letters[2]:
          Letters_4column[0].config(disabledbackground="Yellow")
      if list_for_fourth_word_guess[0] == random_word_letters[0]:
          Letters_4column[0].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[0] == random_word_letters[3]:
          Letters_4column[0].config(disabledbackground="Yellow")
      if list_for_fourth_word_guess[0] == random_word_letters[0]:
          Letters_4column[0].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[0] == random_word_letters[4]:
          Letters_4column[0].config(disabledbackground="Yellow")
      if list_for_fourth_word_guess[0] == random_word_letters[0]:
          Letters_4column[0].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")

      if list_for_fourth_word_guess[1] == random_word_letters[0]:
          Letters_4column[1].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[1] == random_word_letters[1]:
          Letters_4column[1].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[1] == random_word_letters[2]:
          Letters_4column[1].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[1] == random_word_letters[3]:
          Letters_4column[1].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[1] == random_word_letters[4]:
          Letters_4column[1].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")

      if list_for_fourth_word_guess[2] == random_word_letters[0]:
          Letters_4column[2].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[2] == random_word_letters[1]:
          Letters_4column[2].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")

      elif list_for_fourth_word_guess[2] == random_word_letters[2]:
          Letters_4column[2].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[2] == random_word_letters[3]:
          Letters_4column[2].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[2] == random_word_letters[4]:
          Letters_4column[2].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_fourth_word_guess[3] == random_word_letters[0]:
          Letters_4column[3].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[3] == random_word_letters[1]:
          Letters_4column[3].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[3] == random_word_letters[2]:
          Letters_4column[3].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[3] == random_word_letters[3]:
          Letters_4column[3].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[3] == random_word_letters[4]:
          Letters_4column[3].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")

      if list_for_fourth_word_guess[4] == random_word_letters[0]:
          Letters_4column[4].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[4] == random_word_letters[1]:
          Letters_4column[4].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[4] == random_word_letters[2]:
          Letters_4column[4].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[4] == random_word_letters[3]:
          Letters_4column[4].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fourth_word_guess[4] == random_word_letters[4]:
          Letters_4column[4].config(disabledbackground="Yellow")
          if list_for_fourth_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fourth_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")

        
      if list_for_fourth_word_guess[0] == random_word_letters[0]:
          Letters_4column[0].config(disabledbackground="Green")
          if list_for_fourth_word_guess[0] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "e":
            Alphabete.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "t":
            Alphabett.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "y":
            Alphabety.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "s":
            Alphabets.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_fourth_word_guess[0] == "m":
            Alphabetm.config(bg="Green")
      if list_for_fourth_word_guess[1] == random_word_letters[1]:
          Letters_4column[1].config(disabledbackground="Green")
          if list_for_fourth_word_guess[1] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "e":
            Alphabete.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "t":
            Alphabett.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "y":
            Alphabety.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "s":
            Alphabets.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_fourth_word_guess[1] == "m":
            Alphabetm.config(bg="Green")
      if list_for_fourth_word_guess[2] == random_word_letters[2]:
          Letters_4column[2].config(disabledbackground="Green")
          if list_for_fourth_word_guess[2] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "e":
            Alphabete.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "t":
            Alphabett.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "y":
            Alphabety.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "s":
            Alphabets.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_fourth_word_guess[2] == "m":
            Alphabetm.config(bg="Green")
      if list_for_fourth_word_guess[3] == random_word_letters[3]:
          Letters_4column[3].config(disabledbackground="Green")
          if list_for_fourth_word_guess[3] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "e":
            Alphabete.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "t":
            Alphabett.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "y":
            Alphabety.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "s":
            Alphabets.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_fourth_word_guess[3] == "m":
            Alphabetm.config(bg="Green")
      if list_for_fourth_word_guess[4] == random_word_letters[4]:
          Letters_4column[4].config(disabledbackground="Green")
          if list_for_fourth_word_guess[4] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "e":
            Alphabete.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "t":
            Alphabett.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "y":
            Alphabety.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "s":
            Alphabets.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_fourth_word_guess[4] == "m":
            Alphabetm.config(bg="Green")

      if list_for_fourth_word_guess == random_word_letters:
        new_window = Toplevel(window)
        new_window.title("Wordle")
        new_window.geometry("150x150")
        text_win = "You won! Word was: "
        Label_new_window = Label(new_window, text=f"{text_win}{random_word}")
        Label_new_window.pack()
        new_window.mainloop()
        Letter1.config(state="disabled")
        Letter2.config(state="disabled")
        Letter3.config(state="disabled")
        Letter4.config(state="disabled")
        Letter5.config(state="disabled")
        Letter6.config(state="disabled")
        Letter7.config(state="disabled")
        Letter8.config(state="disabled")
        Letter9.config(state="disabled")
        Letter10.config(state="disabled")
        Letter11.config(state="disabled")
        Letter12.config(state="disabled")
        Letter13.config(state="disabled")
        Letter14.config(state="disabled")
        Letter15.config(state="disabled")
        Letter16.config(state="disabled")
        Letter17.config(state="disabled")
        Letter18.config(state="disabled")
        Letter19.config(state="disabled")
        Letter20.config(state="disabled")
        Letter21.config(state="disabled")
        Letter22.config(state="disabled")
        Letter23.config(state="disabled")
        Letter24.config(state="disabled")
        Letter25.config(state="disabled")


      Letter1.config(state="disabled")
      Letter2.config(state="disabled")
      Letter3.config(state="disabled")
      Letter4.config(state="disabled")
      Letter5.config(state="disabled")
      Letter6.config(state="disabled")
      Letter7.config(state="disabled")
      Letter8.config(state="disabled")
      Letter9.config(state="disabled")
      Letter10.config(state="disabled")
      Letter11.config(state="disabled")
      Letter12.config(state="disabled")
      Letter13.config(state="disabled")
      Letter14.config(state="disabled")
      Letter15.config(state="disabled")
      Letter16.config(state="disabled")
      Letter17.config(state="disabled")
      Letter18.config(state="disabled")
      Letter19.config(state="disabled")
      Letter20.config(state="disabled")
      Letter21.config(state="normal")
      Letter22.config(state="normal")
      Letter23.config(state="normal")
      Letter24.config(state="normal")
      Letter25.config(state="normal")


   elif Letters[21].cget("state") == "normal":
      global list_for_fifth_word_guess
      global Letters_5column
      list_for_fifth_word_guess = [Letter21.get(), Letter22.get(), Letter23.get(), Letter24.get(), Letter25.get()]

      if list_for_fifth_word_guess[0] == random_word_letters[0]:
          Letters_5column[0].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[0] == random_word_letters[1]:
          Letters_5column[0].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[0] == random_word_letters[2]:
          Letters_5column[0].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[0] == random_word_letters[3]:
          Letters_5column[0].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[0] == random_word_letters[4]:
          Letters_5column[0].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[0] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[0] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_fifth_word_guess[1] == random_word_letters[0]:
          Letters_5column[1].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[1] == random_word_letters[1]:
          Letters_5column[1].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[1] == random_word_letters[2]:
          Letters_5column[1].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[1] == random_word_letters[3]:
          Letters_5column[1].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[1] == random_word_letters[4]:
          Letters_5column[1].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[1] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[1] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_fifth_word_guess[2] == random_word_letters[0]:
          Letters_5column[2].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[2] == random_word_letters[1]:
          Letters_5column[2].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[2] == random_word_letters[2]:
          Letters_5column[2].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[2] == random_word_letters[3]:
          Letters_5column[2].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[2] == random_word_letters[4]:
          Letters_5column[2].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[2] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[2] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_fifth_word_guess[3] == random_word_letters[0]:
          Letters_5column[3].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[3] == random_word_letters[1]:
          Letters_5column[3].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[3] == random_word_letters[2]:
          Letters_5column[3].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[3] == random_word_letters[3]:
          Letters_5column[3].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[3] == random_word_letters[4]:
          Letters_5column[3].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[3] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[3] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_fifth_word_guess[4] == random_word_letters[0]:
          Letters_5column[4].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[4] == random_word_letters[1]:
          Letters_5column[4].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[4] == random_word_letters[2]:
          Letters_5column[4].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[4] == random_word_letters[3]:
          Letters_5column[4].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")
      elif list_for_fifth_word_guess[4] == random_word_letters[4]:
          Letters_5column[4].config(disabledbackground="Yellow")
          if list_for_fifth_word_guess[4] == "q":
            Alphabetq.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "w":
            Alphabetw.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "e":
            Alphabete.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "r":
            Alphabetr.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "t":
            Alphabett.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "y":
            Alphabety.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "u":
            Alphabetu.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "i":
            Alphabeti.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "o":
            Alphabeto.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "p":
            Alphabetp.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "a":
            Alphabeta.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "s":
            Alphabets.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "d":
            Alphabetd.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "f":
            Alphabetf.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "g":
            Alphabetg.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "h":
            Alphabeth.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "j":
            Alphabetj.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "k":
            Alphabetk.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "l":
            Alphabetl.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "z":
            Alphabetz.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "x":
            Alphabetx.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "c":
            Alphabetc.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "v":
            Alphabetv.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "b":
            Alphabetb.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "n":
            Alphabetn.config(bg="Yellow")
          elif list_for_fifth_word_guess[4] == "m":
            Alphabetm.config(bg="Yellow")


      if list_for_fifth_word_guess[0] == random_word_letters[0]:
          Letters_5column[0].config(disabledbackground="Green")
          if list_for_fifth_word_guess[0] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "e":
            Alphabete.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "t":
            Alphabett.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "y":
            Alphabety.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "s":
            Alphabets.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_fifth_word_guess[0] == "m":
            Alphabetm.config(bg="Green")
      if list_for_fifth_word_guess[1] == random_word_letters[1]:
          Letters_5column[1].config(disabledbackground="Green")
          if list_for_fifth_word_guess[1] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "e":
            Alphabete.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "t":
            Alphabett.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "y":
            Alphabety.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "s":
            Alphabets.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_fifth_word_guess[1] == "m":
            Alphabetm.config(bg="Green")
      if list_for_fifth_word_guess[2] == random_word_letters[2]:
          Letters_5column[2].config(disabledbackground="Green")
          if list_for_fifth_word_guess[2] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "e":
            Alphabete.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "t":
            Alphabett.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "y":
            Alphabety.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "s":
            Alphabets.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_fifth_word_guess[2] == "m":
            Alphabetm.config(bg="Green")
      if list_for_fifth_word_guess[3] == random_word_letters[3]:
          Letters_5column[3].config(disabledbackground="Green")
          if list_for_fifth_word_guess[3] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "e":
            Alphabete.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "t":
            Alphabett.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "y":
            Alphabety.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "s":
            Alphabets.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_fifth_word_guess[3] == "m":
            Alphabetm.config(bg="Green")
      if list_for_fifth_word_guess[4] == random_word_letters[4]:
          Letters_5column[4].config(disabledbackground="Green")
          if list_for_fifth_word_guess[4] == "q":
            Alphabetq.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "w":
            Alphabetw.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "e":
            Alphabete.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "r":
            Alphabetr.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "t":
            Alphabett.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "y":
            Alphabety.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "u":
            Alphabetu.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "i":
            Alphabeti.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "o":
            Alphabeto.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "p":
            Alphabetp.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "a":
            Alphabeta.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "s":
            Alphabets.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "d":
            Alphabetd.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "f":
            Alphabetf.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "g":
            Alphabetg.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "h":
            Alphabeth.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "j":
            Alphabetj.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "k":
            Alphabetk.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "l":
            Alphabetl.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "z":
            Alphabetz.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "x":
            Alphabetx.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "c":
            Alphabetc.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "v":
            Alphabetv.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "b":
            Alphabetb.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "n":
            Alphabetn.config(bg="Green")
          elif list_for_fifth_word_guess[4] == "m":
            Alphabetm.config(bg="Green")

      if list_for_fifth_word_guess == random_word_letters:
        new_window = Toplevel(window)
        new_window.title("Wordle")
        new_window.geometry("150x150")
        text_win = "You won! Word was: "
        Label_new_window = Label(new_window, text=f"{text_win}{random_word}")
        Label_new_window.pack()
        new_window.mainloop()
        Letter1.config(state="disabled")
        Letter2.config(state="disabled")
        Letter3.config(state="disabled")
        Letter4.config(state="disabled")
        Letter5.config(state="disabled")
        Letter6.config(state="disabled")
        Letter7.config(state="disabled")
        Letter8.config(state="disabled")
        Letter9.config(state="disabled")
        Letter10.config(state="disabled")
        Letter11.config(state="disabled")
        Letter12.config(state="disabled")
        Letter13.config(state="disabled")
        Letter14.config(state="disabled")
        Letter15.config(state="disabled")
        Letter16.config(state="disabled")
        Letter17.config(state="disabled")
        Letter18.config(state="disabled")
        Letter19.config(state="disabled")
        Letter20.config(state="disabled")
        Letter21.config(state="disabled")
        Letter22.config(state="disabled")
        Letter23.config(state="disabled")
        Letter24.config(state="disabled")
        Letter25.config(state="disabled")
      elif not list_for_fifth_word_guess == random_word_letters:
        new_window = Toplevel(window)
        new_window.title("Wordle")
        new_window.geometry("150x150")
        text_win = "You lose, word was: "
        Label_new_window = Label(new_window, text=f"{text_win}{random_word}")
        Label_new_window.pack()
        new_window.mainloop()
        

      Letter1.config(state="disabled")
      Letter2.config(state="disabled")
      Letter3.config(state="disabled")
      Letter4.config(state="disabled")
      Letter5.config(state="disabled")
      Letter6.config(state="disabled")
      Letter7.config(state="disabled")
      Letter8.config(state="disabled")
      Letter9.config(state="disabled")
      Letter10.config(state="disabled")
      Letter11.config(state="disabled")
      Letter12.config(state="disabled")
      Letter13.config(state="disabled")
      Letter14.config(state="disabled")
      Letter15.config(state="disabled")
      Letter16.config(state="disabled")
      Letter17.config(state="disabled")
      Letter18.config(state="disabled")
      Letter19.config(state="disabled")
      Letter20.config(state="disabled")
      Letter21.config(state="disabled")
      Letter22.config(state="disabled")
      Letter23.config(state="disabled")
      Letter24.config(state="disabled")
      Letter25.config(state="disabled")


window.bind("<Return>", enterbutton)


Letter1.place(x=10, y=10)
Letter2.place(x=40, y=10)
Letter3.place(x=70, y=10)
Letter4.place(x=100, y=10)
Letter5.place(x=130, y=10)
Letter6.place(x=10, y=60)
Letter7.place(x=40, y=60)
Letter8.place(x=70, y=60)
Letter9.place(x=100, y=60)
Letter10.place(x=130, y=60)
Letter11.place(x=10, y=110)
Letter12.place(x=40, y=110)
Letter13.place(x=70, y=110)
Letter14.place(x=100, y=110)
Letter15.place(x=130, y=110)
Letter16.place(x=10, y=160)
Letter17.place(x=40, y=160)
Letter18.place(x=70, y=160)
Letter19.place(x=100, y=160)
Letter20.place(x=130, y=160)
Letter21.place(x=10, y=210)
Letter22.place(x=40, y=210)
Letter23.place(x=70, y=210)
Letter24.place(x=100, y=210)
Letter25.place(x=130, y=210)

Alphabetq.place(x=10, y=270)
Alphabetw.place(x=35, y=270)
Alphabete.place(x=60, y=270)
Alphabetr.place(x=85, y=270)
Alphabett.place(x=110, y=270)
Alphabety.place(x=135, y=270)
Alphabetu.place(x=160, y=270)
Alphabeti.place(x=185, y=270)
Alphabeto.place(x=210, y=270)
Alphabetp.place(x=235, y=270)
Alphabeta.place(x=10, y=300)
Alphabets.place(x=35, y=300)
Alphabetd.place(x=60, y=300)
Alphabetf.place(x=85, y=300)
Alphabetg.place(x=110, y=300)
Alphabeth.place(x=135, y=300)
Alphabetj.place(x=160, y=300)
Alphabetk.place(x=185, y=300)
Alphabetl.place(x=210, y=300)
Alphabetz.place(x=10, y=330)
Alphabetx.place(x=35, y=330)
Alphabetc.place(x=60, y=330)
Alphabetv.place(x=85, y=330)
Alphabetb.place(x=110, y=330)
Alphabetn.place(x=135, y=330)
Alphabetm.place(x=160, y=330)


TextWordle.place(x=190, y=10)
FinalUserAnswer.place(x=190, y=100)


window.mainloop()