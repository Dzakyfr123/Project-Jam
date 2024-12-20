import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')  
    label.config(text=current_time)  
    label.after(1000, update_time)  

window = tk.Tk()
window.title("Jam Digital")

label = tk.Label(window, font=('calibri', 40, 'bold'), background='orange', foreground='black')
label.pack(anchor='center')

update_time()

window.mainloop()
