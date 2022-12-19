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


my_w = tk.Tk()
my_w.geometry("400x400")
my_w.title("Selecione o seu navegador")
global data


e1 = tk.Text(my_w, font=20, height=4, width=28, bg='white')


def install_atuaizador_Brave():
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


def instal_atualizador_Edge():
    global data 
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
    pyautogui.hotkey("enter")
    time.sleep(2)
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
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Enter")



def  instal_atualizador_Chrome():
    global data 
    webbrowser.open("https://update.hifuzion.com.br/")
    time.sleep(3)
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Enter")
    time.sleep(2)
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
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Tab")
    pyautogui.hotkey("Enter")
















b1 = tk.Button(my_w, text='Brave', command=lambda: install_atuaizador_Brave(),
               font=20, bg='cyan')
b1.grid(row=1, column=1, padx=2, pady=5)



    
b2 = tk.Button(my_w, text='edge', command=lambda: instal_atualizador_Edge(),
               font=20, bg='yellow')
b2.grid(row=1, column=2, padx=2, pady=5)

b3 = tk.Button(my_w, text='Chrome', command=lambda: instal_atualizador_Chrome(),
               font=20, bg='green')
b3.grid(row=1, column=3, padx=2, pady=5)


my_w.mainloop()
