# 6.1.1. API сайтов
# 6.1.2. Создаем проект и репозиторий

# Устанавливаем requests

from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Создаем окно
window = Tk()
window.title("Котики")
window.geometry("600x480")

# Создаем метку без изображения
label = Label()
label.pack()

url = 'https://cataas.com/cat'
img = load_image(url)

if img:
    # Устанавливаем изображение в метку
    label.config(image=img)
    # Необходимо сохранить ссылку на изображение, чтобы избежать сборки мусора
    label.image = img  

window.mainloop()

