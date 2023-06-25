import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
import time
from playwright.sync_api import sync_playwright
from faker import Faker
from colorama import Fore,Style,init
from termcolor import cprint
from pyfiglet import figlet_format
import threading
import sys
import os
import random
import string
from bs4 import BeautifulSoup
import requests
import re
import wmi
from fake_useragent import UserAgent
from tkinter import simpledialog

init(strip=not sys.stdout.isatty())

def on_action_select():
    action_value = action_var.get()
    if action_value == 1:
        placeholder_function1(number_of_repeatation.get())    
    elif action_value == 2:
        placeholder_function2(number_of_browsers.get(),mode_input.get())
    elif action_value == 3:
        placeholder_function3(number_of_browsers.get(),mode_input.get())
    elif action_value == 4:
        placeholder_function4(number_of_browsers.get(),mode_input.get())
    else:
        pass
    

profile_error_message = "لا يوجد عدد كافى من الحسابات لبدء الوظيفة\nمن فضلك اضف المزيد من الحسابات"

def placeholder_function1(number):
    pass

def placeholder_function2(number_of_browsers,mode):
   pass

def placeholder_function3(number_of_browsers,mode):
    pass
    
def placeholder_function4(number_of_browsers,mode):
    pass

def close_program():
    root.quit()

def get_id():
    try:
        c = wmi.WMI()
        physical_disks = c.Win32_DiskDrive()
        for disk in physical_disks:
            # Check if the disk is a physical hard drive
            if "fixed" in disk.MediaType.lower():
                serial="GDC"+disk.SerialNumber.strip()
                return serial
        return None
    except Exception as e:
        print("Error:", str(e))
    return None 

def get_username():
    name = username_entry.get()
    popup.destroy()
    if name =='':
        name='anonymous'  
    serial_number = get_id()
    if serial_number:
        url = 'https://1100.website/~sakrapi/tebot/api.php' 
        data = {
            'username': name,
            'cpu_id': serial_number
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            result = response.json()
            validation_status = result['validation_status']
            remaining_time = result['remaining_time']
            license_key = result['license_key']
            messagebox.showinfo("Licence info",f"احتفظ بمفتاح الترخيص جيدا \nLicense Key : {license_key} \nRemainig time : {remaining_time} days\nyour version : {validation_status}")
        else:
            messagebox.showerror("خطأ","تأكد من اتصالك بالانترنت\nفى حالة تكرار الخطأ والتاكد من اتصال الانترنت تواصل معنا \nTelegram : @Joker_Python\nTelegram: @JokerOfPython")
            close_program()
    else:
        messagebox.showerror("خطأ","تواصل معنا لفحص الخطأ\nTelegram : @Joker_Python\nTelegram: @JokerOfPython")  
        close_program()
    root.deiconify()  

def version_check():
    serial_number = get_id()
    if serial_number:
        url = 'https://1100.website/~sakrapi/tebot/apii.php' 
        data = {
            'cpu_id': serial_number
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            result = response.json()
            validation_status = result['validation_status']
            remaining_time = result['remaining_time']
            license_key = result['license_key']
            return validation_status,remaining_time,license_key
        else:
            messagebox.showerror("خطأ","تأكد من اتصالك بالانترنت\nفى حالة تكرار الخطأ والتاكد من اتصال الانترنت تواصل معنا \nTelegram : @Joker_Python\nTelegram: @JokerOfPython")
            close_program()
    else:
        messagebox.showerror("خطأ","تواصل معنا لفحص الخطأ\nTelegram : @Joker_Python\nTelegram: @JokerOfPython")  
        close_program()  

root = tk.Tk()
root.title("GoogleDomainsCreation(GDCV1.0)")
root.geometry("500x200")
root.withdraw()

style = ttk.Style()
style.configure("SkyBlue.TFrame", background="sky blue")
style.configure("SkyBlue.TRadiobutton", background="sky blue")
style.configure("SkyBlue.TLabel", background="sky blue")
style.configure("SkyBlue.TEntry", background="sky blue")
style.configure("SkyBlue.TButton", background="sky blue")

icon = tk.PhotoImage(file="images/logo.png")
root.iconphoto(False, icon)

#background_image = tk.PhotoImage(file="images/background.png")
background_label = ttk.Label(root, style="SkyBlue.TLabel")
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

#logo = ttk.Label(root, image=icon ,style="SkyBlue.TLabel")
#logo.pack(pady=10)

frame = ttk.Frame(root,style="SkyBlue.TFrame")
#frame.pack(pady=20)
frame.pack(fill="both", expand=True)

popup = tk.Toplevel(root)
popup.title("Enter Your Name")
popup.geometry("300x200")
popup.protocol("WM_DELETE_WINDOW", get_username)

username_label = ttk.Label(popup, text="Enter your name:")
username_label.pack()

username_entry = ttk.Entry(popup)
username_entry.pack()

submit_button = ttk.Button(popup, text="OK", command=get_username)
submit_button.pack()


action_var = tk.IntVar()
actions = [("تجهيز ملف الدومينات", 1), ("إضافة           الكاباتشا", 2), ("بدأ                    الانشاء", 3), ("فلترة                النتيجة", 4)]
for text, value in actions:
    ttk.Radiobutton(frame, text=text, value=value, variable=action_var,style="SkyBlue.TRadiobutton").grid(column=2, row=value, padx=20, sticky=tk.E)

number_of_repeatation = tk.IntVar()
ttk.Label(frame, text="عدد التكرار",style="SkyBlue.TLabel").grid(column=1, row=1, padx=20, sticky=tk.E)
ttk.Entry(frame, textvariable=number_of_repeatation,style="SkyBlue.TEntry").grid(column=0, row=1, padx=20, sticky=tk.E)

number_of_browsers = tk.IntVar()
ttk.Label(frame, text="عدد المتصفحات",style="SkyBlue.TLabel").grid(column=1, row=2, padx=20, sticky=tk.E)
ttk.Entry(frame, textvariable=number_of_browsers,style="SkyBlue.TEntry").grid(column=0, row=2, padx=20, sticky=tk.E)

mode_input = tk.BooleanVar()
ttk.Label(frame, text="هل تريد إخفاء المتصفح ؟",style="SkyBlue.TLabel").grid(column=1, row=4, padx=20, sticky=tk.W)
ttk.Radiobutton(frame, text="Yes", variable=mode_input, value=True,style="SkyBlue.TRadiobutton").grid(column=0, row=4, padx=(20, 0), sticky=tk.W)
ttk.Radiobutton(frame, text="No", variable=mode_input, value=False,style="SkyBlue.TRadiobutton").grid(column=0, row=4, padx=(80, 0), sticky=tk.W)

submit_button = ttk.Button(frame, text="تنفيذ", command=on_action_select,style="SkyBlue.TButton")
submit_button.grid(column=1, row=5, pady=20, sticky=tk.E)

close_button = ttk.Button(frame, text="إغلاق", command=close_program,style="SkyBlue.TButton")
close_button.grid(column=0, row=5, pady=20, sticky=tk.E)
root.mainloop()
