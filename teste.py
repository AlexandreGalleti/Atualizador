from cgitb import text
from platform import python_branch
from sqlite3 import Row
import tkinter as tk
import clipboard
from colorama import Fore
import pyautogui
import webbrowser
import time
from os import mkdir, chdir, getcwd, path
import os.path
import copy
import pprint
import doctest
import pyrect
import pyscreeze


my_w = tk.Tk()
my_w.geometry("350x350")
my_w.title("atalho de suporte")
global data


e1 = tk.Text(my_w, font=20, height=4, width=28, bg='white')


def install_atuaizador():
    webbrowser.open("https://update.hifuzion.com.br/")
    time.sleep(3)
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Enter")
    time.sleep(3)
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Enter")
    time.sleep(2)
    pyautogui.hotkey("Enter")
    time.sleep(3)
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Enter")




pas = 'Backup_hifuzion'

cam = path.join(path.expanduser('~'), 'Desktop')
chdir(cam)

if os.path.isdir(pas):
    print(F'A pasta "{pas}" já existe em Desktop!')

else:
    mkdir(pas)
    cam2 = cam + '\\' + pas
    chdir(cam2)
    print(getcwd)





b1 = tk.Button(my_w, text='Passo 1', command=lambda: install_atuaizador(),
               font=20, bg='cyan')
b1.grid(row=1, column=1, padx=2, pady=5)



    



my_w.mainloop()
